"""Step 3 - Real-time vehicle detection (and optional tracking) on a video.

Controls while the window is open:
    q / ESC  -> quit
    SPACE    -> pause / resume
    s        -> save a screenshot to outputs/

Usage (from the repo root):
    python src/03_detect_video.py
    python src/03_detect_video.py --source data/videos/traffic.mp4 --conf 0.4
    python src/03_detect_video.py --source 0            # webcam
    python src/03_detect_video.py --track               # count unique vehicles
    python src/03_detect_video.py --save                # write annotated video
"""
import argparse
import time

import cv2
from ultralytics import YOLO

from common import MODEL_PATH, OUTPUT_DIR, VEHICLE_CLASSES, VIDEOS_DIR


def parse_args():
    p = argparse.ArgumentParser(description="YOLOv8 vehicle detection on video")
    p.add_argument("--source", default=str(VIDEOS_DIR / "video.mp4"),
                   help="video path, or 0 for webcam")
    p.add_argument("--model", default=str(MODEL_PATH))
    p.add_argument("--conf", type=float, default=0.4, help="confidence threshold")
    p.add_argument("--width", type=int, default=1080, help="display width (0 = original)")
    p.add_argument("--track", action="store_true", help="enable object tracking (unique IDs)")
    p.add_argument("--save", action="store_true", help="save annotated video to outputs/")
    p.add_argument("--no-show", action="store_true", help="do not open a window")
    return p.parse_args()


def main():
    args = parse_args()
    source = int(args.source) if args.source.isdigit() else args.source

    model = YOLO(args.model)
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise SystemExit(f"Could not open video source: {args.source}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    writer = None
    paused = False
    prev_time = time.time()
    shot_count = 0
    unique_ids = set()
    frame = None

    while True:
        if not paused:
            ok, frame = cap.read()
            if not ok:
                print("Video finished.")
                break

            if args.width and frame.shape[1] != args.width:
                scale = args.width / frame.shape[1]
                frame = cv2.resize(frame, None, fx=scale, fy=scale)

            classes = list(VEHICLE_CLASSES)
            if args.track:
                result = model.track(frame, conf=args.conf, classes=classes,
                                     persist=True, verbose=False)[0]
                if result.boxes.id is not None:
                    unique_ids.update(int(i) for i in result.boxes.id)
            else:
                result = model(frame, conf=args.conf, classes=classes, verbose=False)[0]

            annotated = result.plot()

            # per-class counts for the current frame
            counts = {name: 0 for name in VEHICLE_CLASSES.values()}
            for c in result.boxes.cls:
                counts[VEHICLE_CLASSES[int(c)]] += 1

            now = time.time()
            fps = 1.0 / max(now - prev_time, 1e-6)
            prev_time = now

            lines = [f"FPS: {fps:.1f}", f"Vehicles: {len(result.boxes)}"]
            lines += [f"{k}: {v}" for k, v in counts.items() if v]
            if args.track:
                lines.append(f"Unique: {len(unique_ids)}")
            for n, text in enumerate(lines):
                cv2.putText(annotated, text, (15, 35 + n * 32),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 4)
                cv2.putText(annotated, text, (15, 35 + n * 32),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            if args.save:
                if writer is None:
                    h, w = annotated.shape[:2]
                    fps_in = cap.get(cv2.CAP_PROP_FPS) or 30
                    writer = cv2.VideoWriter(str(OUTPUT_DIR / "detected_video.mp4"),
                                             cv2.VideoWriter_fourcc(*"mp4v"), fps_in, (w, h))
                writer.write(annotated)

        if not args.no_show and frame is not None:
            cv2.imshow("Traffic Robot - YOLOv8", annotated)
            key = cv2.waitKey(1) & 0xFF
            if key in (ord("q"), 27):
                break
            if key == ord(" "):
                paused = not paused
            if key == ord("s"):
                shot_count += 1
                path = OUTPUT_DIR / f"screenshot_{shot_count}.jpg"
                cv2.imwrite(str(path), annotated)
                print(f"Screenshot saved: {path}")

    cap.release()
    if writer is not None:
        writer.release()
        print(f"Annotated video saved to: {OUTPUT_DIR / 'detected_video.mp4'}")
    cv2.destroyAllWindows()
    if args.track:
        print(f"Unique vehicles tracked: {len(unique_ids)}")


if __name__ == "__main__":
    main()

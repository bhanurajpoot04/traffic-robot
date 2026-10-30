"""Step 2 - Run YOLOv8 on a single image.

Prints every detection (class, confidence, box) and saves an annotated image
plus a vehicle count.

Usage (from the repo root):
    python src/02_detect_image.py
    python src/02_detect_image.py --image data/images/cars.jpg --conf 0.4
"""
import argparse

import cv2
from ultralytics import YOLO

from common import IMAGES_DIR, MODEL_PATH, OUTPUT_DIR, VEHICLE_CLASSES


def main():
    parser = argparse.ArgumentParser(description="YOLOv8 detection on an image")
    parser.add_argument("--image", default=str(IMAGES_DIR / "traffic.jpg"))
    parser.add_argument("--model", default=str(MODEL_PATH))
    parser.add_argument("--conf", type=float, default=0.25, help="confidence threshold")
    args = parser.parse_args()

    model = YOLO(args.model)
    img = cv2.imread(args.image)
    if img is None:
        raise SystemExit(f"Could not read image: {args.image}")

    result = model(img, conf=args.conf)[0]
    boxes = result.boxes
    print(f"Total detections: {len(boxes)}")
    print("---")

    vehicles = 0
    for i, box in enumerate(boxes, start=1):
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        confidence = float(box.conf[0])
        x1, y1, x2, y2 = (int(v) for v in box.xyxy[0])
        if class_id in VEHICLE_CLASSES:
            vehicles += 1
        print(f"Detection {i}:")
        print(f"  Class      : {class_name} (ID: {class_id})")
        print(f"  Confidence : {confidence:.2f}")
        print(f"  Box        : ({x1}, {y1}) to ({x2}, {y2})")
        print("---")

    print(f"Vehicles (car/motorcycle/bus/truck): {vehicles}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "detected.jpg"
    cv2.imwrite(str(out_path), result.plot())
    print(f"Annotated image saved to: {out_path}")


if __name__ == "__main__":
    main()


import cv2
import time
from ultralytics import YOLO

# --- Config ---
VIDEO_PATH = 'video.mp4'
WINDOW_SIZE = (1080, 720)
CONFIDENCE = 0.4

# --- Vehicle Classes (YOLO COCO IDs) ---
vehicle_classes = [2, 3, 5, 7]  
# 2=car, 3=motorbike, 5=bus, 7=truck

# --- Model Load ---
model = YOLO('yolov8n.pt')

# --- Video Open ---
cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("❌ Video file nahi mila!")
    exit()

# --- Variables ---
prev_time = 0
paused = False
screenshot_count = 0
annotated_frame = None

# --- Main Loop ---
while cap.isOpened():

    if not paused:
        ret, frame = cap.read()
        if not ret:
            print("Video khatam ho gayi.")
            break

        frame = cv2.resize(frame, WINDOW_SIZE)

        # YOLO Detection
        results = model(frame, conf=CONFIDENCE)[0]

        # Count vehicles
        vehicle_count = 0

        for box in results.boxes:
            cls = int(box.cls[0])
            if cls in vehicle_classes:
                vehicle_count += 1

        # Draw boxes
        annotated_frame = results.plot()

        # FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
        prev_time = current_time

        # Show FPS
        cv2.putText(annotated_frame, f"FPS: {int(fps)}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show Vehicle Count
        cv2.putText(annotated_frame, f"Vehicles: {vehicle_count}", (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Vehicle Detection & Counting", annotated_frame)

    # Controls
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('p'):
        paused = not paused
    elif key == ord('s'):
        if annotated_frame is not None:
            name = f"screenshot_{screenshot_count}.jpg"
            cv2.imwrite(name, annotated_frame)
            print(f"Saved: {name}")
            screenshot_count += 1

# Cleanup
cap.release()
cv2.destroyAllWindows()


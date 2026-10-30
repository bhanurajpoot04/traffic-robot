"""Step 1 - Check that Ultralytics is installed and the YOLOv8n model loads."""
import ultralytics
from ultralytics import YOLO

from common import MODEL_PATH

print("Ultralytics version:", ultralytics.__version__)

# 'n' in yolov8n = nano (smallest and fastest model)
model = YOLO(str(MODEL_PATH))
print("Model loaded!")
print("Number of classes YOLO can detect:", len(model.names))
print("First 10 classes:", list(model.names.values())[:10])

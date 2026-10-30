"""Shared paths and constants for the Traffic Robot project."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "yolov8n.pt"
IMAGES_DIR = ROOT / "data" / "images"
VIDEOS_DIR = ROOT / "data" / "videos"
OUTPUT_DIR = ROOT / "outputs"

# COCO class IDs for vehicles (YOLOv8 is trained on the COCO dataset)
VEHICLE_CLASSES = {2: "car", 3: "motorcycle", 5: "bus", 7: "truck"}

# from ultralytics import YOLO
# import cv2
# # Version check karo
# import ultralytics
# print('Ultralytics version:', ultralytics.__version__)


# from ultralytics import YOLO
# # YOLOv8n load karo — 'n' = nano (sabse chhota aur fast)
# model = YOLO('yolov8n.pt')
# print('Model loaded!')
# print('Classes YOLO detect kar sakta hai:', len(model.names))
# print('Pehli 10 classes:', list(model.names.values()))


# from ultralytics import YOLO
# import cv2
# # Model load karo
# model = YOLO('yolov8n.pt')
# # Image load karo

# img = cv2.imread('cars.jpg')
# # Detection chalao!
# results = model(img)
# print('Detection complete!')
# print('Type of results:', type(results))
# print('Kitne results:', len(results))


from ultralytics import YOLO
import cv2
model = YOLO('yolov8n.pt')
img = cv2.imread('traffic.jpg')
results = model(img)
# Pehle result lo
result = results[0]
boxes = result.boxes
print(f'Total detections: {len(boxes)}')
print('---')
# Har detection ke baare mein print karo
for i, box in enumerate(boxes):
    class_id = int(box.cls[0])
    class_name = model.names[class_id]
    confidence = float(box.conf[0])
    x1, y1, x2, y2 = box.xyxy[0]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    print(f'Detection {i+1}:')
    print(f' Class : {class_name} (ID: {class_id})')
    print(f' Confidence: {confidence:.2f}')
    print(f' Box : ({x1}, {y1}) to ({x2}, {y2})')
    print('---')
from ultralytics import YOLO
import cv2

#version check karo
import ultralytics
print('ultralytics version:',ultralytics.__version__)

from ultralytics import YOLO
model = YOLO('yolov8n.pt')

print ('Model loaded!')
print('classes YOLO detect kar sakta hai:', len(model.names))
print('pehli 10 classes:',list(model.names.values())[:10])


# from ultralytics import YOLO
# import cv2


# model = YOLO('yolov8n.pt')

# img = cv2.imread("")

# results = model(img)

# print('detection complete')
# print('type of results:',type(results))
# print('kitne results:', len(results))


from ultralytics import YOLO

import cv2

model = YOLO('yolov8n.pt')

img = cv2.imread('traffic.png')

results = model(img)

result  = results[0]

# Detected image pe boxes draw karo

for box in result.boxes:

    class_id   = int(box.cls[0])

    class_name = model.names[class_id]

    confidence = float(box.conf[0])

    if confidence < 0.5:        # Low confidence skip karo

        continue
# Smart Traffic System Workshop  |  
#  Page 15

    x1, y1, x2, y2 = map(int, box.xyxy[0])

    # Rectangle draw karo — green box

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Label banao: "car 0.87"

    label = f'{class_name} {confidence:.2f}'

    # Label ke peeche background rectangle

    (lw, lh), _ = cv2.getTextSize(

        label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)

    cv2.rectangle(img,

                  (x1, y1 - lh - 8), (x1 + lw, y1),

                  (0, 255, 0), -1)                 # Filled green

    cv2.putText(img, label, (x1, y1 - 5),

                cv2.FONT_HERSHEY_SIMPLEX, 0.6,

                (0, 0, 0), 2)                      # Black text

# n Puri image screen pe dikhao — fit hogi!

cv2.namedWindow('YOLO Detection', cv2.WINDOW_NORMAL)

cv2.resizeWindow('YOLO Detection', 1280, 720)

cv2.imshow('YOLO Detection', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
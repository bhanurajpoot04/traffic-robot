import cv2
import numpy as np


canvas = np.zeros((480 , 640 , 3) , dtype='uint8')


cv2.rectangle(canvas, (50, 50), (250, 200), (255, 0, 0), 2)

cv2.circle(canvas, (400, 150), 60, (0, 0, 255), 3) 

cv2.line(canvas, (0, 300), (640, 300), (255, 255, 0), 2) #

# cv2.putText(
# canvas,
# 'North Lane: 12 Vehicles', # Text
# (30, 60), # Position (x, y) — top-left se
# cv2.FONT_HERSHEY_SIMPLEX, # Font style
# 0.8, # Font scale (size)
# (0, 255, 0), # Color — Green (BGR)
# 2 # Thickness
# )


# lanes = [('North', 12), ('South', 5), ('East', 20), ('West', 8)]

# for i, (lane, count) in enumerate(lanes):
#     y_pos = 120 + i * 50 # Har line 50px neeche
#     text = f'{lane}: {count} vehicles'
#     cv2.putText(canvas, text, (30, y_pos),
#     cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)



cv2.imshow('Drawing', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     if not ret: break
#     cv2.imshow('Camera', frame)
#     key = cv2.waitKey(1) & 0xFF # & 0xFF = safe way to read key
#     if key == ord('q'): # 'q' = quit
#         print('Quit!')
#         break
#     elif key == ord('s'): # 's' = screenshot save karo
#         cv2.imwrite('screenshot.jpg', frame)
#         print('Screenshot saved!')
#     elif key == ord('g'): # 'g' = grayscale toggle
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow('Gray', gray)

# cap.release()
# cv2.destroyAllWindows()
# import cv2
# # Camera kholo (0 = default camera)
# cap = cv2.VideoCapture(0)
# # Camera properly khula ya nahi?
# if not cap.isOpened():
#     print('Camera nahi mila!')
# else:
#     print('Camera ready hai!')

#     # Ek frame lo aur dikhao
# ret, frame = cap.read() # ret = True/False, frame = image
# if ret:
#     cv2.imshow('My Camera', frame)
#     cv2.waitKey(0)
# cap.release() # Camera band karo
# cv2.destroyAllWindows()



import cv2

cap = cv2.VideoCapture(0)

while True: # Hamesha chalta raho
    ret, frame = cap.read() # Naya frame lo
    if not ret: # Frame nahi mila?
        print('Frame nahi aaya!')
        break
    cv2.imshow('Live Camera', frame) # Frame dikhao
    key = cv2.waitKey(1) # 1ms wait karo
    if key == ord('q'): # 'q' dabate hi band karo
        break
cap.release() # Camera band karo

cv2.destroyAllWindows()

import cv2

print("OPEN CV VERSION : " , cv2.__version__)

import cv2
Image load karo (imread = image read)
img = cv2.imread('traffic.jpg')
Check karo — image mili ya nahi?
if img is None:
 print('Image nahi mili! File ka naam check karo.')
else:
    print('Image successfully load hui!')
    cv2.imshow('Traffic Image', img) # Window mein dikhao
    cv2.waitKey(0) # 0 = koi bhi key dabao tab tak rukho
    cv2.destroyAllWindows() # Saari windows band karo

print('Shape :', img.shape) # (height, width, channels)
print('Size :', img.size) # total pixels
print('Dtype :', img.dtype) # data type
# Alag alag access karo
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
print(f'Height: {height}px | Width: {width}px | Channels: {channels}')


img_bgr = cv2.imread('traffic.jpg') # BGR format mein load hoga
# BGR se RGB convert karo
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# Grayscale (black & white) banana
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original (BGR)', img_bgr)
cv2.imshow('Grayscale', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()



img = cv2.imread('traffic.jpg')
print('Original size:', img.shape)
# Fixed size mein resize karo
img_small = cv2.resize(img, (320, 240)) # (width, height) — dhyan rakhna!
print('Resized size:', img_small.shape)

# Half size karo (percentage se)
h, w = img.shape[:2]
img_half = cv2.resize(img, (w // 2, h // 2))
print('Half size:', img_half.shape)
# Save karo
cv2.imwrite('traffic_small.jpg', img_small)

print('Saved: traffic_small.jpg')
cv2.imshow('Original', img)
cv2.imshow('Resized', img_small)
cv2.waitKey(0)
cv2.destroyAllWindows()
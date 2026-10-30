import cv2

print("OPEN CV VERSION :", cv2.__version__)

# Image load karo (imread = image read)
img = cv2.imread('traffic.jpg')

# Check karo - image mili ya nahi?
if img is None:
    print("Image nahi mili! File ka naam check karo.")
else:
    print("Image successfully load hui!")

    cv2.imshow("Traffic Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Shape :", img.shape)
    print("Size :", img.size)
    print("Dtype :", img.dtype)

    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]

    print(f"Height: {height}px | Width: {width}px | Channels: {channels}")

# ---------------------------------------
# Color Conversion
# ---------------------------------------

img_bgr = cv2.imread('traffic.jpg')

if img_bgr is not None:

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Original (BGR)", img_bgr)
    cv2.imshow("Grayscale", img_gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ---------------------------------------
# Resize Image
# ---------------------------------------

img = cv2.imread('traffic.jpg')

if img is not None:

    print("Original size:", img.shape)

    img_small = cv2.resize(img, (320, 240))

    print("Resized size:", img_small.shape)

    h, w = img.shape[:2]

    img_half = cv2.resize(img, (w // 2, h // 2))

    print("Half size:", img_half.shape)

    cv2.imwrite("traffic_small.jpg", img_small)

    print("Saved: traffic_small.jpg")

    cv2.imshow("Original", img)
    cv2.imshow("Resized", img_small)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
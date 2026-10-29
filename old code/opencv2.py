# import cv2 

# # Camera kholo (0 = default camera)
# cap = cv2.VideoCapture(0)
# # Camera properly khula ya nahi?
# if not cap.isOpened():
#     print('Camera nahi mila!')
# else:
#     print('Camera ready hai!')
# # Ek frame lo aur dikhao
# ret, frame = cap.read() # ret = True/False, frame = image
# if ret:
#     cv2.imshow('My Camera', frame)

# cv2.waitKey(0)
# cap.release() # Camera band karo
# cv2.destroyAllWindows()



# import cv2
# cap = cv2.VideoCapture(0)
# while True: # Hamesha chalta raho
#     ret, frame = cap.read() # Naya frame lo
#     if not ret: # Frame nahi mila?
#         print('Frame nahi aaya!')
#         break
#     cv2.imshow('Live Camera', frame) # Frame dikhao
#     key = cv2.waitKey(1) # 1ms wait karo
#     if key == ord('q'): # 'q' dabate hi band karo
#         break
# cap.release() # Camera band karo
# cv2.destroyAllWindows()



# import cv2
# import numpy as np
# # Blank image banana (kale background pe draw karenge)
# canvas = np.zeros((480, 640, 3), dtype='uint8')
# # Rectangle — bounding box jaise
# # cv2.rectangle(image, top-left, bottom-right, color_BGR, thickness)
# cv2.rectangle(canvas, (50, 50), (250, 200), (0, 255, 0), 5) # Green box
# # Circle — detection center mark karne ke liye
# # cv2.circle(image, center, radius, color_BGR, thickness)
# cv2.circle(canvas, (100, 150), 60, (0, 0, 255), 3) # Red circle
# # Line — lane boundary dikhane ke liye
# # cv2.line(image, start_point, end_point, color_BGR, thickness)
# cv2.line(canvas, (0, 300), (640, 300), (255, 255, 0), 2) # Yellow line

# cv2.imshow('Drawing', canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# import cv2
# import numpy as np
# canvas = np.zeros((480, 640, 3), dtype='uint8')
# # cv2.putText(image, text, position, font, scale, color, thickness)
# cv2.putText(
# canvas,
# 'North Lane: 12 Vehicles', # Text
# (30, 60), # Position (x, y) — top-left se
# cv2.FONT_HERSHEY_SIMPLEX, # Font style
# 0.8, # Font scale (size)
# (0, 255, 0), # Color — Green (BGR)
# 2 # Thickness
# )
# # Multiple lines — alag alag y position
# lanes = [('North', 12), ('South', 5), ('East', 20), ('West', 8)]
# for i, (lane, count) in enumerate(lanes):
#     y_pos = 120 + i * 50 # Har line 50px neeche
# text = f'{lane}: {count} vehicles'
# cv2.putText(canvas, text, (30, y_pos),
# cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
# cv2.imshow('Lane Counter', canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# import cv2

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



# Day 4 Mini Project — Live Traffic Monitor
# import cv2

# cap = cv2.VideoCapture(0)

# # Simulated lane counts (baad mein YOLO se aayenge!)
# lane_counts = {'North': 12, 'South': 5, 'East': 20, 'West': 8}
# frame_number = 0
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

# frame_number += 1
# # === Drawing zone ===
# # Title bar — top pe blue rectangle
# cv2.rectangle(frame, (0, 0), (640, 40), (180, 95, 24), -1) # -1=filled
# cv2.putText(frame, 'SMART TRAFFIC MONITOR', (10, 28),
# cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
# # Lane counts dikhao
# for i, (lane, count) in enumerate(lane_counts.items()):
#     y = 80 + i * 35
#     color = (0, 255, 0) if count > 10 else (0, 200, 255)
#     cv2.putText(frame, f'{lane}: {count} vehicles',
#     (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
# # Frame counter — bottom right
#     cv2.putText(frame, f'Frame: {frame_number}', (480, 460),
#     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)
# # Busiest lane highlight karo
#     busiest = max(lane_counts, key=lane_counts.get)
#     cv2.putText(frame, f'Busiest: {busiest}!', (10, 240),
#     cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
#     cv2.imshow('Traffic Monitor', frame)
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord('q'):
#         break
#     elif key == ord('s'):
#         cv2.imwrite('monitor_screenshot.jpg', frame)
#         print('Screenshot saved!')
# cap.release()
# cv2.destroyAllWindows()


# import cv2

# cap = cv2.VideoCapture(0)

# # Simulated lane counts (later YOLO se replace karenge)
# lane_counts = {
#     'North': 12,
#     'South': 5,
#     'East': 20,
#     'West': 8
# }

# frame_number = 0

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     frame_number += 1

#     # =========================
#     # Title Bar
#     # =========================
#     cv2.rectangle(frame, (0, 0), (640, 40), (180, 95, 24), -1)

#     cv2.putText(
#         frame,
#         'SMART TRAFFIC MONITOR',
#         (10, 28),
#         cv2.FONT_HERSHEY_SIMPLEX,
#         0.7,
#         (255, 255, 255),
#         2
#     )

#     # =========================
#     # Lane Counts
#     # =========================
#     for i, (lane, count) in enumerate(lane_counts.items()):

#         y = 80 + i * 35

#         # High traffic => green
#         color = (0, 255, 0) if count > 10 else (0, 200, 255)

#         cv2.putText(
#             frame,
#             f'{lane}: {count} vehicles',
#             (10, y),
#             cv2.FONT_HERSHEY_SIMPLEX,
#             0.6,
#             color,
#             2
#         )

#     # =========================
#     # Frame Counter
#     # =========================
#     cv2.putText(
#         frame,
#         f'Frame: {frame_number}',
#         (480, 460),
#         cv2.FONT_HERSHEY_SIMPLEX,
#         0.5,
#         (150, 150, 150),
#         1
#     )

#     # =========================
#     # Busiest Lane
#     # =========================
#     busiest = max(lane_counts, key=lane_counts.get)

#     cv2.putText(
#         frame,
#         f'Busiest: {busiest}!',
#         (10, 240),
#         cv2.FONT_HERSHEY_SIMPLEX,
#         0.8,
#         (0, 0, 255),
#         2
#     )

#     # =========================
#     # Show Window
#     # =========================
#     cv2.imshow('Traffic Monitor', frame)

#     key = cv2.waitKey(1) & 0xFF

#     # Quit
#     if key == ord('q'):
#         break

#     # Save Screenshot
#     elif key == ord('s'):
#         cv2.imwrite('monitor_screenshot.jpg', frame)
#         print('Screenshot saved!')

# cap.release()
# cv2.destroyAllWindows()



# import cv2
# import numpy as np

# # Open webcam
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     # Get frame height and width
#     height, width, _ = frame.shape

#     # Center point
#     center_x = width // 2
#     center_y = height // 2

#     # Triangle size
#     size = 80

#     # Triangle points
#     points = np.array([
#         [center_x, center_y - size],          # Top point
#         [center_x - size, center_y + size],   # Bottom left
#         [center_x + size, center_y + size]    # Bottom right
#     ], np.int32)

#     points = points.reshape((-1, 1, 2))

#     # Draw white triangle
#     cv2.polylines(
#         frame,
#         [points],
#         isClosed=True,
#         color=(255, 255, 255),  # White
#         thickness=3
#     )

#     # Show camera feed
#     cv2.imshow("Triangle Center Feed", frame)

#     # Press Q to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()



# import cv2
# import random

# # Open webcam
# cap = cv2.VideoCapture(0)

# # Random emoji lists
# top_emojis = ["😎", "🔥", "🚀", "🤖", "🎯", "⚡"]
# bottom_emojis = ["😂", "🥶", "💀", "👀", "🎮", "✨"]

# # Select random emojis
# top_emoji = random.choice(top_emojis)
# bottom_emoji = random.choice(bottom_emojis)

# screenshot_count = 0

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     # Get frame dimensions
#     height, width, _ = frame.shape

#     # =========================
#     # CENTER TEXT
#     # =========================
#     text = "HELLO WORLD"

#     font = cv2.FONT_HERSHEY_SIMPLEX
#     scale = 1.2
#     thickness = 3

#     # Get text size
#     text_size = cv2.getTextSize(text, font, scale, thickness)[0]

#     text_x = (width - text_size[0]) // 2
#     text_y = (height + text_size[1]) // 2

#     # Draw text
#     cv2.putText(
#         frame,
#         text,
#         (text_x, text_y),
#         font,
#         scale,
#         (255, 255, 255),
#         thickness
#     )

#     # =========================
#     # TOP EMOJI
#     # =========================
#     cv2.putText(
#         frame,
#         top_emoji,
#         (width // 2 - 20, 50),
#         cv2.FONT_HERSHEY_SIMPLEX,
#         1.5,
#         (0, 255, 255),
#         3
#     )

#     # =========================
#     # BOTTOM EMOJI
#     # =========================
#     cv2.putText(
#         frame,
#         bottom_emoji,
#         (width // 2 - 20, height - 30),
#         cv2.FONT_HERSHEY_SIMPLEX,
#         1.5,
#         (255, 0, 255),
#         3
#     )

#     # =========================
#     # SHOW WINDOW
#     # =========================
#     cv2.imshow("Emoji Camera", frame)

#     key = cv2.waitKey(1) & 0xFF

#     # Quit
#     if key == ord('q'):
#         break

#     # Screenshot
#     elif key == ord('s'):
#         screenshot_name = f"screenshot_{screenshot_count}.jpg"

#         cv2.imwrite(screenshot_name, frame)

#         print(f"Saved: {screenshot_name}")

#         screenshot_count += 1

#         # New random emojis after screenshot
#         top_emoji = random.choice(top_emojis)
#         bottom_emoji = random.choice(bottom_emojis)

# # Cleanup
# cap.release()
# cv2.destroyAllWindows()
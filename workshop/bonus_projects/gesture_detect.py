"""
gesture_detect.py
-----------------
Hand Gesture DETECTOR — captures webcam feed, tracks hand landmarks
via MediaPipe, and prints the detected gesture name in real time.
 
Requirements:
    pip install opencv-python mediapipe
"""
 
import cv2
import mediapipe as mp
 
# ── MediaPipe setup ───────────────────────────────────────────────
mp_hands   = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
 
# Tip landmark IDs for each finger
FINGER_TIPS = [8, 12, 16, 20]
THUMB_TIP   = 4
 
def fingers_up(hand_landmarks):
    """
    Returns [thumb, index, middle, ring, pinky] as booleans.
    True = finger extended, False = curled.
    """
    lm = hand_landmarks.landmark
    fingers = []
 
    # Thumb: compare x (for right hand facing camera)
    fingers.append(lm[THUMB_TIP].x < lm[THUMB_TIP - 1].x)
 
    # Four fingers: tip y < pip y → finger is up
    for tip_id in FINGER_TIPS:
        fingers.append(lm[tip_id].y < lm[tip_id - 2].y)
 
    return fingers  # [thumb, index, middle, ring, pinky]
 
def classify_gesture(fingers):
    """Map finger-state list to a gesture name."""
    thumb, index, middle, ring, pinky = fingers
    up_count = sum(fingers)
 
    if up_count == 0:                                         return "FIST"
    if up_count == 5:                                         return "OPEN HAND"
    if index and not middle and not ring and not pinky:       return "POINTING"
    if index and middle and not ring and not pinky:           return "PEACE / VICTORY"
    if thumb and not index and not middle and not ring and not pinky: return "THUMBS UP"
    if thumb and pinky and not index and not middle and not ring:     return "CALL ME"
    if index and middle and ring and pinky and not thumb:     return "FOUR FINGERS"
    if not thumb and not index and not middle and not ring and pinky: return "PINKY"
    return f"CUSTOM ({up_count} fingers)"
 
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        return
 
    print("Gesture Detector running — press Q to quit")
 
    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.75,
        min_tracking_confidence=0.75,
    ) as hands:
 
        while True:
            ret, frame = cap.read()
            if not ret:
                break
 
            frame  = cv2.flip(frame, 1)
            rgb    = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)
 
            label = "No Hand Detected"
 
            if result.multi_hand_landmarks:
                for hand_lm in result.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_lm, mp_hands.HAND_CONNECTIONS)
                    label = classify_gesture(fingers_up(hand_lm))
                    print(f"Detected: {label}")
 
            cv2.rectangle(frame, (0, 0), (440, 60), (0, 0, 0), -1)
            cv2.putText(frame, label, (10, 42),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 120), 2, cv2.LINE_AA)
 
            cv2.imshow("Gesture Detector", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
 
    cap.release()
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()

import cv2
import mediapipe as mp
import pyautogui
import math
import time
 
mp_hands   = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
 
FINGER_TIPS = [8, 12, 16, 20]
THUMB_TIP   = 4
 
# ── Cooldown to prevent gesture spam ─────────────────────────────
COOLDOWN    = 0.8   # seconds between action triggers
last_action = 0.0
 
# ── Finger state ──────────────────────────────────────────────────
def fingers_up(lm):
    fingers = [lm[THUMB_TIP].x < lm[THUMB_TIP - 1].x]
    for tip in FINGER_TIPS:
        fingers.append(lm[tip].y < lm[tip - 2].y)
    return fingers  # [thumb, index, middle, ring, pinky]
 
# ── Distance between two landmarks ───────────────────────────────
def landmark_distance(lm, id1, id2, w, h):
    x1, y1 = int(lm[id1].x * w), int(lm[id1].y * h)
    x2, y2 = int(lm[id2].x * w), int(lm[id2].y * h)
    return math.hypot(x2 - x1, y2 - y1), (x1, y1), (x2, y2)
 
# ── Gesture → Action map ──────────────────────────────────────────
def execute_gesture(fingers, lm, w, h, frame):
    global last_action
    now = time.time()
 
    thumb, index, middle, ring, pinky = fingers
    up_count = sum(fingers)
    action   = None
 
    # ── FIST → Mute / Pause media ────────────────────────────────
    if up_count == 0:
        action = "FIST — Mute / Pause"
        if now - last_action > COOLDOWN:
            pyautogui.press("volumemute")
            last_action = now
 
    # ── OPEN HAND → Play / Unmute ────────────────────────────────
    elif up_count == 5:
        action = "OPEN HAND — Play / Unmute"
        if now - last_action > COOLDOWN:
            pyautogui.press("volumemute")
            last_action = now
 
    # ── POINTING (index only) → Move Mouse ───────────────────────
    elif index and not middle and not ring and not pinky:
        action = "POINTING — Mouse Move"
        tip_x = int(lm[8].x * w)
        tip_y = int(lm[8].y * h)
        screen_w, screen_h = pyautogui.size()
        mouse_x = int(tip_x / w * screen_w)
        mouse_y = int(tip_y / h * screen_h)
        pyautogui.moveTo(mouse_x, mouse_y, duration=0.05)
        cv2.circle(frame, (tip_x, tip_y), 12, (0, 255, 0), -1)
 
    # ── PEACE (index + middle) → Volume Up ───────────────────────
    elif index and middle and not ring and not pinky:
        action = "PEACE — Volume Up"
        if now - last_action > COOLDOWN:
            pyautogui.press("volumeup")
            last_action = now
 
    # ── THUMBS UP → Next Track ───────────────────────────────────
    elif thumb and not index and not middle and not ring and not pinky:
        action = "THUMBS UP — Next Track"
        if now - last_action > COOLDOWN:
            pyautogui.hotkey("ctrl", "right")
            last_action = now
 
    # ── CALL ME (thumb + pinky) → Previous Track ─────────────────
    elif thumb and pinky and not index and not middle and not ring:
        action = "CALL ME — Previous Track"
        if now - last_action > COOLDOWN:
            pyautogui.hotkey("ctrl", "left")
            last_action = now
 
    # ── FOUR FINGERS → Screenshot ────────────────────────────────
    elif index and middle and ring and pinky and not thumb:
        action = "FOUR FINGERS — Screenshot"
        if now - last_action > COOLDOWN:
            pyautogui.hotkey("win", "shift", "s")
            last_action = now
 
    # ── PINCH (thumb + index close) → Left Click ─────────────────
    else:
        dist, pt1, pt2 = landmark_distance(lm, THUMB_TIP, 8, w, h)
        if dist < 40:
            action = "PINCH — Left Click"
            if now - last_action > COOLDOWN:
                pyautogui.click()
                last_action = now
            cv2.line(frame, pt1, pt2, (255, 0, 0), 3)
 
    return action or f"CUSTOM ({up_count} fingers)"
 
 
# ── Main loop ─────────────────────────────────────────────────────
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        return
 
    print("Gesture Controller running — press Q to quit")
    print("Gestures mapped:")
    print("  FIST          → Mute / Pause")
    print("  OPEN HAND     → Play / Unmute")
    print("  POINTING      → Move Mouse")
    print("  PEACE         → Volume Up")
    print("  THUMBS UP     → Next Track")
    print("  CALL ME       → Previous Track")
    print("  FOUR FINGERS  → Screenshot")
    print("  PINCH         → Left Click")
 
    pyautogui.FAILSAFE = False  # disable corner failsafe for smooth mouse control
 
    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.75,
        min_tracking_confidence=0.75,
    ) as hands:
 
        while True:
            ret, frame = cap.read()
            if not ret:
                break
 
            h, w, _ = frame.shape
            frame    = cv2.flip(frame, 1)
            rgb      = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result   = hands.process(rgb)
 
            action_label = "No Hand Detected"
 
            if result.multi_hand_landmarks:
                for hand_lm in result.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_lm, mp_hands.HAND_CONNECTIONS)
                    lm      = hand_lm.landmark
                    fingers = fingers_up(lm)
                    action_label = execute_gesture(fingers, lm, w, h, frame)
 
            # HUD overlay
            cv2.rectangle(frame, (0, 0), (640, 65), (20, 20, 20), -1)
            cv2.putText(frame, action_label, (10, 45),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 200, 255), 2, cv2.LINE_AA)
 
            cv2.imshow("Gesture Controller", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
 
    cap.release()
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()

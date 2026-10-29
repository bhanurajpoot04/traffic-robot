"""
🎨 Live Webcam Drawing Canvas - eSkills
Draw anything using a colored object (blue pen cap, marker lid, etc.)
Controls shown on screen. Press 'Q' to quit.
"""

import cv2
import numpy as np
import time
import os

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
CANVAS_ALPHA = 0.7          # drawing layer opacity
TRAIL_LENGTH = 64           # smoothing trail length
SAVE_DIR = os.path.expanduser("~/Desktop")

# HSV color ranges for the tracking object
# Default: BLUE object (change if needed)
COLOR_RANGES = {
    "blue":   ([100, 120, 70],  [130, 255, 255]),
    "red":    ([0,   120, 70],  [10,  255, 255]),
    "green":  ([40,  120, 70],  [80,  255, 255]),
    "yellow": ([20,  120, 70],  [35,  255, 255]),
}

# Brush palette (BGR colors)
BRUSHES = {
    "Red":     (0,   0,   220),
    "Orange":  (0,   140, 255),
    "Yellow":  (0,   220, 220),
    "Green":   (50,  200, 50),
    "Cyan":    (220, 200, 0),
    "Blue":    (220, 80,  0),
    "Purple":  (200, 0,   180),
    "White":   (255, 255, 255),
    "Black":   (20,  20,  20),
    "Eraser":  None,
}

BRUSH_NAMES = list(BRUSHES.keys())
BRUSH_SIZES = [4, 8, 14, 22, 36]


# ─────────────────────────────────────────────
# HELPER: Draw rounded rect
# ─────────────────────────────────────────────
def rounded_rect(img, x, y, w, h, r, color, thickness=-1):
    cv2.rectangle(img, (x + r, y), (x + w - r, y + h), color, thickness)
    cv2.rectangle(img, (x, y + r), (x + w, y + h - r), color, thickness)
    cv2.circle(img, (x + r,     y + r),     r, color, thickness)
    cv2.circle(img, (x + w - r, y + r),     r, color, thickness)
    cv2.circle(img, (x + r,     y + h - r), r, color, thickness)
    cv2.circle(img, (x + w - r, y + h - r), r, color, thickness)


# ─────────────────────────────────────────────
# MAIN APP
# ─────────────────────────────────────────────
def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Cannot open webcam!")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    ret, frame = cap.read()
    H, W = frame.shape[:2]

    canvas      = np.zeros((H, W, 3), dtype=np.uint8)   # drawing layer
    ui_layer    = np.zeros((H, W, 3), dtype=np.uint8)   # persistent UI

    current_brush   = 0          # index into BRUSH_NAMES
    current_size    = 1          # index into BRUSH_SIZES
    track_color     = "blue"     # which object color to track
    pts             = []         # smoothing trail
    drawing         = False
    last_pt         = None
    show_help       = True
    save_flash      = 0          # countdown for save flash

    # ── toolbar layout ─────────────────────────────
    TOOLBAR_H    = 60
    SWATCH_W     = 52
    SWATCH_H     = 44
    SWATCH_PAD   = 6
    START_X      = 10
    SWATCH_Y     = (TOOLBAR_H - SWATCH_H) // 2

    cv2.namedWindow("🎨 Drawing Canvas", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("🎨 Drawing Canvas", W, H)

    fps_time = time.time()
    fps = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)   # mirror

        # ── FPS ────────────────────────────────────
        now     = time.time()
        fps     = int(1 / max(now - fps_time, 0.001))
        fps_time = now

        # ── Color tracking ─────────────────────────
        hsv  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lo   = np.array(COLOR_RANGES[track_color][0])
        hi   = np.array(COLOR_RANGES[track_color][1])
        mask = cv2.inRange(hsv, lo, hi)

        # For red, also check upper range
        if track_color == "red":
            lo2   = np.array([170, 120, 70])
            hi2   = np.array([180, 255, 255])
            mask  = cv2.bitwise_or(mask, cv2.inRange(hsv, lo2, hi2))

        mask = cv2.erode(mask,  None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cx, cy = None, None
        if cnts:
            c    = max(cnts, key=cv2.contourArea)
            area = cv2.contourArea(c)
            if area > 800:
                (x, y), radius = cv2.minEnclosingCircle(c)
                cx, cy = int(x), int(y)

        # ── Smoothing ──────────────────────────────
        pts.append((cx, cy))
        if len(pts) > TRAIL_LENGTH:
            pts.pop(0)

        # ── Draw on canvas ─────────────────────────
        if cx is not None and cy is not None:
            brush_name = BRUSH_NAMES[current_brush]
            color      = BRUSHES[brush_name]
            size       = BRUSH_SIZES[current_size]

            if last_pt is not None:
                if brush_name == "Eraser":
                    cv2.line(canvas, last_pt, (cx, cy), (0, 0, 0), size * 4)
                else:
                    cv2.line(canvas, last_pt, (cx, cy), color, size)
                    cv2.circle(canvas, (cx, cy), size // 2, color, -1)

            last_pt = (cx, cy)

            # visual indicator on frame
            indicator_color = color if brush_name != "Eraser" else (180, 180, 180)
            cv2.circle(frame, (cx, cy), max(size, 8), indicator_color, 2)
            cv2.circle(frame, (cx, cy), 3, (255, 255, 255), -1)
        else:
            last_pt = None

        # ── Blend canvas onto frame ─────────────────
        out = frame.copy()
        mask_c = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        _, mask_c = cv2.threshold(mask_c, 1, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask_c)

        fg = cv2.bitwise_and(canvas, canvas, mask=mask_c)
        bg = cv2.bitwise_and(out,    out,    mask=mask_inv)
        blend = cv2.addWeighted(fg, CANVAS_ALPHA, fg, 0, 0)
        out = cv2.add(bg, blend)

        # ── Draw toolbar bg ─────────────────────────
        cv2.rectangle(out, (0, 0), (W, TOOLBAR_H), (15, 15, 20), -1)
        cv2.line(out, (0, TOOLBAR_H), (W, TOOLBAR_H), (60, 60, 80), 1)

        # ── Color swatches ──────────────────────────
        for i, bname in enumerate(BRUSH_NAMES):
            bcolor = BRUSHES[bname]
            bx = START_X + i * (SWATCH_W + SWATCH_PAD)
            by = SWATCH_Y

            # Selection highlight
            if i == current_brush:
                rounded_rect(out, bx - 3, by - 3, SWATCH_W + 6, SWATCH_H + 6, 5,
                             (255, 255, 255), 2)

            draw_color = bcolor if bcolor else (50, 50, 50)
            rounded_rect(out, bx, by, SWATCH_W, SWATCH_H, 5, draw_color, -1)

            if bname == "Eraser":
                cv2.putText(out, "ERZ", (bx + 4, by + SWATCH_H - 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (180, 180, 180), 1)
            else:
                cv2.putText(out, bname[:3].upper(), (bx + 6, by + SWATCH_H - 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.38, (255, 255, 255), 1)

        # ── Size indicators ─────────────────────────
        size_x = START_X + len(BRUSH_NAMES) * (SWATCH_W + SWATCH_PAD) + 20
        cv2.putText(out, "SIZE", (size_x, SWATCH_Y + 16),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (150, 150, 180), 1)
        for i, sz in enumerate(BRUSH_SIZES):
            sx = size_x + i * 38
            sy = SWATCH_Y + 35
            col = (255, 230, 100) if i == current_size else (120, 120, 140)
            cv2.circle(out, (sx + 14, sy), max(sz // 2, 3), col, -1)
            if i == current_size:
                cv2.circle(out, (sx + 14, sy), max(sz // 2, 3) + 2, (255, 255, 255), 1)

        # ── Track color selector ────────────────────
        tc_x = W - 260
        cv2.putText(out, "TRACK:", (tc_x, SWATCH_Y + 16),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.42, (150, 150, 180), 1)
        tc_colors = list(COLOR_RANGES.keys())
        tc_display = {"blue": (220, 80, 0), "red": (0, 0, 220),
                      "green": (50, 200, 50), "yellow": (0, 220, 220)}
        for i, tc in enumerate(tc_colors):
            tx = tc_x + i * 50
            ty = SWATCH_Y + 22
            col = tc_display[tc]
            cv2.circle(out, (tx + 10, ty + 10), 12, col, -1)
            if tc == track_color:
                cv2.circle(out, (tx + 10, ty + 10), 14, (255, 255, 255), 2)

        # ── FPS ────────────────────────────────────
        cv2.putText(out, f"FPS:{fps}", (W - 70, H - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (80, 80, 100), 1)

        # ── Help overlay ────────────────────────────
        if show_help:
            tips = [
                "Hold a COLORED object in front of cam to draw",
                "[1-9/0] Select brush color    [Z] Eraser",
                "[+/-]   Brush size            [C] Clear canvas",
                "[S]     Save drawing          [H] Hide help",
                "[B/R/G/Y] Track blue/red/green/yellow object",
                "[Q]     Quit",
            ]
            bx, by = 20, H - len(tips) * 26 - 20
            cv2.rectangle(out, (bx - 8, by - 8),
                          (bx + 420, by + len(tips) * 26 + 4), (10, 10, 20), -1)
            cv2.rectangle(out, (bx - 8, by - 8),
                          (bx + 420, by + len(tips) * 26 + 4), (60, 60, 80), 1)
            for j, tip in enumerate(tips):
                cv2.putText(out, tip, (bx, by + j * 26 + 18),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.48, (200, 220, 255), 1)

        # ── Save flash ──────────────────────────────
        if save_flash > 0:
            cv2.putText(out, "✓ SAVED!", (W // 2 - 60, H // 2),
                        cv2.FONT_HERSHEY_DUPLEX, 1.2, (100, 255, 100), 2)
            save_flash -= 1

        cv2.imshow("🎨 Drawing Canvas", out)

        # ── Key handling ────────────────────────────
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q') or key == 27:
            break
        elif key == ord('c'):
            canvas[:] = 0
        elif key == ord('s'):
            fname = os.path.join(SAVE_DIR, f"drawing_{int(time.time())}.png")
            combo = cv2.addWeighted(frame, 0.5, canvas, 0.8, 0)
            cv2.imwrite(fname, combo)
            print(f"💾 Saved to {fname}")
            save_flash = 60
        elif key == ord('h'):
            show_help = not show_help
        elif key == ord('z'):
            current_brush = BRUSH_NAMES.index("Eraser")
        elif key == ord('+') or key == ord('='):
            current_size = min(current_size + 1, len(BRUSH_SIZES) - 1)
        elif key == ord('-'):
            current_size = max(current_size - 1, 0)
        elif key == ord('b'):
            track_color = "blue"
        elif key == ord('r'):
            track_color = "red"
        elif key == ord('g'):
            track_color = "green"
        elif key == ord('y'):
            track_color = "yellow"
        elif ord('1') <= key <= ord('9'):
            idx = key - ord('1')
            if idx < len(BRUSH_NAMES) - 1:  # exclude eraser
                current_brush = idx
        elif key == ord('0'):
            current_brush = min(9, len(BRUSH_NAMES) - 1)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
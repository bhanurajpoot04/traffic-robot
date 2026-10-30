# Workshop Code (day-wise, original)

These are the scripts written by hand during the **Smart Traffic System Workshop**, kept
exactly as they were tested. Many lines are commented out on purpose: each block is one
exercise from the day's PDF, un-commented while practising.

> These scripts load media by plain filename (e.g. `traffic.jpg`, `video.mp4`, `yolov8n.pt`).
> Run them from a folder that contains those files, for example
> `cd workshop/day5_yolo` after copying the needed files from `data/` and `models/` next to the script.
> For ready-to-run versions that find their own paths, use the scripts in [`../src`](../src).

| Folder | Day | Files | What it covers |
|---|---|---|---|
| `day1-2_python/` | Day 1-2 | `hello.py` | Variables, if/elif/else, match-case, lists, dicts, loops, functions |
| `day3-4_opencv/` | Day 3-4 | `opencv.py`, `opencv2.py`, `opencv_revise.py`, `webcam.py` | Read/show images, BGR vs RGB, resize/save, webcam loop, drawing shapes & text, traffic-monitor mini project |
| `day5_yolo/` | Day 5 | `yolo.py`, `yolos.py`, `video.py` | Load YOLOv8n, read detections, draw boxes, **real-time vehicle detection & counting on video** (FPS, pause, screenshot) |
| `bonus_projects/` | Extra | `air_drawing_canvas.py`, `gesture_detect.py`, `gesture_control.py` | Colour-tracking air-drawing canvas; MediaPipe hand-gesture detector and gesture-controlled mouse/volume |

Notes
- `day5_yolo/video.py` is the main working demo (see `demo/working_demo.mp4`). Keys: `p` pause, `s` screenshot, `q` quit.
- `hello.py` uses `match-case`, so it needs **Python 3.10+**.
- `gesture_*.py` need `pip install -r requirements-extras.txt`. `gesture_control.py` really moves the mouse and presses media keys, so keep your hand in front of the camera and press `q` to stop.
- `gesture_detect.py` and `gesture_control.py` were one file (`gesturesample.py`) with two programs; they are split here so each one runs on its own.

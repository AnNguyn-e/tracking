# YOLOv8 Object Detection & Dice Detection Project

A comprehensive object detection project using YOLOv8 with specialized dice detection capabilities for counting pip numbers on dice faces. Includes image upload, real-time detection, and visual representation with matplotlib drawings.

## Project Structure

```
PBL5/
├── data/                    # Input images/videos
├── models/                  # Saved model weights
├── results/                 # Output results (detection results, visualizations, text files)
├── utils/
│   ├── __init__.py         # Package initialization
│   ├── detector.py         # YOLOv8 detector class
│   ├── dice_detector.py    # Specialized dice detection module
│   └── visualizer.py       # Visualization with matplotlib
├── detect.py               # Main detection script
├── gui_app.py              # GUI application for dice detection
├── config.yaml             # Configuration file
├── requirements.txt        # Python dependencies
├── notebook.ipynb          # Jupyter notebook
└── README.md              # This file
```

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. The YOLOv8 model weights will be downloaded automatically on first use.

## Usage

### Command Line

Detect objects in an image:

```bash
python detect.py --source ./data/image.jpg --save ./results/output.jpg
```

Detect objects in a video:

```bash
python detect.py --source ./data/video.mp4 --save ./results/output.mp4
```

Real-time webcam detection:

```bash
python detect.py --source 0
```

### Configuration

Edit `config.yaml` to customize:

- Model size (yolov8n, yolov8s, yolov8m, yolov8l, yolov8x)
- Confidence threshold
- Device (GPU/CPU)
- Input/output paths

### Python API

```python
from utils.detector import YOLOv8Detector

detector = YOLOv8Detector(model_name="yolov8m", conf_threshold=0.45)

# Image detection
results = detector.detect_image("image.jpg", save_path="output.jpg")

# Video detection
detector.detect_video("video.mp4", save_path="output.mp4")

# Webcam detection
detector.detect_webcam(save_path="webcam_output.mp4")
```

## Models Available

| Model   | Size        | Speed   | Accuracy  |
| ------- | ----------- | ------- | --------- |
| YOLOv8n | Nano        | Fastest | Good      |
| YOLOv8s | Small       | Fast    | Better    |
| YOLOv8m | Medium      | Medium  | Best      |
| YOLOv8l | Large       | Slower  | Excellent |
| YOLOv8x | Extra Large | Slowest | Best      |

## Features

### Object Detection

- ✅ Real-time object detection
- ✅ Image detection
- ✅ Video detection
- ✅ Webcam support
- ✅ Customizable confidence threshold
- ✅ GPU/CPU support
- ✅ Configurable via YAML
- ✅ Easy-to-use API

### Dice Detection (NEW!)

- 🎲 Automatic pip counting (1-6 pips per die)
- 📊 Visual dice face diagrams using matplotlib
- 📁 Image upload from device
- 💾 Save results to text and JSON files
- 🖼️ Annotated image with bounding boxes and pip numbers
- 📈 Batch processing support
- 🎨 Beautiful GUI interface with Vietnamese/English support
- ⚡ Real-time detection with confidence scores

## Requirements

- Python 3.8+
- PyTorch
- OpenCV
- Ultralytics YOLOv8
- Matplotlib
- PIL/Pillow

## Example: Dice Detection Output

When using dice detection, the following files are created in `./results/`:

1. **dice_detection_results.txt** - Text file with Vietnamese/English results
2. **dice_detection_results.json** - JSON format for programmatic access
3. **dice_detection_result.jpg** - Annotated image with bounding boxes
4. **dice_visualization.png** - Visual representation of detected dice faces

## Output Files

When using dice detection, the following files are created in `./results/`:

1. **dice_detection_results.txt** - Text file with Vietnamese/English results
2. **dice_detection_results.json** - JSON format for programmatic access
3. **dice_detection_result.jpg** - Annotated image with bounding boxes
4. **dice_visualization.png** - Visual representation of detected dice faces
5. **comparison.png** - Side-by-side comparison (if generated)

## Example Output Format

```
============================================================
XÚC SẮC NHẬN DIỆN KẾT QUẢ
Dice Detection Results
============================================================

Thời gian / Time: 2026-01-05 14:30:45

Số lượng xúc sắc / Dice Count: 2

------------------------------------------------------------
CHI TIẾT / DETAILS:
------------------------------------------------------------

Xúc sắc 1 / Die 1:
  Số chấm / Pips: 3
  Độ tin cậy / Confidence: 0.9500
  Vị trí / Position: (100, 50, 250, 200)

Xúc sắc 2 / Die 2:
  Số chấm / Pips: 5
  Độ tin cậy / Confidence: 0.9200
  Vị trí / Position: (300, 50, 450, 200)

------------------------------------------------------------
TỔNG CỘNG / TOTAL PIPS: 8
------------------------------------------------------------
```

## Notes

- First run will download model weights (~100MB for yolov8m)
- GPU support requires CUDA-compatible hardware
- Press 'q' to quit webcam detection
- For best dice detection, use clear, well-lit images
- Each die should be clearly visible in the image

## References

- [YOLOv8 Documentation](https://docs.ultralytics.com/models/yolov8/)
- [YOLO GitHub](https://github.com/ultralytics/ultralytics)

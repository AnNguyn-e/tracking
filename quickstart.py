"""
Quick Start Guide for Dice Detection Project
Hướng dẫn bắt đầu nhanh cho Dự án Nhận diện Xúc sắc
"""

GUIDE = """
═══════════════════════════════════════════════════════════════════
🎲 XÚC SẮC NHẬN DIỆN - DICE DETECTION SYSTEM
Quick Start Guide / Hướng dẫn Bắt đầu
═══════════════════════════════════════════════════════════════════

📋 TABLE OF CONTENTS / MỤC LỤC
─────────────────────────────────────────────────────────────────

1. Installation / Cài đặt
2. Quick Usage / Cách sử dụng nhanh
3. GUI Application / Ứng dụng Giao diện
4. Command Line Usage / Sử dụng Dòng lệnh
5. Output Files / Tệp Kết quả
6. Troubleshooting / Xử lý sự cố


═══════════════════════════════════════════════════════════════════
1️⃣ INSTALLATION / CÀI ĐẶT
═══════════════════════════════════════════════════════════════════

First Time Setup:
  1. Make sure you have Python 3.8 or higher installed
  2. Open terminal and navigate to the project directory:
     
     cd d:\\CODE_TEST\\PBL5

  3. Install all dependencies:
     
     pip install -r requirements.txt

  4. First use will download the YOLOv8 model (~100MB)


═══════════════════════════════════════════════════════════════════
2️⃣ QUICK USAGE / CÁCH SỬ DỤNG NHANH
═══════════════════════════════════════════════════════════════════

🖥️ OPTION A: GUI Application (Recommended / Khuyến khích)
──────────────────────────────────────────────────────────

This is the easiest way! / Đây là cách dễ nhất!

Command:
  python gui_app.py

Steps / Bước:
  1. Click "Tải ảnh lên / Upload Image"
  2. Select your image with dice / Chọn ảnh có xúc sắc
  3. Click "Nhận diện / Detect Dice"
  4. Wait for results / Chờ kết quả
  5. View detected pips for each die / Xem số chấm mỗi xúc sắc
  6. Click "Lưu kết quả / Save Results" to export
  
Output:
  - Annotated image with bounding boxes / Ảnh có khung chữ nhật
  - Text file with results in Vietnamese/English
  - JSON file for data analysis / Tệp JSON để phân tích


🔧 OPTION B: Command Line / Dòng lệnh
──────────────────────────────────────

Quick demo:
  python demo.py --image ./data/sample.jpg

With custom output:
  python demo.py --image your_image.jpg --output ./my_results


📓 OPTION C: Jupyter Notebook / Sổ tay Jupyter
──────────────────────────────────────────────

For interactive analysis:
  
  Open notebook.ipynb in Jupyter
  Cell 4: Change model_size if needed
  Run cells sequentially
  Download and test with sample image
  Perform custom analysis


═══════════════════════════════════════════════════════════════════
3️⃣ GUI APPLICATION DETAILED / CHI TIẾT ỨNG DỤNG GIAO DIỆN
═══════════════════════════════════════════════════════════════════

Launch GUI:
  python gui_app.py

Screen Layout:
  
  ┌─────────────────────────────────────────────────────┐
  │          Nhận Diện Xúc Sắc - Dice Detection        │
  ├────────────────────────┬────────────────────────────┤
  │                        │   Điều khiển / Controls:   │
  │                        │  ┌──────────────────────┐  │
  │    IMAGE DISPLAY       │  │ 📁 Upload Image      │  │
  │    (Left Side)         │  │ 🎲 Detect Dice       │  │
  │                        │  │ 💾 Save Results      │  │
  │                        │  │ 🗑️  Clear             │  │
  │                        │  └──────────────────────┘  │
  │                        │                            │
  │                        │  Results Display:          │
  │                        │  ┌──────────────────────┐  │
  │                        │  │ Dice 1: 3 pips      │  │
  │                        │  │ Dice 2: 5 pips      │  │
  │                        │  │ Total: 8 pips       │  │
  │                        │  └──────────────────────┘  │
  └────────────────────────┴────────────────────────────┘

Buttons:
  
  1. 📁 Upload Image / Tải ảnh lên
     - Click to select image from device
     - Supported formats: JPG, PNG, BMP
     
  2. 🎲 Detect Dice / Nhận diện
     - Analyzes image to detect dice
     - Counts pips (1-6) on each die
     - Shows confidence scores
     
  3. 💾 Save Results / Lưu kết quả
     - Saves detection results to file
     - Creates annotated image
     - Exports data in multiple formats
     
  4. 🗑️  Clear / Xóa
     - Clears all current detections
     - Resets for new image


═══════════════════════════════════════════════════════════════════
4️⃣ COMMAND LINE USAGE / SỬ DỤNG DÒNG LỆNH
═══════════════════════════════════════════════════════════════════

Demo Script:
  
  Basic usage:
    python demo.py --image image.jpg
  
  Custom output directory:
    python demo.py --image image.jpg --output ./my_results


General Detection Script:
  
  Image detection:
    python detect.py --source image.jpg
  
  Video detection:
    python detect.py --source video.mp4
  
  Webcam detection (press 'q' to quit):
    python detect.py --source 0


Python API:
  
  from utils.dice_detector import DiceDetector
  from utils.visualizer import DiceVisualizer
  
  # Create detector
  detector = DiceDetector(conf_threshold=0.45)
  
  # Detect
  results = detector.detect_pips("image.jpg", visualize=True)
  
  # Save
  detector.save_results_to_file(results)
  
  # Visualize
  visualizer = DiceVisualizer()
  visualizer.visualize_dice_pips(results['dice'])


═══════════════════════════════════════════════════════════════════
5️⃣ OUTPUT FILES / TỆP KẾT QUẢ
═══════════════════════════════════════════════════════════════════

All results are saved in ./results/ directory

Files created:
  
  📄 dice_detection_results.txt
     - Human-readable format
     - Vietnamese and English labels
     - Easy to read in any text editor
     
  📊 dice_detection_results.json
     - Machine-readable format
     - Includes all detection details
     - For programmatic access
     
  🖼️  dice_detection_result.jpg
     - Original image with annotations
     - Red bounding boxes around dice
     - Pip counts labeled
     
  📈 dice_visualization.png
     - Visual diagram of detected dice
     - Shows all 6 faces representation
     - Nice for presentations

Example Text Output:
  
  ============================================================
  XÚC SẮC NHẬN DIỆN KẾT QUẢ
  Dice Detection Results
  ============================================================
  
  Thời gian / Time: 2026-01-05 14:30:45
  Số lượng xúc sắc / Dice Count: 2
  
  Xúc sắc 1 / Die 1:
    Số chấm / Pips: 3
    Độ tin cậy / Confidence: 0.9500
  
  Xúc sắc 2 / Die 2:
    Số chấm / Pips: 5
    Độ tin cậy / Confidence: 0.9200
  
  TỔNG CỘNG / TOTAL PIPS: 8


═══════════════════════════════════════════════════════════════════
6️⃣ TROUBLESHOOTING / XỬ LÝ SỰ CỐ
═══════════════════════════════════════════════════════════════════

Problem: Module not found error
─────────────────────────────────
  Solution:
    1. Check you're in correct directory: cd d:\\CODE_TEST\\PBL5
    2. Reinstall dependencies: pip install -r requirements.txt
    3. Try: pip install --upgrade pip setuptools wheel

Problem: No dice detected
──────────────────────────
  Solution:
    1. Ensure dice are clearly visible
    2. Good lighting is essential
    3. Make sure dice faces are not blurry
    4. Try adjusting confidence threshold in config.yaml
    5. Use detector.py instead (more general)

Problem: GUI won't start
───────────────────────
  Solution:
    1. Install tkinter: pip install tk
    2. Check Python version: python --version
    3. Run from administrator/sudo terminal
    4. Try demo.py instead: python demo.py

Problem: Slow detection
──────────────────────
  Solution:
    1. Use smaller model: change yolov8m to yolov8n in config.yaml
    2. Check GPU availability
    3. Reduce image resolution
    4. Close other applications

Problem: Out of memory error
────────────────────────────
  Solution:
    1. Use CPU instead: change device from 0 to 'cpu' in config.yaml
    2. Use smaller model: yolov8n
    3. Reduce image size before detection


═══════════════════════════════════════════════════════════════════
📚 ADDITIONAL RESOURCES / TÍNH NĂNG BỔ SUNG
═══════════════════════════════════════════════════════════════════

For more information:
  - YOLOv8 Docs: https://docs.ultralytics.com/
  - OpenCV Docs: https://docs.opencv.org/
  - Matplotlib: https://matplotlib.org/

Project Structure:
  PBL5/
  ├── gui_app.py              ← GUI Application
  ├── demo.py                 ← Demo Script
  ├── detect.py               ← General Detection
  ├── notebook.ipynb          ← Jupyter Notebook
  ├── config.yaml             ← Configuration
  ├── utils/
  │   ├── dice_detector.py    ← Dice Detection
  │   ├── visualizer.py       ← Visualization
  │   └── detector.py         ← General Detection
  └── results/                ← Output Files


═══════════════════════════════════════════════════════════════════
✅ READY TO GET STARTED! / SẴN SÀNG BẮT ĐẦU!
═══════════════════════════════════════════════════════════════════

Run this command to start:
  python gui_app.py

Or try the demo:
  python demo.py --image ./data/sample.jpg

Good luck! / Chúc bạn thành công!
"""

if __name__ == "__main__":
    print(GUIDE)
    
    # Save to file
    with open("QUICKSTART.txt", "w", encoding="utf-8") as f:
        f.write(GUIDE)
    
    print("\n✅ Quick start guide saved to QUICKSTART.txt")

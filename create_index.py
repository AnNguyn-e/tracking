"""
INDEX - Dice Detection System
Complete Project Structure and File Guide

Chỉ Mục - Hệ Thống Nhận Diện Xúc Sắc
Cấu Trúc Dự Án Hoàn Chỉnh và Hướng Dẫn Tệp
"""

import os
from pathlib import Path

def create_index():
    index_content = """
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║            🎲 DICE DETECTION SYSTEM - COMPLETE PROJECT INDEX              ║
║                                                                            ║
║              XÚC SẮC NHẬN DIỆN - CHỈ MỤC DỰ ÁN HOÀN CHỈNH                 ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝


📋 QUICK NAVIGATION
═════════════════════════════════════════════════════════════════════════════

🚀 START HERE:
   1. Read: PROJECT_COMPLETE.md          (Overview of everything)
   2. Run:  python test_setup.py         (Verify installation)
   3. Use:  python gui_app.py            (Launch application)

📖 DOCUMENTATION:
   • PROJECT_COMPLETE.md    - Project completion summary
   • SETUP_GUIDE.md        - Detailed setup and configuration
   • README.md             - Full project documentation
   • QUICKSTART.txt        - Quick start guide (run: python quickstart.py)


🎯 MAIN APPLICATIONS (Choose One)
═════════════════════════════════════════════════════════════════════════════

1. 🖥️  GUI APPLICATION (Recommended / Khuyến khích)
   ────────────────────────────────────────────────
   File: gui_app.py
   Command: python gui_app.py
   
   Features:
   ✓ User-friendly interface
   ✓ Image upload from device
   ✓ Real-time detection
   ✓ One-click export
   ✓ Bilingual interface
   
   Best for: General users, quick analysis

2. 💻 COMMAND LINE DEMO
   ───────────────────
   File: demo.py
   Command: python demo.py --image image.jpg
   
   Features:
   ✓ Quick detection from command line
   ✓ Custom output directory
   ✓ Console output
   
   Best for: Automated workflows, scripting

3. 🔍 GENERAL DETECTION
   ──────────────────
   File: detect.py
   Commands:
     python detect.py --source image.jpg
     python detect.py --source video.mp4
     python detect.py --source 0          (webcam)
   
   Features:
   ✓ Works on images, videos, webcam
   ✓ General object detection (not just dice)
   ✓ Configurable parameters
   
   Best for: General purpose detection

4. 📓 JUPYTER NOTEBOOK
   ──────────────────
   File: notebook.ipynb
   Command: jupyter notebook notebook.ipynb
   
   Features:
   ✓ Interactive exploration
   ✓ Step-by-step learning
   ✓ Customizable cells
   ✓ Visualization examples
   
   Best for: Learning, experimentation, education


🔧 UTILITY MODULES (Python API)
═════════════════════════════════════════════════════════════════════════════

Located in: utils/

1. utils/dice_detector.py
   ───────────────────
   Class: DiceDetector
   
   Usage:
     from utils.dice_detector import DiceDetector
     detector = DiceDetector()
     results = detector.detect_pips("image.jpg")
     detector.save_results_to_file(results)
   
   Methods:
   ✓ detect_pips()           - Main detection
   ✓ save_results_to_file()  - Export results
   ✓ _count_dice_pips()      - Count pips
   ✓ _create_visualization() - Generate image

2. utils/visualizer.py
   ──────────────────
   Class: DiceVisualizer
   
   Usage:
     from utils.visualizer import DiceVisualizer
     visualizer = DiceVisualizer()
     visualizer.visualize_dice_pips(dice_info_list)
   
   Methods:
   ✓ visualize_dice_pips()           - Draw dice diagrams
   ✓ create_comparison_visualization() - Before/after
   ✓ create_statistics_chart()       - Stats visualization
   ✓ draw_die_diagram()              - Single die drawing

3. utils/detector.py
   ────────────────
   Class: YOLOv8Detector
   
   Usage:
     from utils.detector import YOLOv8Detector
     detector = YOLOv8Detector()
     results = detector.detect_image("image.jpg")
   
   Methods:
   ✓ detect_image()   - Image detection
   ✓ detect_video()   - Video detection
   ✓ detect_webcam()  - Webcam detection


⚙️  HELPER SCRIPTS
═════════════════════════════════════════════════════════════════════════════

1. test_setup.py
   ────────────
   Purpose: Verify installation and dependencies
   Command: python test_setup.py
   
   Checks:
   ✓ Python packages installed
   ✓ Custom modules available
   ✓ Directory structure
   ✓ Required files present
   ✓ YOLOv8 model loading

2. quickstart.py
   ────────────
   Purpose: Display quick start guide
   Command: python quickstart.py
   
   Shows:
   ✓ Installation instructions
   ✓ Usage examples
   ✓ Output file descriptions
   ✓ Troubleshooting tips

3. launch.bat
   ──────────
   Purpose: Windows batch launcher
   Usage: Double-click launch.bat
   
   Features:
   ✓ Menu-driven interface
   ✓ Launch any application
   ✓ Run tests
   ✓ Bilingual support


📁 DIRECTORY STRUCTURE
═════════════════════════════════════════════════════════════════════════════

PBL5/
├── 🚀 APPLICATIONS
│   ├── gui_app.py ...................... GUI application (⭐ Start here)
│   ├── demo.py ......................... Demo script
│   ├── detect.py ....................... General detection
│   └── notebook.ipynb .................. Jupyter notebook
│
├── 🛠️  UTILITIES
│   └── utils/
│       ├── __init__.py
│       ├── detector.py ................. YOLOv8 detector
│       ├── dice_detector.py ............ Dice detection (⭐ New!)
│       └── visualizer.py .............. Visualization (⭐ New!)
│
├── ⚙️  CONFIGURATION
│   ├── config.yaml ..................... Settings
│   └── requirements.txt ................ Dependencies
│
├── 📖 DOCUMENTATION
│   ├── README.md ....................... Full documentation
│   ├── PROJECT_COMPLETE.md ............ Project summary
│   ├── SETUP_GUIDE.md ................. Setup guide
│   ├── QUICKSTART.txt (auto-generated)
│   └── INDEX.md (this file)
│
├── 🔧 HELPER SCRIPTS
│   ├── test_setup.py ................... Verification
│   ├── quickstart.py ................... Quick start
│   └── launch.bat (Windows) ............ Batch launcher
│
└── 📁 DATA DIRECTORIES
    ├── data/ ........................... Input images/videos
    ├── models/ ......................... Model weights
    ├── results/ ........................ Output files
    └── utils/ .......................... Python modules


📊 OUTPUT FILES
═════════════════════════════════════════════════════════════════════════════

When you detect dice, these files are saved to ./results/:

1. dice_detection_results.txt
   Purpose: Human-readable results
   Format: Text with Vietnamese/English labels
   Usage: Open with any text editor
   
   Contains:
   • Timestamp
   • Number of dice detected
   • Pip count for each die
   • Confidence scores
   • Total pips

2. dice_detection_results.json
   Purpose: Machine-readable format
   Format: JSON
   Usage: Parse with Python, import to spreadsheet
   
   Contains:
   • All results in structured format
   • Perfect for data analysis
   • Easy to process programmatically

3. dice_detection_result.jpg
   Purpose: Annotated image
   Format: JPEG image
   Contents:
   • Original image
   • Green bounding boxes
   • Pip count labels
   • Die numbers

4. dice_visualization.png
   Purpose: Visual dice diagrams
   Format: PNG image
   Contents:
   • Diagram of each detected die
   • Pip positions shown as circles
   • Professional appearance
   • Ready for presentations


⚡ QUICK COMMANDS
═════════════════════════════════════════════════════════════════════════════

Installation:
  pip install -r requirements.txt

Verification:
  python test_setup.py

Start GUI:
  python gui_app.py

Run Demo:
  python demo.py --image image.jpg

Windows Launcher:
  launch.bat

Jupyter Notebook:
  jupyter notebook notebook.ipynb

Show Quick Start:
  python quickstart.py


🎯 COMMON TASKS
═════════════════════════════════════════════════════════════════════════════

Task: Detect dice in an image
─────────────────────────────
1. Run: python gui_app.py
2. Click: Upload Image
3. Select: Image with dice
4. Click: Detect Dice
5. Save: Results


Task: Batch process multiple images
─────────────────────────────────
from pathlib import Path
from utils.dice_detector import DiceDetector

detector = DiceDetector()
for img_file in Path("data").glob("*.jpg"):
    results = detector.detect_pips(str(img_file))
    print(f"{img_file.name}: {results['total_pips']} total pips")


Task: Get results programmatically
──────────────────────────────────
from utils.dice_detector import DiceDetector

detector = DiceDetector()
results = detector.detect_pips("image.jpg")

for die in results['dice']:
    print(f"Die {die['die']}: {die['pips']} pips")

print(f"Total: {results['total_pips']}")


Task: Create custom visualization
──────────────────────────────────
from utils.visualizer import DiceVisualizer

visualizer = DiceVisualizer()
visualizer.visualize_dice_pips(
    results['dice'],
    save_path="my_custom_viz.png"
)


📚 DOCUMENTATION MAP
═════════════════════════════════════════════════════════════════════════════

Need help with...                    → See file
─────────────────────────────────────────────────
Getting started quickly?             → PROJECT_COMPLETE.md
Installation instructions?           → SETUP_GUIDE.md
Full documentation?                  → README.md
Quick reference?                     → QUICKSTART.txt (run: python quickstart.py)
Project structure?                   → This file (INDEX.md)
Code examples?                        → notebook.ipynb
API reference?                        → Docstrings in utils/*.py
Troubleshooting?                      → SETUP_GUIDE.md → Section 6


🔗 DEPENDENCIES
═════════════════════════════════════════════════════════════════════════════

Core Libraries:
  • ultralytics (YOLOv8)
  • torch (PyTorch)
  • torchvision
  • opencv-python (cv2)
  • numpy
  • pillow
  • matplotlib
  • pyyaml

See requirements.txt for exact versions


💡 TIPS & TRICKS
═════════════════════════════════════════════════════════════════════════════

✓ For fastest detection:      Change model to "yolov8n" in config.yaml
✓ For best accuracy:          Use "yolov8l" or "yolov8x" in config.yaml
✓ For CPU-only machines:      Set device: 'cpu' in config.yaml
✓ For better lighting:        Use well-lit images for best results
✓ For batch processing:       Use demo.py with a loop
✓ For custom training:        Use YOLOv8 training API
✓ For deployment:             Export model with ultralytics export
✓ For API access:             Use utils/dice_detector.py in your code


✅ VERIFICATION CHECKLIST
═════════════════════════════════════════════════════════════════════════════

After setup, verify everything works:

□ Run: python test_setup.py
  (All tests should pass)

□ Launch: python gui_app.py
  (GUI window should appear)

□ Upload: test image
  (Image should display)

□ Detect: click detect button
  (Results should appear)

□ Save: click save results
  (Files should be created in ./results/)

□ Verify: check ./results/ folder
  (Should contain results.txt, results.json, etc.)


🎉 YOU'RE ALL SET!
═════════════════════════════════════════════════════════════════════════════

Your Dice Detection System is ready to use!

Next steps:
  1. Read PROJECT_COMPLETE.md
  2. Run python test_setup.py
  3. Run python gui_app.py
  4. Upload an image with dice
  5. Click "Nhận diện / Detect Dice"
  6. View results and save to file

Enjoy! / Hãy tận hưởng!

═════════════════════════════════════════════════════════════════════════════

Questions? Check: SETUP_GUIDE.md → Troubleshooting
Want to learn? Check: notebook.ipynb
Need quick help? Run: python quickstart.py

═════════════════════════════════════════════════════════════════════════════

Built with ❤️ using YOLOv8 | Enhanced for Dice Detection | Bilingual Support

Last Updated: 2026-01-05
Version: 1.0 Complete
"""
    return index_content


def main():
    # Create INDEX.md
    index_content = create_index()
    
    with open("INDEX.md", "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print(index_content)
    print("\n✅ INDEX.md has been created!")


if __name__ == "__main__":
    main()

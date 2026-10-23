"""
Test Script - Verify all components are working
"""

import sys
from pathlib import Path
import importlib


def test_imports():
    """Test all required imports"""
    print("=" * 60)
    print("Testing Imports...")
    print("=" * 60 + "\n")
    
    required_packages = {
        'cv2': 'OpenCV',
        'numpy': 'NumPy',
        'PIL': 'Pillow',
        'matplotlib': 'Matplotlib',
        'ultralytics': 'Ultralytics',
        'tkinter': 'Tkinter',
        'yaml': 'PyYAML'
    }
    
    all_ok = True
    for package, name in required_packages.items():
        try:
            module = importlib.import_module(package)
            version = getattr(module, '__version__', 'unknown')
            print(f"✅ {name:20} - OK (v{version})")
        except ImportError:
            print(f"❌ {name:20} - MISSING")
            all_ok = False
    
    return all_ok


def test_modules():
    """Test custom modules"""
    print("\n" + "=" * 60)
    print("Testing Custom Modules...")
    print("=" * 60 + "\n")
    
    modules = {
        'utils.detector': 'YOLOv8 Detector',
        'utils.dice_detector': 'Dice Detector',
        'utils.visualizer': 'Visualizer'
    }
    
    all_ok = True
    for module_name, description in modules.items():
        try:
            module = importlib.import_module(module_name)
            print(f"✅ {description:25} - OK")
        except ImportError as e:
            print(f"❌ {description:25} - ERROR: {e}")
            all_ok = False
    
    return all_ok


def test_directories():
    """Test directory structure"""
    print("\n" + "=" * 60)
    print("Testing Directory Structure...")
    print("=" * 60 + "\n")
    
    required_dirs = [
        'data',
        'models',
        'results',
        'utils'
    ]
    
    all_ok = True
    for dir_name in required_dirs:
        dir_path = Path(dir_name)
        if dir_path.exists() and dir_path.is_dir():
            print(f"✅ {dir_name:20} - EXISTS")
        else:
            print(f"❌ {dir_name:20} - MISSING")
            all_ok = False
    
    return all_ok


def test_files():
    """Test required files"""
    print("\n" + "=" * 60)
    print("Testing Required Files...")
    print("=" * 60 + "\n")
    
    required_files = {
        'gui_app.py': 'GUI Application',
        'demo.py': 'Demo Script',
        'detect.py': 'Detection Script',
        'config.yaml': 'Configuration',
        'requirements.txt': 'Requirements',
        'README.md': 'Documentation',
        'notebook.ipynb': 'Jupyter Notebook'
    }
    
    all_ok = True
    for file_name, description in required_files.items():
        file_path = Path(file_name)
        if file_path.exists() and file_path.is_file():
            size = file_path.stat().st_size
            print(f"✅ {description:25} - OK ({size} bytes)")
        else:
            print(f"❌ {description:25} - MISSING")
            all_ok = False
    
    return all_ok


def test_model():
    """Test YOLOv8 model availability"""
    print("\n" + "=" * 60)
    print("Testing YOLOv8 Model...")
    print("=" * 60 + "\n")
    
    try:
        from ultralytics import YOLO
        print("⏳ Loading YOLOv8 model (this may take a moment)...")
        
        # Try to load model (will download if not present)
        model = YOLO("yolov8n.pt")
        print(f"✅ YOLOv8 Model        - LOADED")
        print(f"   Model info: {model.info()}")
        return True
    except Exception as e:
        print(f"❌ YOLOv8 Model        - ERROR: {e}")
        return False


def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "DICE DETECTION PROJECT - TEST SUITE" + " " * 14 + "║")
    print("╚" + "=" * 58 + "╝")
    
    results = {
        'Imports': test_imports(),
        'Custom Modules': test_modules(),
        'Directory Structure': test_directories(),
        'Required Files': test_files(),
        'YOLOv8 Model': test_model()
    }
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60 + "\n")
    
    for test_name, result in results.items():
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:30} {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ ALL TESTS PASSED - READY TO USE!")
        print("\n🎲 Start using:")
        print("   python gui_app.py          (GUI Application)")
        print("   python demo.py --image img.jpg  (Demo)")
        print("   python detect.py           (General Detection)")
        print("   python quickstart.py       (Quick Start Guide)")
    else:
        print("❌ SOME TESTS FAILED - PLEASE FIX ISSUES ABOVE")
        print("\nTroubleshooting:")
        print("  1. Reinstall requirements: pip install -r requirements.txt")
        print("  2. Check Python version: python --version (need 3.8+)")
        print("  3. Check internet connection (for downloading YOLOv8 model)")
    
    print("=" * 60 + "\n")
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())

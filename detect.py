"""
YOLOv8 Object Detection Script
"""

import argparse
import yaml
from pathlib import Path
from utils.detector import YOLOv8Detector


def load_config(config_path="config.yaml"):
    """Load configuration from YAML file"""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


def main():
    parser = argparse.ArgumentParser(description="YOLOv8 Object Detection")
    parser.add_argument("--config", type=str, default="config.yaml", help="Config file path")
    parser.add_argument("--model", type=str, default="yolov8m", help="Model size")
    parser.add_argument("--source", type=str, help="Input source (image, video, or webcam)")
    parser.add_argument("--conf", type=float, default=0.45, help="Confidence threshold")
    parser.add_argument("--save", type=str, help="Save output path")
    
    args = parser.parse_args()
    
    # Load config if exists
    if Path(args.config).exists():
        config = load_config(args.config)
        model_name = config['model'].get('name', args.model)
        device = config['model'].get('device', 0)
        conf = config['detection'].get('confidence_threshold', args.conf)
        source = args.source or config['input'].get('source', 0)
        save_path = args.save or None
    else:
        model_name = args.model
        device = 0
        conf = args.conf
        source = args.source or 0
        save_path = args.save
    
    print(f"Model: {model_name}")
    print(f"Confidence Threshold: {conf}")
    print(f"Source: {source}")
    
    # Initialize detector
    detector = YOLOv8Detector(model_name=model_name, device=device, conf_threshold=conf)
    
    # Detect based on source type
    source_path = Path(str(source))
    
    if isinstance(source, int):
        print("Starting webcam detection... (Press 'q' to quit)")
        detector.detect_webcam(save_path=save_path)
    elif str(source).lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        print(f"Detecting objects in image: {source}")
        results = detector.detect_image(source, save_path=save_path)
        print(f"Detection complete. Saved to: {save_path}")
    elif str(source).lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        print(f"Detecting objects in video: {source}")
        detector.detect_video(source, save_path=save_path)
    else:
        print("Unsupported source type. Use image, video, or webcam (0)")


if __name__ == "__main__":
    main()

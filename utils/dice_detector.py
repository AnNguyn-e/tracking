"""
Dice Detection Module
Detects dice and their pip numbers
"""

import cv2
import numpy as np
from pathlib import Path
from ultralytics import YOLO
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import time
from datetime import datetime


class DiceDetector:
    """Detect dice and extract pip numbers"""
    
    def __init__(self, model_path="yolov8m.pt", conf_threshold=0.45):
        """
        Initialize dice detector
        
        Args:
            model_path: Path to YOLOv8 model
            conf_threshold: Confidence threshold
        """
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.dice_pips = {}  # Store detected pips for each die
        
    def detect_pips(self, image, visualize=True, output_dir="./results"):
        """
        Detect dice and count pips
        
        Args:
            image: Input image (path or numpy array)
            visualize: Whether to create visualization
            output_dir: Directory to save results
            
        Returns:
            Dictionary with detection results
        """
        Path(output_dir).mkdir(exist_ok=True)
        
        # Load image if path
        if isinstance(image, str):
            img = cv2.imread(image)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            img = image
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) if len(img.shape) == 3 else img
        
        # Run YOLO detection
        results = self.model(img, conf=self.conf_threshold, verbose=False)
        result = results[0]
        
        # Extract dice regions
        dice_regions = []
        detections = []
        
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            conf = float(box.conf)
            class_name = self.model.names[int(box.cls)]
            
            dice_regions.append({
                'coords': (x1, y1, x2, y2),
                'confidence': conf,
                'class': class_name
            })
            
            detections.append({
                'class': class_name,
                'confidence': f"{conf:.4f}",
                'x1': x1,
                'y1': y1,
                'x2': x2,
                'y2': y2
            })
        
        # Count pips for each detected dice
        pips_results = self._count_dice_pips(img_rgb, dice_regions)
        
        # Create visualization
        if visualize:
            viz_img = self._create_visualization(
                img_rgb, dice_regions, pips_results, output_dir
            )
        
        # Prepare results
        total_pips = sum([p['pips'] for p in pips_results])
        
        results_dict = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'dice_count': len(dice_regions),
            'dice': pips_results,
            'total_pips': total_pips,
            'raw_detections': detections
        }
        
        return results_dict
    
    def _count_dice_pips(self, image, dice_regions):
        """
        Count pips in each detected dice
        
        Args:
            image: RGB image
            dice_regions: List of dice bounding boxes
            
        Returns:
            List of pip counts
        """
        pips_results = []
        
        for idx, region in enumerate(dice_regions, 1):
            x1, y1, x2, y2 = region['coords']
            
            # Extract dice region
            dice_img = image[y1:y2, x1:x2]
            
            # Convert to grayscale
            if len(dice_img.shape) == 3:
                gray = cv2.cvtColor(dice_img, cv2.COLOR_RGB2GRAY)
            else:
                gray = dice_img
            
            # Count white/light pips (circles)
            # Apply threshold to find pips
            _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
            
            # Find contours (pips)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Filter contours by area (pips should have similar size)
            pip_count = 0
            if len(contours) > 0:
                areas = [cv2.contourArea(c) for c in contours]
                avg_area = np.mean(areas) if areas else 0
                
                # Count contours with reasonable area (not noise)
                for contour in contours:
                    area = cv2.contourArea(contour)
                    if area > avg_area * 0.5 and area < avg_area * 2.5:
                        pip_count += 1
            
            # If detection failed, use alternative method (simple counting)
            if pip_count == 0:
                pip_count = self._count_pips_alternative(dice_img)
            
            # Ensure pip count is between 1 and 6
            pip_count = max(1, min(6, pip_count))
            
            pips_results.append({
                'die': idx,
                'pips': pip_count,
                'confidence': region['confidence'],
                'bbox': region['coords']
            })
        
        return pips_results
    
    def _count_pips_alternative(self, dice_img):
        """
        Alternative method to count pips using brightness
        """
        if len(dice_img.shape) == 3:
            gray = cv2.cvtColor(dice_img, cv2.COLOR_RGB2GRAY)
        else:
            gray = dice_img
        
        # Count bright pixels (pips)
        bright_pixels = np.sum(gray > 200)
        total_pixels = gray.shape[0] * gray.shape[1]
        
        # Estimate pip count from ratio
        ratio = bright_pixels / total_pixels
        
        if ratio < 0.15:
            return 1
        elif ratio < 0.25:
            return 2
        elif ratio < 0.35:
            return 3
        elif ratio < 0.45:
            return 4
        elif ratio < 0.55:
            return 5
        else:
            return 6
    
    def _create_visualization(self, image, dice_regions, pips_results, output_dir):
        """
        Create visualization with bounding boxes and pip counts
        """
        img_copy = image.copy()
        
        # Draw bounding boxes and pip numbers
        for region_idx, (region, pips_info) in enumerate(zip(dice_regions, pips_results)):
            x1, y1, x2, y2 = region['coords']
            
            # Draw rectangle
            cv2.rectangle(img_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Draw pip count
            pip_text = f"Pips: {pips_info['pips']}"
            cv2.putText(
                img_copy, pip_text, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
            )
            
            # Draw die number
            die_text = f"Die {pips_info['die']}"
            cv2.putText(
                img_copy, die_text, (x1, y2 + 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2
            )
        
        # Save visualization
        output_path = Path(output_dir) / "dice_detection_result.jpg"
        cv2.imwrite(str(output_path), cv2.cvtColor(img_copy, cv2.COLOR_RGB2BGR))
        
        return img_copy
    
    def save_results_to_file(self, results, output_dir="./results"):
        """
        Save detection results to text file
        
        Args:
            results: Detection results dictionary
            output_dir: Directory to save results
        """
        Path(output_dir).mkdir(exist_ok=True)
        
        output_path = Path(output_dir) / "dice_detection_results.txt"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("XÚC SẮC NHẬN DIỆN KẾT QUẢ\n")
            f.write("Dice Detection Results\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"Thời gian / Time: {results['timestamp']}\n")
            f.write(f"Số lượng xúc sắc / Dice Count: {results['dice_count']}\n\n")
            
            f.write("-" * 60 + "\n")
            f.write("CHI TIẾT / DETAILS:\n")
            f.write("-" * 60 + "\n\n")
            
            for die_info in results['dice']:
                f.write(f"Xúc sắc {die_info['die']} / Die {die_info['die']}:\n")
                f.write(f"  Số chấm / Pips: {die_info['pips']}\n")
                f.write(f"  Độ tin cậy / Confidence: {die_info['confidence']:.4f}\n")
                f.write(f"  Vị trí / Position: {die_info['bbox']}\n\n")
            
            f.write("-" * 60 + "\n")
            f.write(f"TỔNG CỘNG / TOTAL PIPS: {results['total_pips']}\n")
            f.write("-" * 60 + "\n\n")
            
            f.write("CHÚ THÍCH / NOTES:\n")
            f.write("- Mỗi xúc sắc có 6 mặt (1-6 chấm)\n")
            f.write("- Each die has 6 faces (1-6 pips)\n")
            f.write("- Tổng có thể từ 2 đến 12\n")
            f.write("- Total ranges from 2 to 12\n")
        
        return str(output_path)

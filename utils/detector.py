"""
YOLOv8 Object Detection Module
"""

from ultralytics import YOLO
import cv2
import numpy as np
from pathlib import Path


class YOLOv8Detector:
    def __init__(self, model_name="yolov8m", device=0, conf_threshold=0.45):
        """
        Initialize YOLOv8 detector
        
        Args:
            model_name: Model size (yolov8n, yolov8s, yolov8m, yolov8l, yolov8x)
            device: GPU device ID or 'cpu'
            conf_threshold: Confidence threshold for detections
        """
        self.model = YOLO(f"{model_name}.pt")
        self.device = device
        self.conf_threshold = conf_threshold
        
    def detect_image(self, image_path, save_path=None):
        """
        Detect objects in an image
        
        Args:
            image_path: Path to input image
            save_path: Path to save annotated image
            
        Returns:
            Results object from YOLO
        """
        results = self.model(image_path, conf=self.conf_threshold, device=self.device)
        
        if save_path:
            for r in results:
                im_array = r.plot()
                cv2.imwrite(save_path, im_array)
        
        return results
    
    def detect_video(self, video_path, save_path=None, display=True):
        """
        Detect objects in a video
        
        Args:
            video_path: Path to input video
            save_path: Path to save annotated video
            display: Display video while processing
        """
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        if save_path:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(save_path, fourcc, fps, (width, height))
        
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            results = self.model(frame, conf=self.conf_threshold, device=self.device)
            annotated_frame = results[0].plot()
            
            if save_path:
                out.write(annotated_frame)
            
            if display:
                cv2.imshow('YOLOv8 Detection', annotated_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
            frame_count += 1
            if frame_count % 30 == 0:
                print(f"Processed {frame_count} frames")
        
        cap.release()
        if save_path:
            out.release()
        if display:
            cv2.destroyAllWindows()
    
    def detect_webcam(self, save_path=None, display=True, duration=None):
        """
        Real-time detection from webcam
        
        Args:
            save_path: Path to save video
            display: Display detection live
            duration: Duration in seconds (None for continuous)
        """
        cap = cv2.VideoCapture(0)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        if save_path:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(save_path, fourcc, fps, (width, height))
        
        frame_count = 0
        import time
        start_time = time.time()
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            results = self.model(frame, conf=self.conf_threshold, device=self.device)
            annotated_frame = results[0].plot()
            
            if save_path:
                out.write(annotated_frame)
            
            if display:
                cv2.imshow('YOLOv8 Webcam Detection', annotated_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
            frame_count += 1
            
            if duration and (time.time() - start_time) > duration:
                break
        
        cap.release()
        if save_path:
            out.release()
        if display:
            cv2.destroyAllWindows()
        
        print(f"Total frames captured: {frame_count}")

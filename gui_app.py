"""
GUI Application for Dice Detection
Allows uploading images and detecting dice pips
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import cv2
import numpy as np
from pathlib import Path
import threading
import json
from datetime import datetime

from utils.dice_detector import DiceDetector


class DiceDetectionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nhận Diện Xúc Sắc - Dice Detection System")
        self.root.geometry("1200x800")
        self.root.resizable(True, True)
        
        # Initialize detector
        self.detector = DiceDetector(conf_threshold=0.45)
        self.current_image = None
        self.current_results = None
        
        # Create GUI
        self.create_widgets()
        
    def create_widgets(self):
        """Create GUI widgets"""
        
        # Main container
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left side - Image display
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Image label
        tk.Label(left_frame, text="Ảnh / Image", font=("Arial", 12, "bold")).pack()
        
        self.image_label = tk.Label(left_frame, bg="gray", width=400, height=400)
        self.image_label.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Right side - Controls and results
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        # Control panel
        control_frame = tk.LabelFrame(right_frame, text="Điều khiển / Controls", padx=10, pady=10)
        control_frame.pack(fill=tk.X, pady=5)
        
        # Upload button
        self.upload_btn = tk.Button(
            control_frame,
            text="Tải ảnh lên / Upload Image",
            command=self.upload_image,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=8
        )
        self.upload_btn.pack(fill=tk.X, pady=5)
        
        # Detect button
        self.detect_btn = tk.Button(
            control_frame,
            text="Nhận diện / Detect Dice",
            command=self.detect_dice,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=8,
            state=tk.DISABLED
        )
        self.detect_btn.pack(fill=tk.X, pady=5)
        
        # Save results button
        self.save_btn = tk.Button(
            control_frame,
            text="Lưu kết quả / Save Results",
            command=self.save_results,
            bg="#FF9800",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=8,
            state=tk.DISABLED
        )
        self.save_btn.pack(fill=tk.X, pady=5)
        
        # Clear button
        self.clear_btn = tk.Button(
            control_frame,
            text="Xóa / Clear",
            command=self.clear_all,
            bg="#f44336",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=8
        )
        self.clear_btn.pack(fill=tk.X, pady=5)
        
        # Results panel
        results_frame = tk.LabelFrame(right_frame, text="Kết quả / Results", padx=10, pady=10)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Results text area
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            height=15,
            width=40,
            font=("Arial", 9),
            state=tk.DISABLED
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar(value="Sẵn sàng / Ready")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg="#e0e0e0",
            font=("Arial", 9)
        )
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
    
    def upload_image(self):
        """Upload image from file"""
        file_path = filedialog.askopenfilename(
            title="Chọn ảnh / Select Image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.current_image = cv2.imread(file_path)
            if self.current_image is not None:
                self.display_image(file_path)
                self.detect_btn.config(state=tk.NORMAL)
                self.status_var.set(f"Ảnh đã tải / Image loaded: {Path(file_path).name}")
            else:
                messagebox.showerror("Lỗi / Error", "Không thể đọc ảnh / Cannot read image")
    
    def display_image(self, image_path):
        """Display image in GUI"""
        # Load and resize image
        img = Image.open(image_path)
        img.thumbnail((400, 400), Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage
        photo = ImageTk.PhotoImage(img)
        
        # Update label
        self.image_label.config(image=photo)
        self.image_label.image = photo
    
    def detect_dice(self):
        """Run dice detection"""
        if self.current_image is None:
            messagebox.showwarning("Cảnh báo / Warning", "Vui lòng tải ảnh / Please upload an image")
            return
        
        # Show status
        self.status_var.set("Đang xử lý... / Processing...")
        self.root.update()
        
        # Run detection in thread
        thread = threading.Thread(target=self._detect_thread)
        thread.start()
    
    def _detect_thread(self):
        """Detection thread"""
        try:
            results = self.detector.detect_pips(
                self.current_image,
                visualize=True,
                output_dir="./results"
            )
            
            self.current_results = results
            
            # Update results display
            self.display_results(results)
            
            # Display result image
            result_img_path = "./results/dice_detection_result.jpg"
            self.display_image(result_img_path)
            
            self.save_btn.config(state=tk.NORMAL)
            self.status_var.set(f"Hoàn thành / Completed - Tổng chấm: {results['total_pips']}")
            
        except Exception as e:
            self.status_var.set(f"Lỗi / Error: {str(e)}")
            messagebox.showerror("Lỗi / Error", f"Lỗi nhận diện / Detection error: {str(e)}")
    
    def display_results(self, results):
        """Display detection results"""
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        
        text_content = "=" * 40 + "\n"
        text_content += "KẾT QUẢ NHẬN DIỆN\n"
        text_content += "Detection Results\n"
        text_content += "=" * 40 + "\n\n"
        
        text_content += f"Thời gian / Time:\n{results['timestamp']}\n\n"
        text_content += f"Số xúc sắc / Dice Count:\n{results['dice_count']}\n\n"
        
        text_content += "-" * 40 + "\n"
        text_content += "CHI TIẾT / DETAILS:\n"
        text_content += "-" * 40 + "\n\n"
        
        for die_info in results['dice']:
            text_content += f"Xúc sắc {die_info['die']} / Die {die_info['die']}:\n"
            text_content += f"  Chấm / Pips: {die_info['pips']}\n"
            text_content += f"  Độ tin cậy / Conf: {die_info['confidence']:.4f}\n\n"
        
        text_content += "-" * 40 + "\n"
        text_content += f"TỔNG CỘNG / TOTAL:\n{results['total_pips']}\n"
        text_content += "-" * 40 + "\n"
        
        self.results_text.insert(tk.END, text_content)
        self.results_text.config(state=tk.DISABLED)
    
    def save_results(self):
        """Save results to file"""
        if self.current_results is None:
            messagebox.showwarning("Cảnh báo / Warning", "Không có kết quả để lưu / No results to save")
            return
        
        try:
            # Save text results
            text_path = self.detector.save_results_to_file(
                self.current_results,
                output_dir="./results"
            )
            
            # Also save JSON
            json_path = "./results/dice_detection_results.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                # Convert datetime to string for JSON serialization
                results_copy = self.current_results.copy()
                results_copy['timestamp'] = str(results_copy['timestamp'])
                json.dump(results_copy, f, indent=2, ensure_ascii=False)
            
            messagebox.showinfo(
                "Thành công / Success",
                f"Kết quả đã được lưu tại / Results saved to:\n"
                f"{text_path}\n"
                f"{json_path}"
            )
            
            self.status_var.set("Đã lưu kết quả / Results saved")
            
        except Exception as e:
            messagebox.showerror("Lỗi / Error", f"Lỗi lưu kết quả / Error saving results: {str(e)}")
    
    def clear_all(self):
        """Clear all"""
        self.current_image = None
        self.current_results = None
        self.image_label.config(image='')
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state=tk.DISABLED)
        self.detect_btn.config(state=tk.DISABLED)
        self.save_btn.config(state=tk.DISABLED)
        self.status_var.set("Sẵn sàng / Ready")


def main():
    """Main function"""
    root = tk.Tk()
    app = DiceDetectionGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

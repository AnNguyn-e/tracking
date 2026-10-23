"""
Visualization Module for Dice Detection
Creates visual representations using matplotlib
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.patches import Circle, Rectangle, Wedge
import cv2
from pathlib import Path


class DiceVisualizer:
    """Create visualizations for dice detection results"""
    
    @staticmethod
    def visualize_dice_pips(dice_info_list, figsize=(12, 5), save_path="./results/dice_visualization.png"):
        """
        Create visualization showing dice pip numbers
        
        Args:
            dice_info_list: List of dice information
            figsize: Figure size
            save_path: Path to save visualization
        """
        Path(save_path).parent.mkdir(exist_ok=True)
        
        fig, axes = plt.subplots(1, len(dice_info_list), figsize=figsize)
        
        # Handle single dice
        if len(dice_info_list) == 1:
            axes = [axes]
        
        for idx, (ax, dice_info) in enumerate(zip(axes, dice_info_list)):
            pips = dice_info['pips']
            die_num = dice_info['die']
            
            # Draw die face
            ax.set_xlim(0, 3)
            ax.set_ylim(0, 3)
            ax.set_aspect('equal')
            ax.invert_yaxis()
            
            # Draw border
            rect = Rectangle((0.2, 0.2), 2.6, 2.6, linewidth=3, edgecolor='black', facecolor='white')
            ax.add_patch(rect)
            
            # Draw pips
            DiceVisualizer._draw_die_pips(ax, pips)
            
            # Title
            ax.set_title(f"Die {die_num}\n({pips} pips)", fontsize=14, fontweight='bold')
            ax.axis('off')
        
        plt.suptitle("Dice Detection Results", fontsize=16, fontweight='bold', y=1.02)
        plt.tight_layout()
        plt.savefig(save_path, dpi=100, bbox_inches='tight')
        plt.close()
        
        return save_path
    
    @staticmethod
    def _draw_die_pips(ax, num_pips):
        """
        Draw pips on a die face
        
        Args:
            ax: Matplotlib axis
            num_pips: Number of pips (1-6)
        """
        pip_radius = 0.15
        
        # Pip positions for each number
        positions = {
            1: [(1.5, 1.5)],
            2: [(0.8, 0.8), (2.2, 2.2)],
            3: [(0.8, 0.8), (1.5, 1.5), (2.2, 2.2)],
            4: [(0.8, 0.8), (0.8, 2.2), (2.2, 0.8), (2.2, 2.2)],
            5: [(0.8, 0.8), (0.8, 2.2), (1.5, 1.5), (2.2, 0.8), (2.2, 2.2)],
            6: [(0.8, 0.8), (0.8, 1.5), (0.8, 2.2), (2.2, 0.8), (2.2, 1.5), (2.2, 2.2)]
        }
        
        # Draw circles for pips
        for x, y in positions.get(num_pips, []):
            circle = Circle((x, y), pip_radius, color='black')
            ax.add_patch(circle)
    
    @staticmethod
    def create_comparison_visualization(original_img, result_img, dice_info, 
                                       save_path="./results/comparison.png"):
        """
        Create side-by-side comparison of original and detected
        
        Args:
            original_img: Original image (numpy array or path)
            result_img: Result image with bounding boxes
            dice_info: Dice information list
            save_path: Path to save
        """
        Path(save_path).parent.mkdir(exist_ok=True)
        
        # Load images if paths
        if isinstance(original_img, str):
            orig = cv2.imread(original_img)
            orig = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
        else:
            orig = original_img
        
        if isinstance(result_img, str):
            result = cv2.imread(result_img)
            result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        else:
            result = result_img
        
        # Create figure
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # Original image
        axes[0].imshow(orig)
        axes[0].set_title("Original Image", fontsize=12, fontweight='bold')
        axes[0].axis('off')
        
        # Result image
        axes[1].imshow(result)
        axes[1].set_title("Detection Result", fontsize=12, fontweight='bold')
        axes[1].axis('off')
        
        # Add info text
        info_text = f"Total Pips: {sum([d['pips'] for d in dice_info])}\nDice Count: {len(dice_info)}"
        fig.text(0.5, 0.02, info_text, ha='center', fontsize=12, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=100, bbox_inches='tight')
        plt.close()
        
        return save_path
    
    @staticmethod
    def create_statistics_chart(results_list, save_path="./results/statistics.png"):
        """
        Create statistics chart from multiple detections
        
        Args:
            results_list: List of detection results
            save_path: Path to save
        """
        Path(save_path).parent.mkdir(exist_ok=True)
        
        # Extract pip counts
        all_pips = []
        totals = []
        
        for results in results_list:
            for die in results['dice']:
                all_pips.append(die['pips'])
            totals.append(results['total_pips'])
        
        # Create figure with subplots
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # Histogram of individual die pips
        if all_pips:
            axes[0].hist(all_pips, bins=range(1, 8), edgecolor='black', color='skyblue')
            axes[0].set_xlabel("Number of Pips", fontsize=11)
            axes[0].set_ylabel("Frequency", fontsize=11)
            axes[0].set_title("Distribution of Individual Die Pips", fontsize=12, fontweight='bold')
            axes[0].set_xticks(range(1, 7))
            axes[0].grid(axis='y', alpha=0.3)
        
        # Total pips over time
        if totals:
            axes[1].plot(range(1, len(totals) + 1), totals, 'o-', linewidth=2, markersize=8, color='green')
            axes[1].set_xlabel("Detection #", fontsize=11)
            axes[1].set_ylabel("Total Pips", fontsize=11)
            axes[1].set_title("Total Pips Per Detection", fontsize=12, fontweight='bold')
            axes[1].set_ylim(1, 13)
            axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=100, bbox_inches='tight')
        plt.close()
        
        return save_path
    
    @staticmethod
    def draw_die_diagram(num_pips, figsize=(4, 4), save_path=None):
        """
        Draw a single die diagram
        
        Args:
            num_pips: Number of pips (1-6)
            figsize: Figure size
            save_path: Path to save (optional)
            
        Returns:
            Path to saved image or None
        """
        fig, ax = plt.subplots(1, 1, figsize=figsize)
        
        # Set up
        ax.set_xlim(0, 3)
        ax.set_ylim(0, 3)
        ax.set_aspect('equal')
        ax.invert_yaxis()
        
        # Draw die face
        rect = Rectangle((0.2, 0.2), 2.6, 2.6, linewidth=4, edgecolor='darkred', facecolor='lightyellow')
        ax.add_patch(rect)
        
        # Draw pips
        DiceVisualizer._draw_die_pips(ax, num_pips)
        
        # Title
        ax.set_title(f"Die Face: {num_pips} Pips", fontsize=16, fontweight='bold', pad=20)
        ax.axis('off')
        
        if save_path:
            Path(save_path).parent.mkdir(exist_ok=True)
            plt.savefig(save_path, dpi=100, bbox_inches='tight', facecolor='white')
            plt.close()
            return save_path
        else:
            plt.show()
            return None


if __name__ == "__main__":
    # Test visualization
    visualizer = DiceVisualizer()
    
    # Test data
    dice_info = [
        {'die': 1, 'pips': 3, 'confidence': 0.95},
        {'die': 2, 'pips': 5, 'confidence': 0.92}
    ]
    
    # Create visualizations
    print("Creating dice visualization...")
    visualizer.visualize_dice_pips(dice_info, save_path="./results/test_dice_viz.png")
    
    print("Visualization saved!")

"""
Demo Script for Dice Detection
Shows how to use the dice detector and visualizer
"""

import sys
from pathlib import Path
from utils.dice_detector import DiceDetector
from utils.visualizer import DiceVisualizer
import cv2
import argparse


def main():
    parser = argparse.ArgumentParser(description="Dice Detection Demo")
    parser.add_argument("--image", type=str, help="Path to image with dice")
    parser.add_argument("--output", type=str, default="./results", help="Output directory")
    
    args = parser.parse_args()
    
    # Create output directory
    Path(args.output).mkdir(exist_ok=True)
    
    if args.image is None:
        print("=" * 60)
        print("XÚC SẮC NHẬN DIỆN - DEMO")
        print("Dice Detection Demo")
        print("=" * 60)
        print("\nUsage:")
        print("  python demo.py --image <path_to_image> [--output <output_dir>]")
        print("\nExample:")
        print("  python demo.py --image ./data/dice.jpg")
        print("\nOr use the GUI:")
        print("  python gui_app.py")
        return
    
    print("=" * 60)
    print("XÚC SẮC NHẬN DIỆN - DEMO")
    print("Dice Detection Demo")
    print("=" * 60)
    print(f"\nImage: {args.image}")
    print(f"Output: {args.output}")
    
    # Check if image exists
    if not Path(args.image).exists():
        print(f"Error: Image not found at {args.image}")
        return
    
    # Initialize detector and visualizer
    print("\nInitializing detector...")
    detector = DiceDetector(conf_threshold=0.45)
    visualizer = DiceVisualizer()
    
    # Detect dice
    print("Running detection...")
    results = detector.detect_pips(
        args.image,
        visualize=True,
        output_dir=args.output
    )
    
    # Display results
    print("\n" + "=" * 60)
    print("DETECTION RESULTS / KẾT QUẢ NHẬN DIỆN")
    print("=" * 60)
    
    print(f"\nTimestamp: {results['timestamp']}")
    print(f"Dice Count: {results['dice_count']}")
    print(f"Total Pips: {results['total_pips']}\n")
    
    for die_info in results['dice']:
        print(f"Die {die_info['die']}:")
        print(f"  Pips: {die_info['pips']}")
        print(f"  Confidence: {die_info['confidence']:.4f}")
        print(f"  Position: {die_info['bbox']}\n")
    
    # Save results
    print("Saving results...")
    text_file = detector.save_results_to_file(results, output_dir=args.output)
    print(f"Text results saved to: {text_file}")
    
    # Create visualizations
    print("Creating visualizations...")
    viz_file = visualizer.visualize_dice_pips(
        results['dice'],
        save_path=f"{args.output}/dice_visualization.png"
    )
    print(f"Visualization saved to: {viz_file}")
    
    # Load and display result image
    result_img = cv2.imread(f"{args.output}/dice_detection_result.jpg")
    if result_img is not None:
        print(f"Annotated image saved to: {args.output}/dice_detection_result.jpg")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)
    print(f"\nOutput files in: {args.output}/")
    print("  - dice_detection_results.txt")
    print("  - dice_detection_results.json")
    print("  - dice_detection_result.jpg")
    print("  - dice_visualization.png")


if __name__ == "__main__":
    main()

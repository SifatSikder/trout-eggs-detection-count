# Trout Egg Detection and Counting

## Task

Given a single image: a set of trout eggs placed on a white tray, alongside a coin and a ruler for reference, my goal is to detect and count all the eggs in the image

## Overview

The image features a uniform background and lighting, but slight variations in BGR values occur due to shadows and reflections. To handle these variations, I converted the image to the HSV color space, making it easier to segment based on the eggs' orange hue.

## Solution Process

The segmentation result served as a mask for the eggs. Initially, a simple contour detection on the mask merged overlapping eggs into large blobs, so I needed a better strategy. Here's how I solved it:

1. **Distance Transform:**  
   I applied a distance transform to locate the centers of the eggs, even when they overlapped.

2. **Thresholding:**  
   Once I detected the centers, I applied thresholding to mark each egg’s center in white while keeping the rest of the image black. After tuning the hyper parameters, I settled on a threshold value of 0.28.

3. **Morphological Operations:**  
   The resulting thresholded image had distortions, so I used a series of morphological operations to refine the segmentation. I finalized the exact sequence after extensive experimentation.

4. **Watershed Segmentation:**  
   With clearly defined centers, I used them as markers for the watershed algorithm. The algorithm helped separate overlapping objects by “flooding” regions based on distance information. The resulting markers array contained:

   - **0** for background pixels
   - **1** for border pixels
   - **2, 3, 4, ...** for individual egg objects

5. **Contour Detection for Counting:**  
   I created a black canvas matching the mask image size. Every pixel corresponding to a border or object (from the modified markers array) was converted to white. Finally, I ran contour detection to segment individual eggs and counted the total contours.

## Results

- **Total Egg Count:** 103

## Further Refinements

There’s one remaining issue: in the bottom-right of the image, two markers are still connected, leading to a miscount. Attempts to fix this caused some corner eggs to be ignored. Further refinements could help separate these eggs without losing accuracy elsewhere.

## Tools and Libraries Used

- **OpenCV:** For image processing, color conversion, thresholding, morphological transformations, and watershed segmentation.
- **NumPy:** For efficient numerical operations on image data.

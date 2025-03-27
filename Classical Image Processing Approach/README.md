# Trout Egg Detection and Counting

This project demonstrates a classical computer vision approach to detect and count trout eggs in an image. The process involves several steps to segment and accurately count the eggs, even when they overlap.

## Overview

The image features uniform lighting and background; however, slight variations in BGR values occur due to shadows or reflections. To mitigate these variations, the image is converted to the HSV color space, allowing segmentation based on the eggs' orange hue.

## Solution Process

The segmentation result serves as a mask for the eggs. Initially, a straightforward contour detection on the mask would merge overlapping eggs into a single large blob. To address this, the following steps were implemented:

1. **Distance Transform:**  
   The distance transform method was applied to locate the centers of the eggs, even when they overlap.

2. **Thresholding:**  
   After detecting the centers, thresholding was applied to mark each egg's center in white while turning the rest of the image black. The threshold value of 0.28 was determined through multiple rounds of hyperparameter tuning.

3. **Morphological Operations:**  
   The thresholded image exhibited some distortions, which were corrected by applying a chain of morphological operations. The specific sequence of these operations was finalized after extensive experimentation.

4. **Watershed Segmentation:**  
   Once the centers were clearly defined, they were used as markers for the watershed algorithm. The watershed algorithm separates overlapping objects by "flooding" regions based on distance information. The output is a modified markers array where:

   - **0** represents background pixels
   - **1** represents border pixels
   - **2, 3, 4, ...** represent the egg objects

5. **Contour Detection for Counting:**  
   A black canvas of the same size as the mask image was created. Every pixel corresponding to a border or object (as determined by the modified markers array) was converted to white. Finally, contour detection was applied to segment the individual objects, and the total number of contours detected corresponds to the egg count.

## Results

- **Total Egg Count:** 103

## Further Enhancement

A minor issue remains: in the bottom-right side of the image, two markers remain connected, causing them to be counted as a single egg. Efforts to reduce this joint connection resulted in some other corner egg markers being ignored.

## Tools and Libraries Used

- **OpenCV:** Used for image reading, color space conversion, thresholding, morphological transformations, and watershed segmentation.
- **NumPy:** Supports efficient numerical operations on image data.

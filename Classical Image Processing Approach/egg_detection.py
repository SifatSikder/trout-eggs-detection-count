import cv2
import numpy as np

def main():
    image = cv2.imread("trout_egg.jpg")
    original = image.copy()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_orange = np.array([5, 165, 100])
    upper_orange = np.array([25, 255, 255])
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    dist_transform = cv2.distanceTransform(mask, cv2.DIST_L2, 3)
    cv2.normalize(dist_transform, dist_transform, 0, 1.0, cv2.NORM_MINMAX)
    dist_transform = cv2.morphologyEx(dist_transform, cv2.MORPH_CLOSE, None, iterations=2)
    _, sure_foreground = cv2.threshold(dist_transform, 0.28, 1.0, cv2.THRESH_BINARY)
    sure_foreground = cv2.morphologyEx(sure_foreground, cv2.MORPH_CLOSE, None, iterations=1)
    sure_foreground = cv2.morphologyEx(sure_foreground, cv2.MORPH_OPEN, None, iterations=1)
    sure_foreground = cv2.morphologyEx(sure_foreground, cv2.MORPH_ERODE, None, iterations=2)
    sure_foreground = cv2.morphologyEx(sure_foreground, cv2.MORPH_DILATE, None, iterations=1)
    sure_foreground = np.uint8(sure_foreground)
    _, markers = cv2.connectedComponents(sure_foreground)
    markers = markers + 1
    markers[mask == 0] = 0
    cv2.watershed(image, markers)
    segmented = np.zeros_like(mask)
    segmented[markers > 1] = 255
    contours, _ = cv2.findContours(segmented, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    egg_count = len(contours)
    for i, cnt in enumerate(contours):
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(original, center, radius, (0, 255, 0), 2)
        cv2.putText(original, str(i+1), (center[0]-10, center[1]-10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
    print(f"Total number of eggs detected: {egg_count}")
    cv2.imwrite("results/1.mask.png",mask)
    cv2.imwrite("results/2.segmented.png",segmented)
    cv2.imwrite("results/3.final_result.png",original)
    

if __name__ == "__main__":
    main()

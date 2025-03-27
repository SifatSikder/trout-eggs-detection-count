# Trout Egg Detection Using YOLO

## Task

Detect and count trout eggs in a given image using a classical computer vision approach.

## Solution Process

To achieve this, I used the YOLO (You Only Look Once) model. However, the main challenge was obtaining a dataset capable of training the model effectively.

### Dataset Challenge

Luckily, I managed to find a dataset containing 465 images in the internet, but only about 100–120 of these images actually contained trout eggs. The rest were irrelevant frames. Given this limitation, I trained my YOLO model for 50 epochs using an L40S GPU.

### Training and Experimentation

I experimented with different training epochs: 20, 40, 50, 100, 150, 200, and 1000. Through experimentation, I found that training for **50 epochs** provided the best results. Additionally, I determined that a **confidence threshold of 0.68** minimized misclassification.

### Inference Results

After running inference on the model, I obtained the following results:

- **Correctly classified eggs:** 99
- **Incorrectly classified eggs:** 1
- **Undetected objects:** 5

**Total Egg Count:** 100

## Further Enhancements

Since the dataset is limited, manually labeling more images and increasing the dataset size through augmentation will help improve the model's performance. A richer dataset will enable the YOLO model to train better and more accurately detect trout eggs.

## Tools and Libraries Used

- **YOLO:** Used for trout egg detection
- **OpenCV:** Used for visualization of detected eggs

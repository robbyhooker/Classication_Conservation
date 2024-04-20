# Conservation for Classification
 My senoir project!

This project is a machine learning model which performs object detection on aerial wildlife image data, which is being done using the YOLOv8 algorithm. 
YOLOv8: [Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLO (Version 8.0.0) [Computer software]. https://github.com/ultralytics/ultralytics]

## Dataset
That data used is from the WAID dataset, whose acompanying paper can be found at the following link:[https://www.mdpi.com/2076-3417/13/18/10397] 

The WAID dataset contains 14,366 images, split into train, validation, and test sets at a 7:2:1 ratio
All images are a uniform 640 x 640 pixels, and contain corresponding anotation files
Animal Classes include: cattle, sheep, seals, kiang, camels, and zebras

Example Image of Sheep:
<br>
![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/sheeptest.jpg)

## Training
The final model was trained over 100 epochs, with a batch size of sixteen
During training we see loss decrease and mAP increase:
![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/Screenshot%202024-04-20%20111331.png)
## Testing
In testing the model we see consistent accuracy throughout classes:
![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/Screenshot%202024-04-20%20111356.png)


We also see the model is sufficient object detector in the test images:
![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/sheep_annotated.jpg)




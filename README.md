# Classification for Conservation
  This project is an exploration of machine learning applied to ecology and 
wildlife conservation. The specific aim of the project was to detect, classify, 
and track wildlife in aerial imagery. As a byproduct, this presented me with 
the opportunity to learn about machine learning generally, and in its current 
state-of-the-art. To achieve the desired model, I explore existing research, 
methods, and data related to the subject. 
Furthermore, we will explore the famous real time detection algorithm 
YOLO. Discussing how it works internally, why it has become so prevalent, 
and its application to our specific case of aerial wildlife imagery.<br>

 The inspiration for this project comes from my love/fascination for nature and 
interest in machine learning. The reason I chose to study computer science is 
because the breadth of applications the discipline presents. The real time 
object detection of wildlife is both practical for conservation efforts, and 
insightful into computer vision research, making this a compelling endeavor. 
In the field, models like the proposed can be used to monitor wildlife habitats, 
assisting in population censuses, identifying poachers, and ecosystem 
analysis. On a personal level, I hope the commencement of this project is the 
beginning of my further exploration of these fields.<br>


This project is a machine learning model which performs object detection on aerial wildlife image data, which is being done using the YOLOv8 algorithm. 
YOLOv8: [Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLO (Version 8.0.0) [Computer software]. https://github.com/ultralytics/ultralytics]

## Dataset
That data used is from the WAID dataset, whose acompanying paper can be found at the following link:[https://www.mdpi.com/2076-3417/13/18/10397] 

In training machine learning models, the two most valuable assets to an 
engineer are data and compute. Prior to training the wildlife classification 
model at hand, these resources were carefully explored. The WAID1 dataset is 
a free and publicly available dataset designed for the object detection of 
wildlife in aerial imagery. It contains 14,366 images of wildlife, split into 
train, validation, and test sets at a 7:2:1 ratio, respectively. For each image in 
the set there is an accompanying .txt file which contains the class of each 
animal in the image, along with their bounding box coordinates. This data 
format is known as “YOLO” format, as it is used for the ever-popular real
time object detection algorithm, YOLO (You Only Look Once). The images 
in this set are also a uniform 640 x 640 pixels, which is the default input for 
YOLOv8, which was the state-of-the-art version during the training of this 
model. Several other datasets were considered; however, it was determined 
that WAID was the most comprehensive and usable set of those available. The 
animals included in the data are cattle, sheep, kiang, camels, seals, and zebras.

Example Image of Sheep:<br>

![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/sheeptest.jpg)

## Training
The final model was trained over 100 epochs, with a batch size of sixteen
During training we see loss decrease and mAP increase:<br>

![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/Screenshot%202024-04-20%20111331.png)
## Testing
In testing the model we see consistent accuracy throughout classes:<br>

![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/Screenshot%202024-04-20%20111356.png)


We also see the model is sufficient object detector in the test images:<br>

![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/sheep_annotated.jpg)




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
YOLOv8: [Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLO (Version 8.0.0) [Computer software]. https://github.com/ultralytics/ultralytics

## Table of Contents

1. [Dataset](#dataset)
2. [Methods](#methods)
3. [Results](#results)
4. [Conclusions](#conclusions)
5. [Future Work](#future-work)

## Dataset
That data used is from the WAID dataset, whose acompanying paper can be found at the following link: https://www.mdpi.com/2076-3417/13/18/10397

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

## Methods
 The reason compute is so essential in training machine learning algorithms is because the models may need to perform 
billions, or even trillions of floating-point operations to adjust the weights of the model. Performing this number of operations 
can be very time consuming, however the use of a dedicated graphics processing unit (GPU) can greatly increase performance. 
This is because GPUs are tailored to perform matrix operations, such as convolutions and multiplications, in parallel, allowing 
them to do so much faster than the CPU. Knowing this, when training a large convolutional neural network, it is essential to 
utilize a GPU. With recent demand for cloud computing, cloud GPUs have become increasingly available at lower costs. For 
this reason, in training our model, we will deploy the Google Collaboratory's cloud GPU infrastructure, which will increase 
performance on the order of 100x!<br>

 The algorithm chosen the detection problem was YOLOv82. YOLOv8 uses deep learning to build a convolutional neural 
network which makes real time object detections. This was an obvious choice for three main reasons, the first being the ease of 
use with our chosen dataset, as it is already in the correct format for YOLOv8. Next, this model will be most useful in wildlife
 conservation efforts if it is able to detect in real time, and YOLO is built for real time detection. Finally, the popularity of the 
algorithm also means it has a large support community, and an abundance of resources at the engineer's disposal.<br>

The algorithm gets its name from the fact that it can detect objects in a single forward pass of a given image. This 
breakthrough was essential to the high efficiency of the algorithm, allowing it to detect in real time. The diagram below is 
taken from the original YOLO research paper3.Of course, YOLOv8 has become far more complex than the original, however 
this image is still relevant for high level understanding of the algorithm. The convolution layers of the algorithm downsize the
 input image while performing various convolution operations, each of which produces a feature map. In theory and practice, 
these feature maps contain key information edges, corners, patterns, gradients, etc. These convolution layers along with 
activation and pooling layers eventual shrink the input image to an output tensor. This tensor contains the algorithms 
prediction for the classes of the objects detected, along with their corresponding bounding boxes.<br>

In the case of our 640x640 pixel images, the model will eventually downsize them into a final 20x20x16 tensor. Each cell in 
the tensor contains the algorithms overall prediction for the image. This includes the confidence score of an object being 
present in the cell, the bounding box coordinate prediction, and a probability assigned to each class.<br>

![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/yolo.png)<br>

Originally, these predictions are random, as the model has no sense of the truth, however over each epoch, a proper machine learning model will decrease its error and become a sufficient predictor. It does so by comparing its output prediction to the ground truth classes and bounding boxes that correspond with the image in our dataset. The algorithm calculates the error between its prediction and the truth and uses it to adjust the parameters that determine the convolution function, this is known as back propagation. As the parameters become better at predicting the contents of the images, the model becomes learned. <br>

To measure the performance of the model we will use mean average precision (mAP). This is calculated by the area under the curve of the precision-recall curve, which is show below.<br>

![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/pr_curve.png)

## Results
For the training of our algorithm on aerial wildlife imagery, we will use the methods discussed, and expect to see a decrease in error and increase in accuracy over the course of training. In this case we will train over 100 passes of the dataset (epochs), in each epoch the model will ‘see’ each image in the dataset once, adjusting its parameters accordingly for each batch of images. The results of this project were obtaining using a batch size of 16, over 100 epochs. The charts below show the error and accuracy statistics of our model over the course of training.<br>

The box_loss measures the error in the model’s bounding box predictions over the training of the model. It is calculated by the mean squared error between detected box coordinates and corresponding ground truth coordinates. Similarly, cls_loss measures the error in the model’s class predictions over the training of the model. It is calculated by the cross-entropy loss between the predicted class probabilities and the actual class label. Considering these are measures of error, we are pleased to see them decrease throughout training. Similarly, since mAP50 and mAP50-95 are measures of accuracy, we are pleased to see them increase of the course of training.<br>

![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/Screenshot%202024-04-20%20111331.png)
![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/Screenshot%202024-04-20%20111356.png)

We also see the model is sufficient object detector in the test images:<br>

![alt text](https://github.com/robbyhooker/Classication_Conservation/blob/main/example_images/sheep_annotated.jpg)

## Conclusions
Upon testing the model against data unseen in the training process, the statistics remain promising. We see that precision, recall, and map50 are consistently above 90%. The mAP50-95 averages 63.7% across all classes, which is still impressive considering the high IOU threshold. Given these statistics, I can confidently say this model is an adequate classifier of wildlife in images. It is also proven to be a sufficient tracker when applied to real world video of wildlife! So, the model is not only working on paper, but also performs well in practical cases. This is an exciting outcome for me, as I have learned how to apply methods that are being used to further the fields of ecology research and wildlife conservation!<br>

## Future Work
Going forward, I would like to bolster this model by adding more data, including more species of animal. Doing so might entail traveling to a habitat and collecting new data to add to the dataset. The goal is to have a model that can make predictions on all classes of animal in a habitat, and then deploy the model via live drone or UAV imagery. Coupling this with a dedicated GPU would allow for real time detection of animals in their natural environment!<br>

I also look forward to tweaking the hyperparameters of the network  and analyzing its inner layers. This could lead to insight and a higher performing model.<br>






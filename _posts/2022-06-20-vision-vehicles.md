---
layout: post
title: Vehicle counting, tracking and classification in highway roads with Day and Night environment
subtitle: Deep Learning models to count and track vehicles
gh-repo: FedericoZanotti/Vision-project
gh-badge: [star, fork, follow]
tags: [Vision]
comments: true
---

# Vehicle counting, tracking and classification in highway roads with Day and Night environment  [<img src="https://logos-world.net/wp-content/uploads/2020/11/GitHub-Logo.png" width=50/>](https://github.com/FedericoZanotti/Vision-Project.git)

In this project made for the Vision and Cognitive Services course my colleague and I mainly focused on vehicle counting, detection and tracking in video in day and night time.
For this project we decided first to build different systems that are able to detect and track vehicles in order to count them and compare the results.
Secondly, we added a classification step on the vehicle, we detected the direction movement and we built a system that is able to detect license plates and perform OCR (Optical Character Recognition) on them. 

For the detection and tracking part we choose different approaches:
* **YoloV3** with a _tracking algorithm developed by us_
* **Background subtraction** with _OpenCV_
* **YoloV4** with _DeepSORT_ for object tracking.

We tested all these methods also in a night environment, a challenging task that led to good results. We achieved the best results with Yolov4 DeepSORT, also in the night environment, 
and a good accuracy for Yolov3 with our tracking method both for day and night videos. 
The worst performance was obtained by the OpenCV method, especially in the night environment.

# Results

## OpenCV

First I report the experiments using OpenCV, and in day time the results are pretty good with some mistakes, while in night time it's the opposite: the algorithm
can not see any vehicles because the only movement that the background subtraction algorithm intercept is given by the light of the cars.

#### DayTime

In the left there is what background subtraction perceive, while on the right there is the final result

Background Subtractin             | Final Result

:-------------------------:|:-------------------------:
<img width =400 src="/assets/img/opencv_day_bs.gif" /> | <img align="right" width=400 src="/assets/img/opencv_day.gif" />



#### NightTime

Background Subtractin             | Final Result

:-------------------------:|:-------------------------:
<img width =400 align="left" src="/assets/img/opencv_night_bs.gif" /> | <img width=400 align="right" src="/assets/img/opencv_night.gif" />

## Yolov3


#### DayTime


#### NightTime


## Yolov4


#### DayTime


#### NightTime










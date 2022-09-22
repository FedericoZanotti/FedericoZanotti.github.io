---
layout: post
title: Can we Predict an Heart Failure?
subtitle: Heart failure is an unexpected event that could be mortal, so it is very important to understand what are the parameters that influence it. In this work I have analyzed some possible vital signs to monitor in order to predict an heart failure
thumbnail-img: /assets/img/heart.jpg
gh-repo: FedericoZanotti/Can-we-predict-Heart-Failure
gh-badge: [star, fork, follow]
tags: [Heart Failure, Statistical Learning, R]
comments: true
---

# Heart Failure [<img src="https://logos-world.net/wp-content/uploads/2020/11/GitHub-Logo.png" width=50/>](https://github.com/FedericoZanotti/Can-we-predict-Heart-Failure.git)

The heart failure is an unexpected event, that can occur at any age, but is most common in older people. 
Heart failure means that the heart is unable to pump blood around the body properly. It usually happens because the heart has become too weak or stiff.
There many factors that can cause an heart failure, like for example high blood pressure, cardiomyopathy, arrhythmias and many others. Some aspects of the lifestyle influence
the heart activity such as obesity and drinking too much alcohol.

## Dataset

The objective of this project was to find which are the most important parameter that can influence an heart failure, in particular
In this project I have analyzed a dataset containing the medical records of 299 Heart Failure patients collected at the
Faisalabad Institute of Cardiology and at the Allied Hospital in Faisalabad (Punjab, Pakistan), during
April–December 2015 . The patients consists of 105 women and 194 men, and their ages range between 40
and 95 years old. 
The dataset contains several features for each patient, listed and discussed in the [report](https://github.com/FedericoZanotti/Can-we-predict-Heart-Failure/blob/main/Zanotti_Federico_Report.pdf) 
of the github repo.

## Method

In this work I used R as programming language, as requested by the Professor of the Statistical Learning course, and I have implemented and compared three models:
1. **GLM**: Generalized Linear Model generalizes linear regression by allowing the linear model to be related to the response variable via a link function
2. **LDA**: Linear discriminant analysis is a classification method that approximates the Bayes Classifier
3. **QDA**: Quadratic discriminant analysis is a variant of LDA that allows for non-linear separation of data. It is a more general version of the linear classifier.

Moreover I did some exploratory data analysis in order to catch some pattern in data. Graph and tables are discussed in the report.

## Result

Finally,the report shows that _age_, _ejection fraction_ and
_serum creatinine_ (some medical parameters present in the dataset) are the most relevant features, and we only need these to detect an heart failire. 
In fact **GLM** with these features has an **high recall (83%)**, meaning that the model well identifies when a subject has an Heart Failure. 
This result is encouraging for the hospitals, because even if some clinical features of a patient are missing or incomplete, doctors are able to predict 
patient survival by analyzing the _ejection fraction_ and _serum creatinine_ values according also to the _age_. 





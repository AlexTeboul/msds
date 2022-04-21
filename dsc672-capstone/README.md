# DSC 672: Capstone Project

**Link:** https://www.kaggle.com/alexteboul

TLDR: In this competition we were tasked with predicting shelter pet popularity based on images of the animals. 
Metadata was provided that had human generated feature information about the images - 
like if the pet was in focus and not occluded. Unfortunately, not much signal could be obtained. 
The target variable was the Pawpularity score, a proprietary click-rate score from PetFinder.my that was not well explained by the images or human-generated metadata.

Only improvements over guessing the mean Pawpularity score involved applying transfer learning to predict pet breed of cat and dog, then training models to infer pawpularity based on breed. 
Some breeds were preferred over others in terms of click-rate on the website. 

1. In [Tutorial Part 1: EDA for Beginners](https://www.kaggle.com/alexteboul/tutorial-part-1-eda-for-beginners), we cover the exploratory data analysis process from start to finish for the PetFinder.my Pawpularity Contest.
2. In [Tutorial Part 2: Model Building using the Metadata](https://www.kaggle.com/alexteboul/tutorial-part-2-model-building-using-the-metadata), we build models using the metadata (.csv data) provided by the competition hosts. Specifically, we explore Decision Tree Classification, Decision Tree Regression, Ordinary Least Squares Regression, Ridge Regression, Bernoulli Naive Bayes Classification, Random Forest Regression, and Histogram-based Gradient Boosting Regression (LightGBM). RMSE 20.54
3. In [Tutorial Part 3: CNN Image Models 1](https://www.kaggle.com/alexteboul/tutorial-part-3-cnn-image-modeling-1), we explore preprocessing the training images, explaining the data types necessary to model with images, a basic Convolutional Neural Network architecture, and submitting predictions. Tensorflow
4. 
5. 

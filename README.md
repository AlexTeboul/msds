# msds
MS Data Science DePaul University course work for personal reference. 3.9 GPA

1. [CSC 594: Topics in Artificial intelligence](https://github.com/AlexTeboul/msds/tree/main/csc594-topics-in-artificial-intelligence)
2. [CSC 555: Mining Big Data](https://github.com/AlexTeboul/msds/tree/main/csc555-mining-big-data)
3. [CSC 528: Computer Vision](https://github.com/AlexTeboul/msds/tree/main/csc528-computer-vision)
4. [DSC 672: Capstone - Predicting Shelter Pet Popularity with Computer Vision](https://github.com/AlexTeboul/msds/tree/main/dsc672-capstone)
5. [DSC 540: Advanced Machine Learning](https://github.com/AlexTeboul/msds/tree/main/dsc540-advanced-machine-learning)
6. [DSC 510: Health Data Science](https://github.com/AlexTeboul/msds/tree/main/dsc510-health-data-science)
7. [DSC 478: Programming Machine Learning Applications](https://github.com/AlexTeboul/msds/tree/main/dsc478-programming-machine-learning-applications)
8. [DSC 465: Data Visualization in R and Tableau](https://github.com/AlexTeboul/msds/tree/main/dsc465-data-visualization-in-R-and-Tableau)
9. [DSC 450: Databases for Analytics](https://github.com/AlexTeboul/msds/tree/main/dsc450-databases-for-analytics)
10. [DSC 441: Fundamentals of Data Science](https://github.com/AlexTeboul/msds/tree/main/dsc441-fundamentals-of-data-science)
11. [DSC 430: Python Programming](https://github.com/AlexTeboul/msds/tree/main/dsc430-python-programming)
12. [DSC 424: Advanced Data Analysis in R](https://github.com/AlexTeboul/msds/tree/main/dsc424-advanced-data-analysis-R)
13. [DSC 423: Data Analysis and Regression in R](https://github.com/AlexTeboul/msds/tree/main/dsc423-data-analysis-and-regression-in-R)

## [CSC 594: Topics in Artificial intelligence](https://github.com/AlexTeboul/msds/tree/main/csc594-topics-in-artificial-intelligence)
1. [Content Theory Implementation: Emotional Contagion Chatbot](https://github.com/AlexTeboul/msds/blob/main/csc594-topics-in-artificial-intelligence/CSC594_Emotional_Contagion_Content_Theory_Implementation.ipynb)
    * Build a 6 emotional state text classifier using a Gated Recurrent Neural Network
    * Build a 3 state sentiment analysis classifier using a standard Sequential Neural Network
    * Combine these two models into a chatbot game in which an agent gets its mood updated by what is said to it in the chat.

## [CSC 555: Mining Big Data](https://github.com/AlexTeboul/msds/tree/main/csc555-mining-big-data)
1. [Assignment1_AlexTeboul.pdf](https://github.com/AlexTeboul/msds/blob/main/csc555-mining-big-data/Assignment1_AlexTeboul.pdf): 
    * Vectors, SQL, hash keys and hash functions, MapReduce, linux
2. [Assignment2_AlexTeboul.pdf](https://github.com/AlexTeboul/msds/blob/main/csc555-mining-big-data/Assignment2_AlexTeboul.pdf): 
    * MapReduce, SQL, Mappers and Reducers, HDFS replication factor, worker nodes, Hive, Hadoop, AWS EC2
3. [Assignment3_AlexTeboul.pdf](https://github.com/AlexTeboul/msds/blob/main/csc555-mining-big-data/Assignment3_AlexTeboul.pdf): 
    * MapReduce, Hive, Pig
4. [Assignment4_AlexTeboul.pdf](https://github.com/AlexTeboul/msds/blob/main/csc555-mining-big-data/Assignment4_AlexTeboul.pdf): 
    * Hadoop, Page-Rank, Hive, MapReduce jobs, NameNode vs DataNode, Hbase, Mahout
5. [Assignment5_AlexTeboul.pdf](https://github.com/AlexTeboul/msds/blob/main/csc555-mining-big-data/Assignment5_AlexTeboul.pdf):
    * Jaccard distances, matrix normalization, Spark 
6. [Phase1_AlexTeboul.pdf](https://github.com/AlexTeboul/msds/blob/main/csc555-mining-big-data/Phase1_AlexTeboul.pdf):
    * Hadoop, Hive, Pig, Hadoop Streaming

## [CSC 528: Computer Vision](https://github.com/AlexTeboul/msds/tree/main/csc528-computer-vision)
1. [CSC528_A1.pdf](https://github.com/AlexTeboul/msds/blob/main/csc528-computer-vision/CSC528_A1.pdf)
    * Field of view, transforms, projection, color vision differences, probability, vanishing point, stereopsis, optical flow, parallax
2. [CSC528_A2.ipynb](https://github.com/AlexTeboul/msds/blob/main/csc528-computer-vision/CSC528_A2.ipynb)
    * Image matching using OpenCV and SIFT
    * Camera Calibration and implement the 8-point algorithm for weak calibration from binocular point correspondences
3. [CSC528_A3.ipynb](https://github.com/AlexTeboul/msds/blob/main/csc528-computer-vision/CSC528_A3.ipynb)
    * Guassian Mixture Model image segmentation
4. [CSC528_StyleGAN2_Presentation.pdf](https://github.com/AlexTeboul/msds/blob/main/csc528-computer-vision/CSC528_StyleGAN2_Presentation.pdf)
    * Presented implementation of StyleGAN2. Considerations for social media accounts with fake images. 
    * Conducted survey on how well humans could distinguish between real and fake faces. [survey link](https://forms.gle/PtkxHrUdeBJvmcXMA)
5. [Generating_Fake_Faces_Exploring_StyleGAN.ipynb](https://github.com/AlexTeboul/msds/blob/main/csc528-computer-vision/Generating_Fake_Faces_Exploring_StyleGAN.ipynb)
    * Code for generating fake faces using StyleGAN2

## [DSC 672: Capstone - Predicting Shelter Pet Popularity with Computer Vision](https://github.com/AlexTeboul/msds/tree/main/dsc672-capstone)

- TLDR: In this competition we were tasked with predicting shelter pet popularity based on images of the animals. 
- Metadata was provided that had human generated feature information about the images - 
like if the pet was in focus and not occluded. Unfortunately, not much signal could be obtained. 
- The target variable was the Pawpularity score, a proprietary click-rate score from PetFinder.my that was not well explained by the images or human-generated metadata.
- Only improvements over guessing the mean Pawpularity score involved applying transfer learning to predict pet breed of cat and dog, then training models to infer pawpularity based on breed. 
- Some breeds were preferred over others in terms of click-rate on the website. 

1. In [Tutorial Part 1: EDA for Beginners](https://www.kaggle.com/alexteboul/tutorial-part-1-eda-for-beginners), we cover the exploratory data analysis process from start to finish for the PetFinder.my Pawpularity Contest.
2. In [Tutorial Part 2: Model Building using the Metadata](https://www.kaggle.com/alexteboul/tutorial-part-2-model-building-using-the-metadata), we build models using the metadata (.csv data) provided by the competition hosts. Specifically, we explore Decision Tree Classification, Decision Tree Regression, Ordinary Least Squares Regression, Ridge Regression, Bernoulli Naive Bayes Classification, Random Forest Regression, and Histogram-based Gradient Boosting Regression (LightGBM). RMSE 20.54
3. In [Tutorial Part 3: CNN Image Models 1](https://www.kaggle.com/alexteboul/tutorial-part-3-cnn-image-modeling-1), we explore preprocessing the training images, explaining the data types necessary to model with images, a basic Convolutional Neural Network architecture, and submitting predictions. Tensorflow
4. The research paper summarizing our project: [Paper](https://github.com/AlexTeboul/msds/blob/main/dsc672-capstone/Paper%20-%20Predicting%20Shelter%20Pet%20Popularity%20with%20Computer%20Vision.pdf)
5. The presentation for our project: [Presentation](https://github.com/AlexTeboul/msds/blob/main/dsc672-capstone/Presentation-%20Predicting%20Shelter%20Pet%20Popularity%20with%20Computer%20Vision.pdf) 

## [DSC 540: Advanced Machine Learning](https://github.com/AlexTeboul/msds/tree/main/dsc540-advanced-machine-learning)
1. [DSC540_A1.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc540-advanced-machine-learning/DSC540_A1.pdf)
    * Decision trees, cross-validation, RMSE and explained variance, run-time
2. [DSC540_A1.py](https://github.com/AlexTeboul/msds/blob/main/dsc540-advanced-machine-learning/DSC540_A1.py)
    * code for A1
3. [DSC540_A2.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc540-advanced-machine-learning/DSC540_A2.pdf)
    * Random forest, accuracy and AUC, feature selection with random forest, bagging regressor.
4. [DSC540_A2.py](https://github.com/AlexTeboul/msds/blob/main/dsc540-advanced-machine-learning/DSC540_A2.py)
    * code for A2
5. [DSC540_A3.ipynb](https://github.com/AlexTeboul/msds/blob/main/dsc540-advanced-machine-learning/DSC540_A3.ipynb)
    * code for A3
6. [DSC540_A3.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc540-advanced-machine-learning/DSC540_A3.pdf)
    * Gradient boosting and Ada boosting, MLPClassifier, XGBoost/AdaBoost/MLP regressors, still all on diabetes and wine datasets
7. [DSC540_A4.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc540-advanced-machine-learning/DSC540_A4.pdf)
    * Support Vector Machines, discriminant analysis, compare RF, DT, Ada, GB, NN, and SVM
8. [DSC540_HeartDiseasePrediction_Paper.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc540-advanced-machine-learning/DSC540_HeartDiseasePrediction_Paper.pdf)
    * Paper exploring the use of different machine learning models for heart disease prediction on the CDC BRFSS 2015 dataset. 250,000+ survey responses. Open sourced dataset, code cleaning notebook, modeling code on Kaggle. Achieved 91% accuracy and 0.84 AUC. Extraced most important features for determining heart disease risk / survey questions that should be asked.
9. [DSC540_HeartDiseasePrediction_Presentation.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc540-advanced-machine-learning/DSC540_HeartDiseasePrediction_Presentation.pdf)
    * Presentation slides for heart disease paper using RF, GB, Adaboost, and NN for diabetes binary classification.
10. [DSC540_JournalArticle_R1.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc540-advanced-machine-learning/DSC540_JournalArticle_R1.pdf)
    * Review of paper that involve RF and GB models along accelerometer data from smartphones.
11. [DSC540_JournalArticle_R2.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc540-advanced-machine-learning/DSC540_JournalArticle_R2.pdf)
    * Review of journal article exploring the use of support vector machines for diabetes and pre-diabetes prediciton. They determined a subset of 10 questions from the National Health and Nutritional Examination Survey could serve as a public health awareness tool to predict diabetes risk. I got similar accuracy/AUC on my model in this class for heart disease prediction and in another class for diabetes prediction using the BRFSS 2015 instead of NHANES.

# [DSC 510: Health Data Science](https://github.com/AlexTeboul/msds/tree/main/dsc510-health-data-science)
1. [DSC510_A1.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc510-health-data-science/DSC510_A1.pdf)
    * SAS analysis on Framingham study data outcomes for cardiovascular diseases.
    * Logistic Regression and random forest cardiovascular disease classification in R
2. [DSC510_A2.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc510-health-data-science/DSC510_A2.pdf)
    * Vcorpus, TFxIDF, wordclouds in R. Visualizations from project and create an infographic for final project.
3. [DSC510_CaseStudy_1.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc510-health-data-science/DSC510_CaseStudy_1.pdf)
    * super fluid cognition in trained musicians review
4. [DSC510_CaseStudy_2.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc510-health-data-science/DSC510_CaseStudy_2.pdf)
    * social media in medicine review
5. [DSC510_DiabetesPrediction_Paper.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc510-health-data-science/DSC510_DiabetesPrediction_Paper.pdf)
    * Building predictive models for type II diabetes risk using BRFSS 2015 dataset. 
    * The best model was a neural network that achieved accuracy of 74.0%, sensitivity of 79.6%, specificity of 69.3%, positive predictive value (PPV) of 72.2%, and negative predictive value (NPV) of 77.2%. 
    * Not outstanding results, but good considering it takes only asking about High Blood Pressure, High Cholesterol, General Health, Age, and Body Mass Index (BMI)
    * Could serve as awareness web tool.
6. [DSC510_DiabetesPrediction_Presentation.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc510-health-data-science/DSC510_DiabetesPrediction_Presentation.pdf)
    * Presentation for diabetes prediction project

## [DSC 478: Programming Machine Learning Applications](https://github.com/AlexTeboul/msds/tree/main/dsc478-programming-machine-learning-applications)
1. [DSC478_A1.ipynb](https://github.com/AlexTeboul/msds/blob/main/dsc478-programming-machine-learning-applications/DSC478_A1.ipynb)
    * bank.csv dataset exploratory data analysis, compare and contrast customers who opt-in versus out for (PEP) Personal Equity Plans. seaborn pairplots, countplots, etc in Python.
    * Apply z-score normalization to income variable. discretize age category into bins with pd.cut. apply min-max normalization with preprocessing.MinMaxScaler(). Get a dummy dataframe with pd.get_dummies. correlation matrices and seaborn heatmap for correlation analysis.
    * matplotlib plotting and crosstabs
2. [DSC478_A2.ipynb](https://github.com/AlexTeboul/msds/blob/main/dsc478-programming-machine-learning-applications/DSC478_A2.ipynb)
    * Create a KNN classifier from scratch that works with Euclidean or Cosine Similarity for distance measure for use on a subset of the Newsgroup dataste - which is often used for experiments in text applications of machine learning techniques / natural language processing.
    * create a KNN accuracy function from scratch.
    * modify the training and test data sets so that term weights are converted to TFxIDF weights (instead of raw term frequencies)
    * Rocchio Method adapted for text categorization
    * Classification using scikit-learn KNN, decision tree, naive bayes (gaussian)
    * Data Analysis and Predictive Modeling on Census data + scikit-learn Naive Bayes (Gaussian), decision tree using entropy, and linear discriminant analysis (LDA). 10-fold cross-validation.
3. [DSC478_A3.ipynb](https://github.com/AlexTeboul/msds/blob/main/dsc478-programming-machine-learning-applications/DSC478_A3.ipynb)
    * P1: Linear Regression in Python with scikit-learn on communities dataset for crime. 
    * Create standard Linear Regression model from scratch. Then linear regression with sci-kit and do 10 fold cross validation. compare RMSE.
    * Feature selection, get most informative features from scratch. MAE. Accuracy plots by percentage of selected features.
    * Ridge and Lasso Regression in scikit. Plus alpha parameter tuning.
    * Stochastic gradient descent for regression making sure to standardize using StandardScaler and GridSearchCV. choose optimal l1 or l2 penalty. Use elasticnet penalty on the best parameter settings
    * P2: Automatic Document Clustering on newgroup dataset. Create a cosine similarity distance metric from scratch.  Create kmeans from scratch. Apply kmeans and use topN from scratch.
    * P3: PCA for Dimensionality Reduction in Clustering - scikit (sklearn) decomposition (PCA) performed on image segmentation dataset. Calculate completeness and homogeneity scores with and without PCA - because they're close we can use PCA. 
4. [DSC478_EC.ipynb](https://github.com/AlexTeboul/msds/blob/main/dsc478-programming-machine-learning-applications/DSC478_EC.ipynb)
    * Jokes recommender system from scratch - needs revision.
5. [DSC478_final_paper.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc478-programming-machine-learning-applications/DSC478_final_paper.pdf)
    * Course final project looking at a subset of Yelp Reviews dataset performing NLP techniques. I built a sentiment analysis model from scratch and analyzed how it impacted review / if review score. Applied Logistic Regression to predict if a yelp review would be high (4 or 5) or low (1, 2, or 3) based on sentiment. Based on just the sentiment alone, 83% accuracy was obtained in predicting high vs low yelp review.
6. [DSC478_sentiment_analysis.ipynb](https://github.com/AlexTeboul/msds/blob/main/dsc478-programming-machine-learning-applications/DSC478_sentiment_analysis.ipynb)
    * The code for the final project - exploratory data analysis, sentiment analysis from scratch, logistic regression

## [DSC 465: Data Visualization in R and Tableau](https://github.com/AlexTeboul/msds/tree/main/dsc465-data-visualization-in-R-and-Tableau)
1. [DSC465_A1.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc465-data-visualization-in-R-and-Tableau/DSC465_A1.pdf)
    * Graph time series Intel stock data in Tableau. Stock price and volume over time in Tableau. Histograms. Scatterplots. Error histograms and bar charts for a perception experiment dataset. Boxplots of absolute error for different tests in the dataset in Tableau. 
    * Infant data scatter plots male vs female height vs weight in R with ggplot2. Scatterplot with trendlines in R. 
    * GM car price dataset treemap by make and model price in Tableau. Packed bubble chart in Tableau.
    * More line graphs, stacked area charts, and boxplots in Tableau. 
    * Dissecting a bad visualization and proposing an alternative
2. [DSC465_A2.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc465-data-visualization-in-R-and-Tableau/DSC465_A2.pdf)
    * Dot chart showing median error in Tableau. Jittered categorical scatterplot in Tableau. 
    * Violin Plots in R. Multi-layered boxplots in Tableau. Log-Scale time series line graphs in Tableau for stock price. 
    * Astronomical data visualization in R. Messier (stars/etc visible to the naked eye in the night sky when dark) apparent magnitude vs messier number scatter in R. Used ggplot2 violin plots to compare kinds of astronomic objects and distance away. Messier distance vs apparent magnitude bubble scatter in R using ggplot2.
3. [DSC465_A3.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc465-data-visualization-in-R-and-Tableau/DSC465_A3.pdf)
    * Portland water level dataset heatmaps for water level in R and Tableau. Line graph moving averages in Tableau.
    * Chicago crime dataset types of crime bar graphs over time in R. Rose plots in R. Hexbin plots of latitude v longitude of crimes.
    * Company dataset treemaps for budget visualzation by department.
4. [DSC465_A4.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc465-data-visualization-in-R-and-Tableau/DSC465_A4.pdf)
    * Food Services by state aggregated chloropleth charts in Tableau. Tile cartograms in Tableau. 
    * Overlaying hex-bin plots over geospatial crime data in Chicago. Small multiples chloropleths showign crime type counts by ward in Chicago geospatially.
    * Plot terrain data in R using heatmaps and contour plots

## [DSC 450: Databases for Analytics](https://github.com/AlexTeboul/msds/tree/main/dsc450-databases-for-analytics)
1. [DSC450_A1.pdf](https://github.com/AlexTeboul/msds/tree/main/dsc450-databases-for-analytics/DSC450_A1.pdf)
    * creating tables, primary keys, foreign keys, SQL DDL scripts, 
2. [DSC450_A2.pdf](https://github.com/AlexTeboul/msds/tree/main/dsc450-databases-for-analytics/DSC450_A2.pdf)
    * schema decomposition, SQL DDL and SQL INSERT statements
    * Create tables with Python and sqlite3, simple SQL queries
3. [DSC450_A3.pdf](https://github.com/AlexTeboul/msds/tree/main/dsc450-databases-for-analytics/DSC450_A3.pdf)
    * SQL queries with joins, group by, order by, having. More sqlite3 Python SQL table creation, SQL query with sub-queries
4. [DSC450_A4.pdf](https://github.com/AlexTeboul/msds/tree/main/dsc450-databases-for-analytics/DSC450_A4.pdf)
    * Python random number generation, more SQL queries and Python sqlite3, PL-SQL Trigger script
5. [DSC450_A5.pdf](https://github.com/AlexTeboul/msds/tree/main/dsc450-databases-for-analytics/DSC450_A5.pdf)
    * Create a database of tweets with Python and sqlite3, writing functions to load data into the tables, executing SQL queries, top-words querying
6. [DSC450_TakeHomeFinal.ipynb](https://github.com/AlexTeboul/msds/tree/main/dsc450-databases-for-analytics/DSC450_TakeHomeFinal.ipynb)
    * Load in 1,000,000 tweets into tables defined in Python with sqlite3, run with batching, write and execute specific queries for analyzing the twitter data.

## [DSC 441: Fundamentals of Data Science](https://github.com/AlexTeboul/msds/tree/main/dsc441-fundamentals-of-data-science)
1. [DSC441_A1.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc441-fundamentals-of-data-science/DSC441_A1.pdf)
    * classification vs clustering, classification and prediciton, feature selection and feature extraction, data mining and SQL, data warehouses vs data marts
    * data mining tasks - what is vs isn't data mining.
    * iris dataset analysis in SPSS. scatterplots, descriptive statistics, histograms, boxplots in SPSS. Paper review.
2. [DSC441_A2.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc441-fundamentals-of-data-science/DSC441_A2.pdf)
    * Boxplots, skewness & kurtosis, Q-Q plots in SPSS. 
    * z-score normalization, min-max normalization, decimal scaling normalization
    * scatter plot interpretations, correlation matrices vs covariance matrices
    * equal-depth and equal-width partitioning
    * calculating entropy and information gain from scratch. using it to choose best attribute from scratch.
    * Spotify dataset analysis in SPSS.
3. [DSC441_A3.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc441-fundamentals-of-data-science/DSC441_A3.pdf)
    * Decision Trees for Lupus diagnosis in SPSS. Independent variable importances with CRT / visualize feature importances.
    * Decision Trees for red wine quality dataset predictions plus impact of binning.
4. [DSC441_A4.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc441-fundamentals-of-data-science/DSC441_A4.pdf)
    * Questions on KNN computation, accuracy, regression, and sensitivity to number of features.
    * Decision Tree vs KNN capabilities, ROC - AUC interpretation 
    * High sensitivity vs high specificity which is better for a given scenario. (should actually be sensitivity in this case)
    * Letter recognition tabular dataset decision tree and KNN
5. [DSC441_A5.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc441-fundamentals-of-data-science/DSC441_A5.pdf)
    * k-means clustering on seeds dataset. euclidean distance similarity measure. importance of normalization in KNN and k-means.
    * Choosing a k value plus scree-plot.
    * heirarchical clustering with single linkage algorithm and show dendrogram. again with complete linkage. Compare with k-means on purity. write an executive summary on it.
    * Decision trees and 3-D scatters in SPSS.

## [DSC 430: Python Programming](https://github.com/AlexTeboul/msds/tree/main/dsc430-python-programming)
1. [DSC430_A1_P1.py](https://github.com/AlexTeboul/msds/blob/main/dsc430-python-programming/DSC430_A1_P1.py)
    * overlap area of 2 squares
2. [DSC430_A1_P2.py](https://github.com/AlexTeboul/msds/blob/main/dsc430-python-programming/DSC430_A1_P2.py)
    * true/false if prime
    * true/false if happy integer
    * true/false if happy prime
    * print first n primes, n happy, n happy primes, n sad primes
3. [DSC430_A2_P1.py](https://github.com/AlexTeboul/msds/blob/main/dsc430-python-programming/DSC430_A2_P1.py)
    * from a list of boys names and girls names write a function that says how many times each name ends in a given letter and compare
    * girls names 3x as likely to end in a vowel
4. [DSC430_A2_P2.py](https://github.com/AlexTeboul/msds/blob/main/dsc430-python-programming/DSC430_A2_P2.py)
    * function asks the user to enter the x and y coordinates for the two focal points of the ellipse, the length of the major axis and 
    the number of random points to employ.  
    * The program then computes and prints the area of the ellipse from randomly generated points.'''
5. [DSC430_A3_dicecupgame.py](https://github.com/AlexTeboul/msds/blob/main/dsc430-python-programming/DSC430_A3_dicecupgame.py)
    * create a dicecup game with various rules and the ability to bet on outcomes and keep track of score.
6. [DSC430_A4_P2.py](https://github.com/AlexTeboul/msds/blob/main/dsc430-python-programming/DSC430_A4_P2.py)
    * build a web-scraper/crawler to get the most common words and their counts accross n-pages on a particular web domain using recursion.
7. [DSC430_A5.ipynb](https://github.com/AlexTeboul/msds/blob/main/dsc430-python-programming/DSC430_A5.ipynb)
    * NumPy basics
    * Conway???s Game of Life in Python with NumPy
    * MatPlotLib basics

## [DSC 424: Advanced Data Analysis in R](https://github.com/AlexTeboul/msds/tree/main/dsc424-advanced-data-analysis-R)
1. [DSC424-HousingPriceAnalysis-Paper.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc424-advanced-data-analysis-R/DSC424-HousingPriceAnalysis-Paper.pdf)
    * This paper explores the relationship between home features and sale prices using a combination of exploratory and predictive techniques. More specifically, we seek to answer the question of what home features influence the sale prices of homes in Ames, Iowa. We performed a principal component analysis, common factor analysis, random forest classification, and linear regression in R. Our principal component analysis and common factor analysis uncovered key underlying structures regarding quality, quantity, and room types as the most significant features to explain our data. Through the use of random forest classification and linear regression, we determined that features that add value to a home are commonly associated with larger square footage and the perceived newness of a home, such as when it was built or remodeled.
    * **Keywords**: principal component analysis, common factor analysis, random forest classification, linear regression, home prices, real-estate
2. [DSC424-HousingPriceAnalysis-Presentation.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc424-advanced-data-analysis-R/DSC424-HousingPriceAnalysis-Presentation.pdf)
    * **Keywords**: principal component analysis, common factor analysis, random forest classification, linear regression, home prices, real-estate
3. [DSC424_A1.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc424-advanced-data-analysis-R/DSC424_A1.pdf)
    * About me, linear algebra, marices, vectors in R, Bayesian Linear Regression Journal Article Summary, Data Ethics & Integrity Journal Article Summary, Regression Analysis and visualization in R, multicollinearity checks with VIF>10
4. [DSC424_A2.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc424-advanced-data-analysis-R/DSC424_A2.pdf)
    * Project selection (Ames housing price analysis), advantages and disadvantages of ridge vs lasso regression, causes of overfitting and how to treat/diagnose overfitting in regression, what is multicollinearity and how to address it, analyze the factor analysis performed in a journal article, analyze the PCA performed in a journal article, perform PCA in R, run common factor analysis in R
5. [DSC424_A3.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc424-advanced-data-analysis-R/DSC424_A3.pdf)
    * Perfrom Common Factor Analysis (CFA) in R, create and interpret scree-test with eigen-values vs components, analyze and critique a journal article that uses Canonical Correlation (CC), analyze a second paper using CC, Perform Cannonical Correlation in R, analyze bartlett's chi-squared test results, perform correspondence analysis, create a PCA visualization to help with correspondence analysis
6. [DSC424_A4.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc424-advanced-data-analysis-R/DSC424_A4.pdf)
    * Perform Linear Discriminant Analysis (LDA) in R on housing data, Apply Random Forest Classification and compare to the results of LDA, summarize a journal article that uses cluster analysis in the field of metabolomics/drug research, analyze/summarize a journal article that uses PCA and LDA, perfrom linear discriminant analysis in R for bond ratings classification, analyze/summarize a Natural Language Processing paper where the authors compare Factor Analysis and Latent Dirichlet Allocation for topic modeling 

## [DSC 423: Data Analysis and Regression in R](https://github.com/AlexTeboul/msds/tree/main/dsc423-data-analysis-and-regression-in-R)
1. [DSC423_A2.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc423-data-analysis-and-regression-in-R/DSC423_A2.pdf)
    * Using R markdown. scatterplot matrix in R. correlation matrix in R. Fit a linear regression model and compute VIF statistics to check for multicollinearity.
    * compare coefficient of determination R2 and adjusted R2. create residual plots in R. qq-plots. linear regression test for influencial points / outliers in R. 
    * more linear regression models and predicted vs residuals plots looking for random scatter to show linearity. impact of changing beta values on prediction from linear regression.
    * 95% confidence intervals for different values input for the betas.
2. [DSC423_A3.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc423-data-analysis-and-regression-in-R/DSC423_A3.pdf)
    * exploratory data analysis and linear modeling for college dataset. multicollinearity checks. removing insignificant variables.
    * linear modeling with backward feature selection and forward feature selection
    * predicted vs residuals looking for random scatter to show linearity, qq plot analysis looking for all along line for normality, outlier detection outside -3,3 bounds for studentized residuals.
    * coefficient of determination R2 represents the amount of variation in Y explained by the regression model. The adjusted R2 also describes the amount of variation in Y explained by the regression model but isn't sensitive/altered by simply adding more terms. F statistic with low p value to reject null hypothesis
    * analysis of interaction terms significance, linear regression model, beta parameter estimates, 
    * apply 5-fold cross validation and compute mean absolute percentage error (MAPE) to tell by what percentage off predictions are on average from the actuals
3. [DSC423_A4.pdf](https://github.com/AlexTeboul/msds/blob/main/dsc423-data-analysis-and-regression-in-R/DSC423_A4.pdf)
    * churn analysis in R. boxplots. Logistic Regression in R with backward feature selection to predict churn.


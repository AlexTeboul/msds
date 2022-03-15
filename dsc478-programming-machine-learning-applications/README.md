# DSC 478: Programming Machine Learning Applications

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

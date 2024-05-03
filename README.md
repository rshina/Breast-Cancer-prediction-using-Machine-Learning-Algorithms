# Breast-Cancer-prediction-using-Machine-Learning-Algorithm(SVM Classifier)


## Abstract:

    
Breast cancer represents one of the diseases that make a high number of deaths every
year. It is the most common type of all cancers and the main cause of women's deaths
worldwide. Classification and data mining methods are an effective way to classify data.
Especially in the medical field, where those methods are widely used in diagnosis and
analysis to make decisions.


## Problem Statement:

Given the details of cell nuclei taken from breast mass, predict whether or not a patient
has breast cancer using the Ensembling Techniques. Perform necessary exploratory
data analysis before building the model and evaluate the model based on performance
metrics other than model accuracy.


## Dataset Information:

The dataset consists of several predictor variables and one target variable, Diagnosis.
The target variable has values 'Benign' and 'Malignant', where 'Benign' means that the
cells are not harmful or there is no cancer and 'Malignant' means that the patient has
cancer and the cells have a harmful effect


## Work Flow:


    *  First Import the necessary libraries needed for the project. Below are the libraries that I have used
    
    *  Load the dataset using pandas.
    
    *  Understand the data with basic statistics, info, total records, features and their data types also number of        null values.
    
    *  Perform the data cleaning techniques like treating the missing values.
    
    *  Select the relevent features using Selectkbest method
    
    *  Visualize the data with the help of Matplotlib or Seaborn to get better understanding of the features.
    
         Boxplot(To visualize the Outliers present in the data)
         Histogram (To get idea about the disribution of data in each features)
         Countplot (To get "Benign' and 'Malignant" count)
         Heatmap (To find the Correlation)
         
    *  Data is imbalanced so make it balanced using SMOTE
    
    *  Scale the data using Standerd Scalar
    
    *  Split the data as train and test
    
    *  After the preprocessing of data train the model Using SVM algorithm
    
            Support Vector Machine (SVM) is a supervised machine learning algorithm which can be used for both                  classification or regression challenges. However, it is mostly used in classification problems. In this algorithm, we plot each data item as a point in n-dimensional space (where n is number of features you have) with the value of each feature being the value of a particular coordinate. Then, we perform classification by finding the hyper-plane that differentiate the two classes very well
            
    *  Predict the target
    
    *  Evaluate the output using Classification report,confusion metrix and auc curve
    
    
    *  Created streamlit app it allows the user to give cell information of patient and        can predict whether the patient has cancer or not

##  Conclusion:

   * Machine learning techniques(SVM) is able to classify tumors effectively into malignant and benign tumors with 97.62%  percent accuracy. The technique can rapidly evaluate breast masses and classify them in an automated fashion.

   * Early breast cancer detection can dramatically save lives especially in the developing world. This technique can further improved by combining computer vision and machine learning and deep learning techniques to classify cancer directly using tissue images.
                

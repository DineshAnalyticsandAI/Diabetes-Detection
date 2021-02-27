# Diabetes-Detection
Detect Diabetes in patient using machine learning model (Random Forest)

Application link :  https://diabetes-detection-application.herokuapp.com/

# Business Domain:  Healthcare:  Diabetes
Diabetes is a chronic, metabolic disease characterized by elevated levels of blood glucose (or blood sugar), which leads over time to serious damage to the heart, blood vessels, eyes, kidneys and nerves. The most common is type 2 diabetes, usually in adults, which occurs when the body becomes resistant to insulin or doesn't make enough insulin. In the past three decades the prevalence of type 2 diabetes has risen dramatically in countries of all income levels. Type 1 diabetes, once known as juvenile diabetes or insulin-dependent diabetes, is a chronic condition in which the pancreas produces little or no insulin by itself. For people living with diabetes, access to affordable treatment, including insulin, is critical to their survival. There is a globally agreed target to halt the rise in diabetes and obesity by 2025. 

About 422 million people worldwide have diabetes, the majority living in low-and middle-income countries, and 1.6 million deaths are directly attributed to diabetes each year. Both the number of cases and the prevalence of diabetes have been steadily increasing over the past few decades. 
International Diabetes Federation Key Facts 
(https://www.idf.org/aboutdiabetes/what-is-diabetes/facts-figures.html ): 
•	In year 2019 , Approximately 463 million adults (20-79 years) were living with diabetes; by 2045 this will rise to 700 million\n
•	The proportion of people with type 2 diabetes is increasing in most countries
•	79% of adults with diabetes were living in low- and middle-income countries
•	1 in 5 of the people who are above 65 years old have diabetes
•	1 in 2 (232 million) people with diabetes were undiagnosed
•	Diabetes caused 4.2 million deaths
•	Diabetes caused at least USD 760 billion dollars in health expenditure in 2019 – 10% of total spending on adults
•	More than 1.1 million children and adolescents are living with type 1 diabetes
•	More than 20 million live births (1 in 6 live births) are affected by diabetes during pregnancy

# Problem Statement: 
Diabetes is one of the major chronic diseases in the world.  Early detection and management of disease is key influencer which can help in controlling diabetes. There is need to build a Diabetes Detection web application which can predict whether a person has diabetes or not based on various medical predictors such as glucose level, body mass-index (BMI), Blood pressure, Insulin, Skin Thickness, Age, number of pregnancies and so on.   Web application should use latest and one of the best machine learning model to detect diabetes.  
This application will be useful for people to proactively identify if they are diabetic or not using their phone/laptop with internet connection.  

# Input Dataset: 

## Source:   In this project, we will be using Pima Indians Diabetes dataset which is available in the kaggle website. (https://www.kaggle.com/uciml/pima-indians-diabetes-database/ ).

## Description
This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. Dataset includes females at least 21 years old of Pima Indian heritage.  Dataset includes below listed medical predictors (independent variables) and one target variable.

### Independent variables (features):
•	Pregnancies: Number of times pregnant
•	Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
•	BloodPressure: Diastolic blood pressure (mm Hg)
•	SkinThickness: Triceps skin fold thickness (mm)
•	Insulin: 2-Hour serum insulin (mu U/ml)
•	BMI: Body mass index (weight in kg/(height in m)^2)
•	DiabetesPedigreeFunction: Diabetes pedigree function
•	Age: Age (years)

### Dependent variables (features):
### Outcome: Class variable (0 or 1)

# Solution Statement: 
We will be following steps to build Diabetes detection web application.   This is a supervised machine learning classification problem.  We will perform below steps,
•	Data Acquisition &  EDA
o	Data Collection:  Research and identify dataset for training Diabetes detection machine learning model.  We will utilize Kaggle Pima Indian Diabetes dataset.
o	Perform Exploratory data on data :   Understand data , features and correlations 
•	Model Training & Selection
o	Develop, train and validate multiple models and select best model
•	Evaluate model & Selection
o	   Evaluate and select best models
o	   Generate performance metrics such as F1 score, Precision and Recall
•	Web application
o	Use Streamlit to build web application
•	Deploy Web application 
o	Deploy web application using Heroku (Cloud application platform)

# Benchmark model:
We will use Logistic regression model with F1 score of 0.775 as our benchmark model.   This is from researchgate.net publication white paper on Diabetes detection.   https://www.researchgate.net/publication/334153122_Predictive_Analytics_in_Healthcare_for_Diabetes_Prediction 

# Evaluation metrics: 
Model will be evaluated using below metrics.   Final selected model will be then used in Diabetes detection web application. 
### Accuracy:  Overall, how often is the classifier correct? 
    Accuracy = (True Positive + True Negative/Total)
### Precision:  When model predict yes , how often model is correct ?
    Precision =  True Positive / Predicted Yes
### Recall or Sensitivity: When it's actually yes, how often does it predict yes?
    Recall  =  True positive / Actual yes
### F1 score :  Weighted average of the true positive rate (recall) and precision
    F1 score =   2* ( (  Precision * Recall) / (Precision + Recall) )


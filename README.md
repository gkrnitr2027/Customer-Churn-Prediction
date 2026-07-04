# 📊 Customer Churn Prediction

A Machine Learning project that predicts whether a telecom customer is likely to churn based on customer demographics, account information, and service usage. The project includes Exploratory Data Analysis (EDA), data preprocessing, model building, hyperparameter tuning, and deployment using Streamlit.

---

## 📌 Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses. This project leverages machine learning algorithms to identify customers who are likely to discontinue the service, enabling businesses to take proactive retention measures.

---

## 🚀 Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Label Encoding for Categorical Variables
- Handling Missing Values
- Class Imbalance Handling (SMOTE)
- Model Training using Multiple Algorithms
- Cross Validation
- Model Evaluation using Multiple Metrics
- Streamlit Web Application for Real-time Prediction

---

## 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

The dataset contains customer information including:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract Type
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges
- Churn (Target)

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Pickle
- Streamlit

---

## 📈 Exploratory Data Analysis

Performed:

- Missing Value Analysis
- Duplicate Record Check
- Class Distribution
- Correlation Analysis
- Feature Distribution
- Outlier Detection
- Churn Distribution Visualization

---

## ⚙️ Data Preprocessing

- Removed unnecessary columns
- Handled missing values
- Label Encoding for categorical variables
- Feature Selection
- Train-Test Split
- SMOTE for class balancing

---

## 🤖 Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

---

## 📊 Evaluation Metrics

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix
- Cross Validation Score

---

## 🖥️ Streamlit Application

The project includes a Streamlit web application that allows users to:

- Enter customer details
- Predict customer churn
- View prediction probability
- Display customer information

Run the application:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Customer-Churn-Prediction/
│
├── app.py
├── CCP.ipynb
├── customer_churn_model.pkl
├── encoders.pkl
├── requirements.txt
├── README.md
└── dataset.csv
```

## 📌 Results

The final model successfully predicts customer churn using customer demographics and service information, helping businesses identify customers at risk of leaving and enabling proactive retention strategies.

---

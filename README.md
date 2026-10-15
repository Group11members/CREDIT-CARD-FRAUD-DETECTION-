# CREDIT-CARD-FRAUD-DETECTION- The Credit Card Fraud Detection System is a machine learning project developed by Group 11 to identify potentially fraudulent credit card transactions. It uses a supervised learning approach to classify transactions as either legitimate or fraudulent based on patterns learned from labelled transaction data.

The project combines a trained machine learning model with a Streamlit web application, allowing users to enter transaction features and obtain predictions through a simple interface.

Objectives

- Explore transaction data to understand its structure and characteristics.
- Develop a machine learning model for binary classification of credit card transactions.
- Preprocess transaction features consistently during training and prediction.
- Build an interactive application for testing the trained model.
- Deploy the application to make it accessible through a web browser.

Dataset

The project uses a credit card fraud detection dataset obtained from Kaggle.

The dataset contains the following important columns:

- V1–V28: Anonymised, transformed numerical features representing transaction characteristics. Their original meanings are not individually available in the dataset representation.
- Amount: The monetary value of the transaction.
- Class: The target variable, where "0" represents a legitimate transaction and "1" represents a fraudulent transaction.
- id: A transaction record identifier, which is not part of the model's 29 input features.

During data exploration, we examined the dataset's structure and checked for missing values. The missing-value check on the dataset we examined returned zero missing values.

Model Development

The project follows a supervised machine learning workflow:

1. Data Exploration: Examining the dataset, its features, and the target variable.
2. Preprocessing: Preparing the numerical features and applying a fitted scaler to ensure the inputs are transformed consistently.
3. Model Training: Training a Random Forest classifier using labelled transaction data.
4. Model Evaluation: Assessing the model's performance using the evaluation methods available in the training workflow.
5. Model Saving: Saving the trained model and fitted scaler using Joblib so they can be loaded without retraining the model each time the application starts.
6. Prediction: Passing new transaction features through the saved preprocessing and classification pipeline to obtain a prediction.

The model accepts 29 input features: V1–V28 and Amount. Its output identifies the predicted transaction class. Where supported, the application also displays the model's estimated probability of fraud.

Application Features

The Streamlit web application provides:

- An interactive interface for entering transaction feature values.
- Input fields for all 29 required features.
- Automated prediction using the saved machine learning model.
- Results identifying a transaction as potentially fraudulent or legitimate.
- An estimated fraud probability when available.
- Information about the model and a disclaimer explaining the limitations of its predictions.

Technologies Used

- Python: Main programming language.
- Pandas: Data manipulation and exploration.
- NumPy: Numerical operations.
- Scikit-learn: Machine learning and feature preprocessing.
- Joblib: Saving and loading the trained model and scaler.
- Streamlit: Building the interactive web application.
- Git and GitHub: Version control, source code management, and collaboration.
- Streamlit Community Cloud: Hosting and deployment of the application.

Project Structure

CREDIT-CARD-FRAUD-DETECTION/
├── app.py
├── model.py
├── requirements.txt
├── models/
│   ├── final_model.pkl
│   └── scaler.pkl
├── sample_transactions.csv
├── model_training_results.csv
└── testmodel.py

- "app.py" builds the Streamlit user interface.
- "model.py" loads the saved model and scaler and generates predictions.
- "requirements.txt" lists the Python dependencies.
- "models/final_model.pkl" contains the saved trained model.
- "models/scaler.pkl" contains the fitted scaler.
- "sample_transactions.csv" contains sample transactions used for functional testing.
- "model_training_results.csv" stores model training results.
- "testmodel.py" contains model testing code.

Testing and Deployment

The prediction pipeline was functionally tested using ten prepared sample transactions: five legitimate and five fraudulent. All ten were classified as expected in that initial test. This result demonstrates that the pipeline worked for those examples, but it does not establish the model's overall accuracy or generalisation performance.

The source code and supporting model files are stored in the group's GitHub repository. The application was also configured for deployment using Streamlit Community Cloud. The deployed environment requires its dependencies to be installed correctly for the application to run.

Limitations

This project is an academic prototype. Its predictions are estimates and are not guaranteed to identify every fraudulent transaction correctly. The ten-example functional test is not a substitute for comprehensive evaluation on unseen data. Further testing, performance validation, security controls, and monitoring would be required before considering real-world financial use.

The model should not be used as the sole basis for financial decisions.

Conclusion

This project demonstrates how supervised machine learning can be applied to credit card fraud detection by combining transaction data, preprocessing, a trained Random Forest classifier, and an interactive web application. It also provides practical experience in model integration, software development, version control, testing, and deployment.

Project Team: Group 11
Project Type: Machine Learning Capstone Project
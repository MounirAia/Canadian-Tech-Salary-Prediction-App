## Introduction
The application can be accessed at: https://www.canada-tech-salary.tech/

A web application capable of predicting the salary of an individual working in a tech for  a Canadian-based job.
The goal of this document is to present an overview of the application. This app is for anyone who is thinking about or already working in a tech job at a company based in Canada.

## Product Overview
The application will "predict" the salary of a user using:
- Company size
- Industry type of the company
- Title of the job
- Years of experience of the user
- Country (fix to Canada)
- City where the company is located

### Application Flow
![Big Picture of The Application](https://github.com/MounirAia/Canadian-Tech-Salary-Prediction-App/assets/86434940/f82d4cec-13bc-42db-b3a2-7e31a9b9b6d8)

## Objectives
Learn how to:
 - Design a full-stack web application using various technology.
 - Data processing (whole data science pipeline)
	 - Data Collection
	 - Data Integration
	 - Data Cleaning
	 - Data Visualization
	 - Machine Learning

## Backend
This is a brief description of the few noticeable problems that I had to solve when building the backend of the application.

### I/O Bound
I started the backend by using flask and PyMongo. These 2 libraries are synchronous, which made my application I/O bound. The API request to construct the overview and dashboard views took on average 8.30 seconds due to the multiple database requests made sequentially.

Thus, to solve this problem, I changed the backend web framework to Quart and Mongodb Motor to leverage asynchronous code that allows a better usage of CPU scheduling time. For that reason, the waiting time of this API request takes now around 3 seconds to resolve. Furthermore, during this waiting time, the server can process other user requests which speed up the application and offer a better user experience.

### Model Training

I tested only two different machine learning models: Linear regression model and Random forest regressor model with different parameters' adjustment. I had the best result with the random forest regressor, using various encoding techniques that I found appropriate for the different features. I made available the notebook used to train the different models in the repo data/CreationMLModel.ipynb.

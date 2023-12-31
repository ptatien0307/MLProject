# MLProject - A simple machine learning project 

This project understands how the student's performance (test scores) is affected by other variables such as Gender, Ethnicity, Parental level of education, Lunch and Test preparation course.

# Dataset 
Dataset Source: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977

Some samples
<p align="center">
<img src="https://github.com/ptatien0307/MLProject/assets/79583501/a9aa93c8-089c-4361-be45-fc221644bbdf.png" alt="drawing" width="85%" height="85%"/>
</p>

# Detail 
## Features
In this project, we will use features:
* gender
* Ethnicity
* Parental level of education
* Lunch
* Test preparation course
* Writing score
* Reading score

to predict **math score** of a student

## Model
Some regression models(provided by sklearn) are use in this project:
* Linear, Lasso, Rigde
* RandomForestRegressor
* AdaBoostRegressor
* ...

Also using **GridSearchCV** for hyperparameter tuning and using **r2_score** for evaluation

# Installation
* Install docker (if you don't have)
* Clone this repository
* Build the image using command: `docker build - r <image's name> .`
* Create the container using command: `docker run -d -p 80:80 <image's name>`
* Open a web browser and navigate to http://localhost:80


# Demo
The project is deployed on [render](https://render.com/) with free usage. Due to render's policy, there'll be a delay in the response of the first request after a period of inactivity while the instance spins up. It will take time to load the website

Link: https://simple-ml-project.onrender.com/


<p align="center">
<img src="https://github.com/ptatien0307/MLProject/assets/79583501/f6a24193-4945-4ee4-b2c5-603f8ab41572.png" alt="drawing" width="85%" height="85%"/>
</p>

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9ne_v1oY)
# CSC/SDS293: Homework 2

## Description
The purpose of this homework is to practice Multiple Linear Regression and simple Logistic Regression. 

## Instructions

### Part 1: Linear Model 
For this part of the assignment you will use the Publications dataset included in the ISLR or ISLP package (depending on if you're using R or Python). The dataset contains data on clinical trial publications. You can see documentation for this dataset [here](https://islp.readthedocs.io/en/latest/datasets/Publication.html). 

Filter the dataset to only clinical trials that have been published. This is what you should do the following analyses on. 

Start by fitting a linear regression that models impact as a function of all other variables. 

Based on the summary of this model should you keep all of the predictors in the model? If not, which should you drop and why? 

If you decided to drop any predictors, fit a new model that does not include them and assess whether it is better than the original. 

Next, take a look at the correlation between your variables. Do you see any issues? Which variables are most highly correlated? Investigate and describe the relationship between the two sets of highest correlated variables. 

Fit another linear regression model that includes all variables except for one in each pair of most highly correlated variables. How well does this model fit the data? How does this compare to your earlier models? 


### Part 2: Logistic Regression
You will use the phil.csv dataset included in this repo for this part of the assignment. This data contains information on groundhog's day from 1886 - 2016. You can see documentation on the data [here](https://www.kaggle.com/datasets/groundhogclub/groundhog-day?resource=download). 

Start by filtering the data to only observations where Phil saw a "Full Shadow" or "No Shadow", and observations without NA values.  

Now, model Phil's predictions for spring ("Full Shadow" -> two more weeks of winter, "No Shadow" -> early spring). Make one model for overall average, one for the Northeast, one for the Midwest, and one for Pennsylvania.

What do your models tell you about Phil's predictions across various regions? Do you think Phil is good at his job of predicting spring?   

## Submission and Grading
Please see the assignment overview in `hw02-detailed-rubric.pdf` for submission instructions and rubric. 

# Phishing Email Detection

### Table of Contents
- [Description](#description)
- [Features](#features)
- [Goal](#goal)
- [Usage](#usage)

## Description
This dataset is a collection of english emails labeled as either phishing or legitimate. For more information, you can refer to the [dataset source](https://www.kaggle.com/datasets/subhajournal/phishingemails), and our EDA notebook `EDA.ipynb`.

## Features
Each email has the following features:
- `Email Text`: The content of the email.
- `Email Type`: The label indicating whether the email is phishing or legitimate.

Preprocessing will involve text cleaning, tokenization, and vectorization to convert the email text into a format suitable for classification models.

## Goal
The goal of this project is to answer this problematic: *Is it possible to deploy effective solutions to protect against phising by mail ?*

To achieve this, we will build a machine learning model that can accurately classify emails as phishing or legitimate based on their content. This involves preprocessing the email text, extracting features, and training a classification model.

This problematic is a real-world challenge in cybersecurity for growing companies that do not have the resources to hire a cybersecurity expert.

## Usage
To use this project, follow these steps:
1. If not already done, install the conda env
2. Create the `data/phishing_email_cleaned.csv` file by running the first part in the `EDA.ipynb` notebook.
3. Run the classification model in the `supervised.ipynb` notebook.

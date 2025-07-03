# FTML Project
This repository contains math and code for the Fondamentals of Machine Learning course at EPITA.

Each folder is a section of the project's content.

# Table of Contents
- [Sections](#sections)
- [Configuration](#configuration)

## Sections
1. Bayes estimator and Bayes risk
2. Bayes risk with absolute loss
3. Expected value of empirical risk for OLS
4. Regression on a given dataset
5. Classification on a given dataset
6. Application of supervised learning
7. Application of unsupervised learning

## Configuration
### Python Environment
There are two ways to set up the Python environment for this project: using `pip` or `conda`.

#### Using Conda
Set up the environment using Conda:
```
conda env create -f conda_env.yaml
```
Export the environment:
```
conda env export --name FTML > conda_env.yaml
```

#### Using Pip
Set up the environment using Pip:
```
pip install -r requirements.txt
```
Export the environment:
```
pip freeze > requirements.txt
```

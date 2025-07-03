# Supervised learning Summary
Each notebook is a self-contained example of supervised learning applications.

For more detail, please refer to the individual notebooks for evaluation metrics, and exploration steps.

## Exploration

### Text preprocessing
Initially, we cleaned anything that was not a word: numbers, punctuation, and special characters. We also converted all text to lowercase to ensure uniformity.

We observed that the training did not differ much in most models, and the performance was slightly worse than the original dataset. We assumed that phishing emails might contain many parasitic words that make them stand out, and removing them could potentially reduce the model's ability to detect phishing emails effectively.

Therefore, we decided to keep the text as it is without further preprocessing.

### Dataset imbalance
The number of phishing emails is significantly lower than the number of legitimate emails. This imbalance can lead to models that are biased towards predicting legitimate emails more often.

Each model has a way to address this issue, such as using class weights or `SMOTE` to balance the dataset. We applied these techniques and noticed that performances did not improve significantly. The models were already performing well, and the additional balancing did not yield better results, and in some cases, it even worsened the performance.

## Conclusion
Overall, the models performed well in detecting phishing emails. The choice of hyperparameters affected the performance, but the models were generally robust. The evaluation metrics showed that the models could effectively distinguish between phishing and legitimate emails.
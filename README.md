# Email Signature Extraction

.. image:: https://codecov.io/gh/harmening/signature_extraction/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/harmening/signature_extraction

Email Signature Extraction is a library for splitting email content into two parts: a human-written body and an automatically appended signature.

### Installation
Install required dependencies in a virtual environment:

 * pip install -r requirements.txt



## Approach
A combination of standart algorithms and machine learning techniques is used to detect and extract the signature part. This detection problem is converted into a binary classification task with 2 possible outcomes: `signature` (1) or `body` (0).
After preprocessing the email, its text is splitted into lines and each line is classified while taking previous and next lines into account as well. A subsequent algorithm is applied for grouping several continuous lines of ones (i.e. signatures) and extracting it from the email body.

This repo is organized as follows:


### Text preprocessing
Text preprocessing is the first step of the email segmentation process. Each input email is tokenized on sentence level, using the NLTK SentenceTokenizer. The F1-score significantly increased when applying this preprocessing step.

### Feature Extraction
SignatureFeatureExtractor is a custom scikit-learn transformer, which is applied for feature extraction.
It converts each line of text into a vector, also taking the previous and next line into account.
For each line, the algorithm looks for several features, that are considered to be an important information for a successful classification. There are for example: count of named entities, countaining typical signature words, email-addresses, phone numbers, urls, etc.
The NLTK named entity recognizer used to count entities in the text. 

### Classification
k-Nearest Neighbors (kNN) is a simple, effective and quite popular classification algorithm. After several experiments with different ML algorithms and tuning hyperparameters with GridSearchCV, kNN is chosen because of simplicity and effectiveness. kNN produced an F1 score of 0.95. However, other classification techniques such as LinearSVM also turned out to show good results.

### Evaluation
The evaluation is done based on the f1 metric, which is widely used for evaluating binary classification models:
`F1 = 2 * (precision * recall) / (precision + recall)`, where precision is a measure of result relevancy and recall is a measure of how many truly relevant results are returned. See also https://en.wikipedia.org/wiki/F1_score for more details.


### To Do
 * Find better solution for grouping lines of continuous signature. It is assumend that the longest repeating sequence of ones algorithm is going to fail for some edge cases.
 * Increase size of training data
 * Improve accuracy of classifier model
 * Experiment with Long short-term memory (LSTM) Recurrent Neural Networks (RNN).

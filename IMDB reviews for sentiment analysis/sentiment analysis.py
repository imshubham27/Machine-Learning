import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('dataset.csv', encoding='latin-1',error_bad_lines=False,)

txt_file=open("Accuracy.txt",'w')

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 25000):
    SentimentText = re.sub('[^a-zA-Z]', ' ', dataset['SentimentText'][i])
    SentimentText = SentimentText.lower()
    SentimentText = SentimentText.split()
    ps = PorterStemmer()
    SentimentText = [ps.stem(word) for word in SentimentText if not word in set(stopwords.words('english'))]
    SentimentText = ' '.join(SentimentText)
    corpus.append(SentimentText)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 450)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.350, random_state = 0)

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

from sklearn import metrics
txt_file.write(print("The accuracy of this NLP model is:{}".format(metrics.accuracy_score(y_test, y_pred))))
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer
import numpy as np

# Load Data
dataframe = pd.read_csv("spam.csv")
print(dataframe.describe())
dataframe = dataframe.sample(frac = 1)

# Split Test & Training

x = dataframe["EmailText"]
y = dataframe["Label"]

x_train,y_train = x[0:4457],y[0:4457]
x_test,y_test = x[4457:],y[4457:]

# Feature Extraction
cv = CountVectorizer()
features = np.array(cv.fit_transform(x_train).toarray())

print("Running Model")

model=MultinomialNB()
model.fit(features,y_train) 
features_test=cv.transform(x_test)
print("Accuracy of Model",model.score(features_test,y_test)*100,"%") 

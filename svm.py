import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer

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
features = cv.fit_transform(x_train)

# Model 
# tuned_parameters = {'kernel': ['rbf','linear'], 'gamma': [1e-3, 1e-4], 'C': [1, 10, 100, 1000]}
tuned_parameters =   {'kernel': ['rbf','linear'],'gamma': ['auto']}

model = GridSearchCV(svm.SVC(), tuned_parameters)

model.fit(features,y_train)

print(model.best_params_)

# Show Accuracy
print(model.score(cv.transform(x_test),y_test))
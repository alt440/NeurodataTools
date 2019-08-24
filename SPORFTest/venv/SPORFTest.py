# the forest classifier that I want to test (rerf == sporf)
from rerf.rerfClassifier import rerfClassifier

# Import scikit-learn dataset library. Machine learning tool for python. Used here to get some data.
from sklearn import datasets

# Creating a DataFrame of given iris dataset. (I wonder if this is really useful?
import pandas as pd

# Import train_test_split function
from sklearn.model_selection import train_test_split

# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics


# iris contains all the data related to irises
iris = datasets.load_iris()

# to get the information out of the iris dataset
# print(iris.target_names)
# print(iris.feature_names)

# The reason I am using Panda is because it seems to be useful to see the data better.
# Using Panda, when you print out, you see the columns' signification and the rows' number.
data = pd.DataFrame(
    {
        "sepal length": iris.data[:, 0],
        "sepal width": iris.data[:, 1],
        "petal length": iris.data[:, 2],
        "petal width": iris.data[:, 3],
        "species": iris.target,
    }
)

# Prints the first 5 lines of data
print(data.head())

# extracting some data
# this takes all the data relating only to the 4 columns sepal length, width, petal length, width
X = data[["sepal length", "sepal width", "petal length", "petal width"]]  # Features
# this takes all the data relating to the species column. Note: there is no double square brackets here, because
# we are not adding the title of the column to it. You can print y and X to see for yourself.
y = data["species"]  # Labels

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3
)  # 70% training and 30% test

# Create a RerF Classifier
clf = rerfClassifier(n_estimators=100)

# Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train, y_train)

# so we predict where the X data is supposed to go (which species is the X element from?)
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
import math

# Our forest classifier SPORF (also called Rerf)
from rerf.rerfClassifier import rerfClassifier

# Import scikit-learn dataset library
from sklearn import datasets

# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html
from scipy.stats import mannwhitneyu

# testing sklearn random forest
from sklearn.ensemble import RandomForestClassifier

# tqdm is used as the loading bar in linux
from tqdm import tqdm

# Load dataset
iris = datasets.load_iris()


def iris_pred_acc(cls, n_iter=10000):
    y_train_acc_list = []
    for i in tqdm(range(n_iter)):
        clf.fit(iris.data, iris.target)
        y_pred_train = clf.predict(iris.data)
        y_train_acc_list.append(metrics.accuracy_score(iris.target, y_pred_train))

    return y_train_acc_list


def print_pred_summ(acc_list):
    print(sum([math.isclose(yt, 1) for yt in acc_list]))
    # print("avg acc", sum(y_train_acc_list)/len(y_train_acc_list))
    print(sorted(acc_list)[0:5])


def two_sided_mannwhitneyu(x,y):
    u, prob_one_sided = mannwhitneyu(x, y, use_continuity=False)
    prob = prob_one_sided*2

    return u, prob


# RerF classifier test
clf = rerfClassifier(n_estimators=100, projection_matrix="RerF")
rerf_acc = iris_pred_acc(clf, 10000)
print("RerF")
print_pred_summ(rerf_acc)

# Random Forest classifier test (the one of Neurodata)
clf = rerfClassifier(n_estimators=100, projection_matrix="Base")
rf_acc = iris_pred_acc(clf, 10000)
print("RF")
print_pred_summ(rf_acc)

# Random Forest classifier test (the one of sklearn)
clf = RandomForestClassifier(n_estimators=100)
sklearn_acc = iris_pred_acc(clf, 10000)
print("sklearn")
print_pred_summ(sklearn_acc)

_, prob_rerf_rf = two_sided_mannwhitneyu(rerf_acc, rf_acc)
_, prob_rerf_sklearn = two_sided_mannwhitneyu(rerf_acc, sklearn_acc)
_, prob_rf_sklearn = two_sided_mannwhitneyu(rf_acc, sklearn_acc)

print("RerF vs. RF:      p={prob_rerf_rf:0.10f}")
print("RerF vs. sklearn: p={prob_rerf_sklearn:0.10f}")
print("RF vs. sklearn:   p={prob_rf_sklearn:0.10f}")


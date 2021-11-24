import numpy as np
from numpy import mean
from numpy import std
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix



def train_rf_with_cv(X, Y, model_name):
    # define the model
    model = RandomForestClassifier()
    # evaluate the model
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    compute_score_cv(model, X, Y, cv=cv)
    # n_scores = cross_val_score(model, X, Y, scoring='f1', cv=cv, n_jobs=-1, error_score='raise')
    # print('Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))


def train_rf_with_independent_test_data(X, Y, model_name):
    # implementing train-test-split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=66)
    # random forest model creation
    rfc = RandomForestClassifier()
    rfc.fit(X_train, y_train)
    # predictions
    rfc_predict = rfc.predict(X_test)

    print("=== Confusion Matrix ===")
    print(confusion_matrix(y_test, rfc_predict))
    print('\n')
    print("=== Classification Report ===")
    print(classification_report(y_test, rfc_predict))
    print('\n')


def compute_score_cv(model, X, Y, cv):
    scoring_strings = ['accuracy', 'precision', 'recall', 'f1',
                       'average_precision', 'roc_auc']
    for scoring in scoring_strings:
        n_scores = cross_val_score(model, X, Y, scoring=scoring, cv=cv, n_jobs=-1, error_score='raise')
        print('%20s: %.3f +- %.3f' % (scoring,
                                      np.mean(n_scores),
                                      np.std(n_scores)))

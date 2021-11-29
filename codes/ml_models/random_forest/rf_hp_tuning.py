from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
from pprint import pprint


def get_random_hyper_parameter_grid():
    # Number of trees in random forest
    n_estimators = [int(x) for x in np.linspace(start=100, stop=1000, num=10)]
    # Number of features to consider at every split
    max_features = ['auto', 'sqrt']
    # Maximum number of levels in tree
    max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
    max_depth.append(None)
    # Minimum number of samples required to split a node
    min_samples_split = [2, 5, 10]
    # Minimum number of samples required at each leaf node
    min_samples_leaf = [1, 2, 4]
    # Method of selecting samples for training each tree
    bootstrap = [True, False]
    # Create the random grid
    random_grid = {'n_estimators': n_estimators,
                   'max_features': max_features,
                   'max_depth': max_depth,
                   'min_samples_split': min_samples_split,
                   'min_samples_leaf': min_samples_leaf,
                   'bootstrap': bootstrap}

    pprint(random_grid)
    # On each iteration, the algorithm will choose a difference combination of the features. Altogether,
    # there are 2 * 12 * 2 * 3 * 3 * 10 = 4320 settings!
    return random_grid


def random_search_training(random_hyper_parameter_grid, x_train, y_train):
    # Use the random grid to search for best hyper parameters
    # First create the base model to tune
    rf = RandomForestClassifier()
    # Random search of parameters, using 10 fold cross validation,
    # search across 100 different combinations, and use all available scores

    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=1, random_state=1)

    rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_hyper_parameter_grid,
                                   n_iter=100,
                                   cv=cv,
                                   verbose=2,
                                   scoring=['accuracy', 'precision', 'f1', 'recall', 'roc_auc'],
                                   refit='roc_auc',
                                   return_train_score=True,
                                   random_state=42,
                                   n_jobs=-1)
    # Fit the random search model
    rf_random.fit(x_train, y_train)

    pprint("rf_random: \n")
    pprint(rf_random)

    pprint("rf_random.best_estimator_: \n")
    pprint(rf_random.best_estimator_)

    pprint("rf_random.best_params_: \n")
    pprint(rf_random.best_params_)

    pprint("rf_random.best_score_: \n")
    pprint(rf_random.best_score_)

    pprint("rf_random.best_index_: \n")
    pprint(rf_random.best_index_)

    pprint("rf_random.scorer_: ")
    pprint(rf_random.scorer_)

    pprint("rf_random.scoring: ")
    pprint(rf_random.scoring)

    pprint("rf_random.cv_results_: ")
    pprint(rf_random.cv_results_)

    return rf_random


def evaluate(model, x_test, y_test):
    predictions = model.predict(x_test)
    print('Model Performance')
    print('\n')
    print("=== Confusion Matrix ===")
    print(confusion_matrix(y_test, predictions))
    print('\n')
    print("=== Classification Report ===")
    class_report = classification_report(y_test, predictions)
    print(class_report)
    return class_report


def grid_search_model_training(param_grid, x_train, y_train):
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    # Create a based model
    rf = RandomForestClassifier()
    # Instantiate the grid search model
    grid_search_model = GridSearchCV(estimator=rf, param_grid=param_grid,
                                     cv=cv, n_jobs=-1, verbose=2)
    grid_search_model.fit(x_train, y_train)

    pprint("grid_search_model: \n")
    pprint(grid_search_model)

    pprint("grid_search_model.best_estimator_: \n")
    pprint(grid_search_model.best_estimator_)

    pprint("grid_search_model.best_params_: \n")
    pprint(grid_search_model.best_params_)

    pprint("grid_search_model.best_score_: \n")
    pprint(grid_search_model.best_score_)

    pprint("grid_search_model.best_index_: \n")
    pprint(grid_search_model.best_index_)

    return grid_search_model

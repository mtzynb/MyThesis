from pprint import pprint
from sklearn.svm import SVC
import numpy as np
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix


def get_random_hyper_parameter_grid():
    kernel = ['rbf']
    # kernel = ['sigmoid']
    gamma = ['scale', 'auto']
    # c_range = [1]
    c_range = [x for x in np.logspace(-9, 3, 13)]

    # Create the random grid
    random_grid = {'kernel': kernel,
                   'gamma': gamma,
                   'C': c_range}
    pprint(random_grid)

    return random_grid


def grid_search_model_training(param_grid, x_train, y_train):
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=1, random_state=1)
    # Instantiate the grid search model
    grid_search_model = GridSearchCV(estimator=SVC(), param_grid=param_grid,
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

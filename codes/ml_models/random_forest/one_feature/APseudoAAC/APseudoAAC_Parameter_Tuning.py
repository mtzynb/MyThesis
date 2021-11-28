from codes.tsv_file_utils import get_data_frame_from_tsv_file
import codes.utility as utility
import codes.ml_models.random_forest.rf_tune_hyperparameters as rf_hpt
from pprint import pprint
import time

# -------------- X ---------------------
APseudoAAC_90 = '../../../../../pca_features/round3/one_fearure/APseudoAAC/APseudoAAC_90_mixed_pca.tsv'
APseudoAAC_80 = '../../../../../pca_features/round3/one_fearure/APseudoAAC/APseudoAAC_80_mixed_pca.tsv'
# -------------- Y ---------------------
label_90 = '../../../../../pca_features_label/round3/one_fearure/APseudoAAC/APseudoAAC_90_mixed_pca_label.tsv'
label_80 = '../../../../../pca_features_label/round3/one_fearure/APseudoAAC/APseudoAAC_80_mixed_pca_label.tsv'
# ------------------------- random hyper param grid -------------------------
random_hyper_param_grid = rf_hpt.get_random_hyperparameter_grid()
# ------------------------- get dfs -------------------------
APseudoAAC_90_X = get_data_frame_from_tsv_file(APseudoAAC_90)
APseudoAAC_90_X = APseudoAAC_90_X.iloc[:, 1:11]
# print(APseudoAAC_90_X)

label_90_Y = get_data_frame_from_tsv_file(label_90)
label_90_Y = label_90_Y.iloc[:, 1]
# print(label_90_Y)
# ------------------------- hyperparameter tuning 1 -------------------------
x90_train, x90_test, y90_train, y90_test = utility.split_test_train(APseudoAAC_90_X, label_90_Y)
print(x90_test)

# print("x90_train: ", len(x90_train))
# print("x90_test: ", len(x90_test))
# print("y90_train: ", len(y90_train))
# print("y90_test: ", len(y90_test))
#
# start = time.time()
# rf_random_model = rf_hpt.random_search_training(random_hyperparameter_grid=random_hyper_param_grid, x_train=x90_train,
#                                                 y_train=y90_train)
#
# rf_hpt.evaluate(rf_random_model.best_estimator_, x90_test, y90_test)
# end = time.time()
# utility.save_model("rf_hp1_model.sav", rf_random_model.best_estimator_)
# pprint("model saved.")
#
# print("The time of execution of above program is :", end - start)

# ------------------------- hyperparameter tuning 1 End -------------------------


# start = time.time()
from sklearn.model_selection import GridSearchCV

# Create the parameter grid based on the results of above random search
# {'n_estimators': 200, 'min_samples_split': 5, 'min_samples_leaf': 1,
# 'max_features': 'sqrt', 'max_depth': 100, 'bootstrap': True}

# param_grid = {
#     'bootstrap': [True],
#     'max_depth': [100, 200, 300],
#     'max_features': ['sqrt'],
#     'min_samples_leaf': [1, 2, 3],
#     'min_samples_split': [4, 6],
#     'n_estimators': [100, 200, 300]
# }
#
# rf_grid_model = rf_hpt.grid_search_model_training(param_grid, x90_train, y90_train)
# rf_hpt.evaluate(rf_grid_model.best_estimator_, x90_test, y90_test)
# end = time.time()
# print("The time of execution of above program is :", end - start)
# utility.save_model("rf_hp2_model.sav", rf_grid_model.best_estimator_)
# pprint("model saved.")

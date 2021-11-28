from codes.tsv_file_utils import get_data_frame_from_tsv_file
import codes.utility as utility
import codes.ml_models.random_forest.rf_tune_hyperparameters as rf_hpt
from pprint import pprint
import time
import codes.plot_rf_model as plot_rf

# -------------- X,Y ---------------------
CKSAAP_90 = '../../../../../pca_features/round3/one_fearure/CKSAAP/CKSAAP_90_mixed_pca.tsv'
label_90 = '../../../../../pca_features_label/round3/one_fearure/CKSAAP/CKSAAP_90_mixed_pca_label.tsv'
# ------------------------- random hyper param grid -------------------------
random_hyper_param_grid = rf_hpt.get_random_hyperparameter_grid()
# ------------------------- get dfs -------------------------
CKSAAP_90_X = get_data_frame_from_tsv_file(CKSAAP_90)
CKSAAP_90_X = CKSAAP_90_X.iloc[:, 1:11]

label_90_Y = get_data_frame_from_tsv_file(label_90)
label_90_Y = label_90_Y.iloc[:, 1]
# print(label_90_Y)
# ------------------------- hyperparameter tuning 1 -------------------------
x90_train, x90_test, y90_train, y90_test = utility.split_test_train(CKSAAP_90_X, label_90_Y)
print(x90_test)

print("x90_train: ", len(x90_train))
print("x90_test: ", len(x90_test))
print("y90_train: ", len(y90_train))
print("y90_test: ", len(y90_test))

start = time.time()
rf_random_model = rf_hpt.random_search_training(random_hyperparameter_grid=random_hyper_param_grid, x_train=x90_train,
                                                y_train=y90_train)

print("rf_random_model.best_estimator_: ")
pprint(rf_random_model.best_estimator_)
rf_hpt.evaluate(rf_random_model.best_estimator_, x90_test, y90_test)
print("The time of execution of above program is :", time.time() - start)
plot_rf.plot_rf_model(rf_random_model.cv_results_, scoring=rf_random_model.scoring)

utility.save_model("CKSAAP_rf_hp1_model_1.sav", rf_random_model.best_estimator_)
pprint("model saved.")

# ------------------------- hyperparameter tuning 1 End -------------------------


# start = time.time()
from sklearn.model_selection import GridSearchCV

# Create the parameter grid based on the results of above random search
# {'bootstrap': True,'max_depth': 50,'max_features': 'sqrt','min_samples_leaf': 1,
# 'min_samples_split': 2,'n_estimators': 100}


# rf_grid_model = rf_hpt.grid_search_model_training(param_grid, x90_train, y90_train)
# rf_hpt.evaluate(rf_grid_model.best_estimator_, x90_test, y90_test)
# end = time.time()
# print("The time of execution of above program is :", end - start)
# utility.save_model("rf_hp2_model.sav", rf_grid_model.best_estimator_)
# pprint("model saved.")

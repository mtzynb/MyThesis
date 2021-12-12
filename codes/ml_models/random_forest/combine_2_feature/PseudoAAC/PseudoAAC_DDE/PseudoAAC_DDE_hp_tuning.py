from codes.tsv_file_utils import get_data_frame_from_tsv_file
import codes.utility as utility
import codes.ml_models.random_forest.rf_hp_tuning as rf_hpt
from pprint import pprint
import time
import codes.ml_models.random_forest.rf_model_plot as plot_rf
import codes.ml_models.random_forest.rf_model_log as model_result_rf

start_main = time.time()
# -------------- X,Y ---------------------
pca_features_90 = '../../../../../../pca_features/round3/combined_features/combine_2/PseudoAAC/PseudoAAC_DDE/PseudoAAC_DDE_90_mixed_pca.tsv'
label_90 = '../../../../../../pca_features/round3/combined_features/combine_2/PseudoAAC/PseudoAAC_DDE/pca_feature_labels.tsv'
# ------------------------- random hyper param grid -------------------------
random_hyper_param_grid = rf_hpt.get_random_hyper_parameter_grid()
# ------------------------- get dfs -------------------------
pca_features_90_X = get_data_frame_from_tsv_file(pca_features_90)
pca_features_90_X = pca_features_90_X.iloc[:, 1:11]

label_90_Y = get_data_frame_from_tsv_file(label_90)
label_90_Y = label_90_Y.iloc[:, 1]
# ------------------------- hyper parameter tuning 1 -------------------------
x90_train, x90_test, y90_train, y90_test = utility.split_test_train(pca_features_90_X, label_90_Y)
print(x90_test)

print("x90_train: ", len(x90_train))
print("x90_test: ", len(x90_test))
print("y90_train: ", len(y90_train))
print("y90_test: ", len(y90_test))

start = time.time()
rf_random_model = rf_hpt.random_search_training(random_hyper_parameter_grid=random_hyper_param_grid,
                                                x_train=x90_train,
                                                y_train=y90_train)
end_hp_time = time.time() - start
pprint("hyper parameter tuning took: %s sec" % end_hp_time)
print("rf_random_model.best_estimator_: ")
pprint(rf_random_model.best_estimator_)
rf_hpt.evaluate(rf_random_model.best_estimator_, x90_test, y90_test)
# ------------------------- save state -------------------------
plot_rf.plot_rf_model(rf_random_model.cv_results_, scoring=rf_random_model.scoring,
                      figname="PseudoAAC_DDE_rf_after_hp1_plot.png")
pprint("model fig saved.")

utility.save_model("PseudoAAC_DDE_rf_after_hp1_best_model.sav", rf_random_model.best_estimator_)
pprint("model saved.")

model_result_rf.rf_model_log("PseudoAAC_DDE_rf_after_hp1_model_log.txt",
                             rf_random=rf_random_model,
                             best_estimator_=rf_random_model.best_estimator_,
                             best_params_=rf_random_model.best_params_,
                             best_score_=rf_random_model.best_score_,
                             best_index_=rf_random_model.best_index_,
                             scorer_=rf_random_model.scorer_,
                             scoring=rf_random_model.scoring,
                             cv_results_=rf_random_model.cv_results_,
                             execution_time=end_hp_time)
pprint("model log saved.")
print("whole script execution time: %s sec" % (time.time() - start_main))
# ------------------------- hyperparameter tuning 1 End -------------------------


# start = time.time()

# Create the parameter grid based on the results of above random search
# {'bootstrap': True,'max_depth': 50,'max_features': 'sqrt','min_samples_leaf': 1,
# 'min_samples_split': 2,'n_estimators': 100}


# rf_grid_model = rf_hpt.grid_search_model_training(param_grid, x90_train, y90_train)
# rf_hpt.evaluate(rf_grid_model.best_estimator_, x90_test, y90_test)
# end = time.time()
# print("The time of execution of above program is :", end - start)
# utility.save_model("rf_hp2_model.sav", rf_grid_model.best_estimator_)
# pprint("model saved.")

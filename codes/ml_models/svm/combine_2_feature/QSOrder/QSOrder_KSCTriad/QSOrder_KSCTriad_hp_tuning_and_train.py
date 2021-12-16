from codes.tsv_file_utils import get_data_frame_from_tsv_file
import codes.utility as utility
import codes.ml_models.svm.svm_hp_tuning as svm_hpt
from pprint import pprint
import time
import codes.ml_models.svm.svm_model_log as model_result_log
import codes.ml_models.svm.svm_classifier as svm_classifier

start_main = time.time()
# -------------- X,Y ---------------------
pca_features_90 = '../../../../../../pca_features/round3/combined_features/combine_2/QSOrder/QSOrder_KSCTriad/QSOrder_KSCTriad_90_mixed_pca.tsv'
label_90 = '../../../../../../pca_features/round3/combined_features/combine_2/QSOrder/QSOrder_KSCTriad/pca_feature_labels.tsv'
# ------------------- random hyper param grid ---------------
random_hyper_param_grid = svm_hpt.get_random_hyper_parameter_grid()
# ------------------------- get dfs -------------------------
pca_features_90_X = get_data_frame_from_tsv_file(pca_features_90)
pca_features_90_X = pca_features_90_X.iloc[:, 1:11]

label_90_Y = get_data_frame_from_tsv_file(label_90)
label_90_Y = label_90_Y.iloc[:, 1]
# -------------------------- train test split -------------------
x90_train, x90_test, y90_train, y90_test = utility.split_test_train(pca_features_90_X, label_90_Y)
print("x90_train: ", len(x90_train))
print("x90_test: ", len(x90_test))
print("y90_train: ", len(y90_train))
print("y90_test: ", len(y90_test))
# ------------------ hyper parameter tuning 1 -------------------
start = time.time()
svm_random_model = svm_hpt.grid_search_model_training(
    param_grid=random_hyper_param_grid,
    x_train=x90_train,
    y_train=y90_train)

end_hp_time = time.time() - start
pprint("hyper parameter tuning took: %s sec" % end_hp_time)
print("svm_random_model.best_estimator_: ")
pprint(svm_random_model.best_estimator_)
svm_hpt.evaluate(svm_random_model.best_estimator_, x90_test, y90_test)
# ------------------------- save state -------------------------
utility.save_model("QSOrder_KSCTriad_svm_after_hp1_best_model.sav", svm_random_model.best_estimator_)
pprint("model saved.")

model_result_log.svm_model_log("QSOrder_KSCTriad_svm_after_hp1_model_log.txt",
                               svm_random=svm_random_model,
                               best_estimator_=svm_random_model.best_estimator_,
                               best_params_=svm_random_model.best_params_,
                               best_score_=svm_random_model.best_score_,
                               best_index_=svm_random_model.best_index_,
                               scorer_=svm_random_model.scorer_,
                               scoring=svm_random_model.scoring,
                               cv_results_=svm_random_model.cv_results_,
                               execution_time=end_hp_time)
pprint("model log saved.")
print("whole script execution time: %s sec" % (time.time() - start_main))

# --------------- train svm based on best params on whole train data ---------------------
start = time.time()
svm_model_train = svm_classifier.train_predict_log(x_train=x90_train,
                                                   y_train=y90_train,
                                                   x_test=x90_test,
                                                   y_test=y90_test,
                                                   params=svm_random_model.best_params_,
                                                   log_filename='QSOrder_KSCTriad_svm_rbf_eval_after_test_log.txt')
# --------------------------------------------------
utility.save_model("QSOrder_KSCTriad_svm_rbf_model_train.sav", svm_model_train)
print("model saved.")
# --------------------------------------------------
print("whole script run took %s seconds." % (time.time() - start))

from codes.tsv_file_utils import get_data_frame_from_tsv_file
import codes.utility as utility
import codes.ml_models.random_forest.random_forest as rf
import codes.utility
import time

# -------------- X, Y---------------------
APseudoAAC_90 = '../../../../../pca_features/round3/one_fearure/APseudoAAC/APseudoAAC_90_mixed_pca.tsv'
label_90 = '../../../../../pca_features_label/round3/one_fearure/APseudoAAC/APseudoAAC_90_mixed_pca_label.tsv'
# ------------------------- get dfs -------------------------
APseudoAAC_90_X = get_data_frame_from_tsv_file(APseudoAAC_90)
APseudoAAC_90_X = APseudoAAC_90_X.iloc[:, 1:11]

label_90_Y = get_data_frame_from_tsv_file(label_90)
label_90_Y = label_90_Y.iloc[:, 1]
# --------------------------------------------------
x90_train, x90_test, y90_train, y90_test = utility.split_test_train(APseudoAAC_90_X, label_90_Y)

# params = {'n_estimators': 200, 'min_samples_split': 5, 'min_samples_leaf': 1,
#           'max_features': 'sqrt', 'max_depth': 100, 'bootstrap': True}
# # --------------------------------------------------
# start = time.time()
# rfc_model = rf.train_rf_classifier(x_train=x90_train, y_train=y90_train, params=params)
# utility.save_model("rf_main90_model.sav", rfc_model)
# print("model saved.")
# end = time.time()
# print("The time of execution of above program is :", end - start)

rfc_model = utility.load_model("rf_main90_model_80acc.sav")
rf.evaluate(rfc_model, x_test=x90_test, y_test=y90_test)

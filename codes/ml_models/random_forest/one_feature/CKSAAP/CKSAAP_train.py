from codes.tsv_file_utils import get_data_frame_from_tsv_file
import codes.utility as utility
import codes.ml_models.random_forest.random_forest as rf
import time

# -------------- X, Y---------------------
CKSAAP_90 = '../../../../../pca_features/round3/one_fearure/CKSAAP/CKSAAP_90_mixed_pca.tsv'
label_90 = '../../../../../pca_features_label/round3/one_fearure/CKSAAP/CKSAAP_90_mixed_pca_label.tsv'
# ------------------------- get dfs -------------------------
CKSAAP_90_X = get_data_frame_from_tsv_file(CKSAAP_90)
CKSAAP_90_X = CKSAAP_90_X.iloc[:, 1:11]

label_90_Y = get_data_frame_from_tsv_file(label_90)
label_90_Y = label_90_Y.iloc[:, 1]
# --------------------------------------------------
x90_train, x90_test, y90_train, y90_test = utility.split_test_train(CKSAAP_90_X, label_90_Y)

params = {'bootstrap': True, 'max_depth': 50, 'max_features': 'sqrt', 'min_samples_leaf': 1,
          'min_samples_split': 2, 'n_estimators': 100}
# # # --------------------------------------------------
start = time.time()
rfc_model = rf.train_rf_classifier(x_train=x90_train, y_train=y90_train, params=params)
utility.save_model("CKSAAP_rf_main90_model.sav", rfc_model)
print("model saved.")
end = time.time()
print("The time of execution of above program is :", end - start)

# rfc_model = utility.load_model("CKSAAP_rf_main90_model_79acc.sav")
# rf.evaluate(rfc_model, x_test=x90_test, y_test=y90_test)

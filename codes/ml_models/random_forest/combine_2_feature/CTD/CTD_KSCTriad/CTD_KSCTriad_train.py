from codes.tsv_file_utils import get_data_frame_from_tsv_file
import codes.utility as utility
import codes.ml_models.random_forest.random_forest as rf
import time

# -------------- X, Y---------------------
pca_features_90 = '../../../../../../pca_features/round3/combined_features/combine_2/CTD/CTD_KSCTriad/CTD_KSCTriad_90_mixed_pca.tsv'
label_90 = '../../../../../../pca_features/round3/combined_features/combine_2/CTD/CTD_KSCTriad/pca_feature_labels.tsv'
# ------------------------- get dfs -------------------------
pca_features_90_X = get_data_frame_from_tsv_file(pca_features_90)
pca_features_90_X = pca_features_90_X.iloc[:, 1:11]

label_90_Y = get_data_frame_from_tsv_file(label_90)
label_90_Y = label_90_Y.iloc[:, 1]
# --------------------------------------------------
x90_train, x90_test, y90_train, y90_test = utility.split_test_train(pca_features_90_X, label_90_Y)

params = {'n_estimators': 500, 'min_samples_split': 2,
          'min_samples_leaf': 1, 'max_features': 'sqrt',
          'max_depth': 110, 'bootstrap': True}


# # # --------------------------------------------------
start = time.time()
rfc_model = rf.train_rf_classifier(x_train=x90_train, y_train=y90_train, params=params)
utility.save_model("CTD_KSCTriad_rfmodel_train.sav", rfc_model)
print("model saved.")
end = time.time()
print("rf train model took %s seconds." % (end - start))

rf.evaluate_and_log(rfc_model,
                    x_test=x90_test, y_test=y90_test,
                    log_filename="CTD_KSCTriad_rfeval_after_test_log.txt")

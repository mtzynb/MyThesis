from codes.tsv_file_utils import get_data_frame_from_tsv_file
import codes.utility as utility
import codes.ml_models.random_forest.random_forest as rf
import time

start_main = time.time()
# --------------------------------------------------
sfs_model_result_file = '../../../../feature_selection/wrapper_methods/200_features/200_combined_90_model.sav'
# -------------- X,Y ---------------------
combined_90 = '../../../../../dropped_duplication_features/round3/combine_features/7features_combined_90_mixed_normalized_drpdup.tsv'
label_90 = '../../../../../dropped_duplication_features/round3/combine_features/7features_combined_90_mixed_normalized_drpdup_label.tsv'
# ------------------------- get dfs -------------------------
combined_90_X = get_data_frame_from_tsv_file(combined_90)
combined_90_X = combined_90_X.iloc[:, 1:3015]

label_90_Y = get_data_frame_from_tsv_file(label_90)
label_90_Y = label_90_Y.iloc[:, 1]
# ------------------------- hyper parameter tuning 1 -------------------------
x90_train, x90_test, y90_train, y90_test = utility.split_test_train(combined_90_X, label_90_Y)
print(x90_test)

print("x90_train: ", len(x90_train))
print("x90_test: ", len(x90_test))
print("y90_train: ", len(y90_train))
print("y90_test: ", len(y90_test))
# ------------------get selected features--------------------------------
sfs = utility.load_model(sfs_model_result_file)
print('\nsubsets_')
print(sfs.subsets_)

print('k_feature_idx_')
print(sfs.k_feature_idx_)
print(list(sfs.k_feature_idx_))
selected_idx = list(sfs.k_feature_idx_)
print(len(selected_idx))

print('k_feature_names_')
print(sfs.k_feature_names_)

print('CV Score:')
print(sfs.k_score_)
# --------------------------------------------------
X_train_sfs = x90_train.iloc[:, selected_idx]
X_test_sfs = x90_test.iloc[:, selected_idx]
print(X_train_sfs)
# --------------------------------------------------
params = {'n_estimators': 200,
          'min_samples_split': 5,
          'min_samples_leaf': 1,
          'max_features': 'sqrt',
          'max_depth': 100,
          'bootstrap': True}

# # # --------------------------------------------------
start = time.time()
rfc_model = rf.train_rf_classifier(x_train=X_train_sfs, y_train=y90_train, params=params)
utility.save_model("200_sfs_rf_model_train.sav", rfc_model)
print("model saved.")
end = time.time()
print("rf train model took %s seconds." % (end - start))

rf.evaluate_and_log(rfc_model,
                    x_test=X_test_sfs, y_test=y90_test,
                    log_filename="200_sfs_rf_eval_after_test_log.txt")

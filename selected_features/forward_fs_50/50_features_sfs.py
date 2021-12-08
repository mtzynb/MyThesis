from codes.df_utils import save_df_to_pkl, load_pkl_to_df
import codes.utility as utility
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# --------------------------------------------------
sfs_model_result_file = '../../codes/feature_selection/wrapper_methods/100_features/100_combined_90_model.sav'
# --------------------------------------------------
# -------------- X,Y ---------------------
combined_90 = '../../dropped_duplication_features/round3/combine_features/7features_combined_90_mixed_normalized_drpdup.tsv'
label_90 = '../../dropped_duplication_features/round3/combine_features/7features_combined_90_mixed_normalized_drpdup_label.tsv'
# ------------------------- get dfs -------------------------
combined_90_X = get_data_frame_from_tsv_file(combined_90)
combined_90_X = combined_90_X.iloc[:, 1:3015]

label_90_Y = get_data_frame_from_tsv_file(label_90)
label_90_Y = label_90_Y.iloc[:, 1]
# --------------------------------------------------
x90_train, x90_test, y90_train, y90_test = utility.split_test_train(combined_90_X, label_90_Y)
print(x90_test)
print("x90_train: ", len(x90_train))
print("x90_test: ", len(x90_test))
print("y90_train: ", len(y90_train))
print("y90_test: ", len(y90_test))
# --------------------------------------------------
sfs = utility.load_model(sfs_model_result_file)
print('\nsubsets_')
print(sfs.subsets_)

print('k_feature_idx_')
print(sfs.k_feature_idx_)
print(len(sfs.k_feature_idx_))

print('k_feature_names_')
print(sfs.k_feature_names_)

print('CV Score:')
print(sfs.k_score_)
# # --------------------------------------------------
# X_train_sfs = x90_train[:, sfs.k_feature_idx_]
# X_test_sfs = x90_test[:, sfs.k_feature_idx_]
#
# # --------------------------------------------------
# write_data_frame_to_tsv_file(X_train_sfs, '50_sfs_mixed_normalized_90_drpdup_train.tsv')
# write_data_frame_to_tsv_file(X_train_sfs, '50_sfs_mixed_normalized_90_drpdup_train_label.tsv')
#
# write_data_frame_to_tsv_file(y_90, '50_sfs_mixed_normalized_90_drpdup_test.tsv')
# write_data_frame_to_tsv_file(X_test_sfs, '50_sfs_mixed_normalized_90_drpdup_test.tsv')
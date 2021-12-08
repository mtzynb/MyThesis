from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from codes.tsv_file_utils import get_data_frame_from_tsv_file
from codes.df_utils import save_df_to_pkl, load_pkl_to_df
import plot_wrapper_f_selection as plot_fsf
import codes.utility as utility
import pandas as pd
import time

# --------------------------------------------------
start_main = time.time()
# -------------- X,Y ---------------------
combined_90 = '../../../dropped_duplication_features/round3/combine_features/7features_combined_90_mixed_normalized_drpdup.tsv'
label_90 = '../../../dropped_duplication_features/round3/combine_features/7features_combined_90_mixed_normalized_drpdup_label.tsv'
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
lr_model = LogisticRegression()
# --------------------------------------------------
sfs = SFS(lr_model,
          k_features=(1, 200),
          forward=True,
          floating=False,
          scoring='accuracy',
          verbose=2,
          n_jobs=-1,
          cv=10)

start_fs = time.time()
sfs = sfs.fit(x90_train, y90_train)
end_fs = time.time() - start_fs

print("feature selection took: %s sec" % end_fs)
# ----------------log results---------------------------------
print('\nsubsets_')
print(sfs.subsets_)

print('k_feature_idx_')
print(sfs.k_feature_idx_)

print('k_feature_names_')
print(sfs.k_feature_names_)

print('CV Score:')
print(sfs.k_score_)
# --------------------save model------------------------------
utility.save_model("200_combined_90_model.sav", sfs)
print("model saved.")
# --------------------save plot----------------------------
plot_fsf.plot_f_selection(sfs,
                          'Sequential Forward Selection (w. StdDev)',
                          '200_combined_90_sfs_plot.png')
print("plot saved.")
# --------------------save df results------------------------------
df = pd.DataFrame.from_dict(sfs.get_metric_dict()).T
save_df_to_pkl(df, '200_combined_90_df_result.pkl')
print("pkl saved.")
# --------------------------------------------------
print("whole script execution time: %s sec" % (time.time() - start_main))
# --------------------------------------------------
# sfs = utility.load_model("combined_90_model.sav")
# df = load_pkl_to_df('combined_90_df_result.pkl')
# pprint(df)

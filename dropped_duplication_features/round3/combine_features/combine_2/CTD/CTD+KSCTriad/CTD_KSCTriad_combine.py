from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file
import pandas as pd

# ------------ input files -------------
CTD_90 = '../../../../../../modify_features_column/round3/one_fearure/CTD/combine/combineCTD_90_mixed_normalized_modified_cols_name.tsv'
KSCTriad_90 = '../../../../../../modify_features_column/round3/one_fearure/KSCTriad/KSCTriad_90_mixed_normalized_modified_cols_name.tsv'
# ------------ output files -------------
combined_features_out = 'CTD_KSCTriad_combined_90_mixed_normalized.csv'
# ---------------------------------------
# get df from cdhit 90 data
CTD_90_df = get_data_frame_from_tsv_file(CTD_90)  # acc= 0.74
KSCTriad_90_df = get_data_frame_from_tsv_file(KSCTriad_90)  # acc= 0.77
# ---------------------------------------
# concat all features
combined_features_df = pd.concat([CTD_90_df,
                                  KSCTriad_90_df.iloc[:, 1:]]
                                 , axis=1)
# ---------------------------------------
write_data_frame_to_tsv_file(combined_features_df, combined_features_out)

print(combined_features_df.shape)  # (940, 960)

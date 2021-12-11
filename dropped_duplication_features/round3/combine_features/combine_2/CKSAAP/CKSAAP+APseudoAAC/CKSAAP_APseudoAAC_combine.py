from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file
import pandas as pd

# ------------ input files -------------

APseudoAAC_90 = '../../../../../../modify_features_column/round3/one_fearure/APseudoAAC/APseudoAAC_90_mixed_normalized_modified_cols_name.tsv'
CKSAAP_90 = '../../../../../../modify_features_column/round3/one_fearure/CKSAAP/CKSAAP_90_mixed_normalized_modified_cols_name.tsv'

# ------------ output files -------------
combined_features_out = 'CKSAAP_APseudoAAC_combined_90_mixed_normalized.csv'
# ---------------------------------------
# get df from cdhit 90 data
APseudoAAC_90_df = get_data_frame_from_tsv_file(APseudoAAC_90)  # acc= 0.79
CKSAAP_90_df = get_data_frame_from_tsv_file(CKSAAP_90)  # acc= 0.79
# ---------------------------------------
# concat all features
combined_features_df = pd.concat([CKSAAP_90_df,
                                  APseudoAAC_90_df.iloc[:, 1:]]
                                 , axis=1)
# ---------------------------------------
write_data_frame_to_tsv_file(combined_features_df, combined_features_out)

print(combined_features_df.shape)  # (940, 1629)

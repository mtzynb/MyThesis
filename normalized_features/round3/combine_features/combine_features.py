from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file
import pandas as pd

# ------------ input files -------------

APseudoAAC_90 = '../../../modify_features_column/round3/one_fearure/APseudoAAC/APseudoAAC_90_mixed_normalized_modified_cols_name.tsv'
CKSAAP_90 = '../../../modify_features_column/round3/one_fearure/CKSAAP/CKSAAP_90_mixed_normalized_modified_cols_name.tsv'
CTD_90 = '../../../modify_features_column/round3/one_fearure/CTD/combine/combineCTD_90_mixed_normalized_modified_cols_name.tsv'
DDE_90 = '../../../modify_features_column/round3/one_fearure/DDE/DDE_90_mixed_normalized_modified_cols_name.tsv'
KSCTriad_90 = '../../../modify_features_column/round3/one_fearure/KSCTriad/KSCTriad_90_mixed_normalized_modified_cols_name.tsv'
PseudoAAC_90 = '../../../modify_features_column/round3/one_fearure/PseudoAAC/PseudoAAC_90_mixed_normalized_modified_cols_name.tsv'
QSOrder_90 = '../../../modify_features_column/round3/one_fearure/QSOrder/QSOrder_90_mixed_normalized_modified_cols_name.tsv'

# ------------ output files -------------
combined_features_out = '7features_combined_90_mixed_normalized.csv'
# ---------------------------------------
# ged df from cdhit 90 data
APseudoAAC_90_df = get_data_frame_from_tsv_file(APseudoAAC_90)  # acc= 0.79
CKSAAP_90_df = get_data_frame_from_tsv_file(CKSAAP_90)  # acc= 0.79
CTD_90_df = get_data_frame_from_tsv_file(CTD_90)  # acc= 0.74
DDE_90_df = get_data_frame_from_tsv_file(DDE_90)  # acc= 0.74
KSCTriad_90_df = get_data_frame_from_tsv_file(KSCTriad_90)  # acc= 0.77
PseudoAAC_90_df = get_data_frame_from_tsv_file(PseudoAAC_90)  # acc= 0.79
QSOrder_90_df = get_data_frame_from_tsv_file(QSOrder_90)  # acc= 0.81
# ---------------------------------------
# concat all features
combined_features_df = pd.concat([QSOrder_90_df,
                                  APseudoAAC_90_df.iloc[:, 1:],
                                  CKSAAP_90_df.iloc[:, 1:],
                                  PseudoAAC_90_df.iloc[:, 1:],
                                  KSCTriad_90_df.iloc[:, 1:],
                                  CTD_90_df.iloc[:, 1:],
                                  DDE_90_df.iloc[:, 1:]]
                                 , axis=1)
# ---------------------------------------
# write_data_frame_to_tsv_file(combined_features_df, combined_features_out)

print(combined_features_df.shape) # (940, 3064)
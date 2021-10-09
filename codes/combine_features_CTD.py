import pandas as pd
import tsv_file_utils as tsv_file_utils

# ----------------- combine CTD features together ----------------------

# ------------ input files -------------

CTDC_train_100 = '../features/iFeature/round2/CTD/CTDC/CTDC_100_mixed_train.tsv'
CTDC_train_90 = '../features/iFeature/round2/CTD/CTDC/CTDC_90_mixed_train.tsv'
CTDC_train_80 = '../features/iFeature/round2/CTD/CTDC/CTDC_80_mixed_train.tsv'

CTDT_train_100 = '../features/iFeature/round2/CTD/CTDT/CTDT_100_mixed_train.tsv'
CTDT_train_90 = '../features/iFeature/round2/CTD/CTDT/CTDT_90_mixed_train.tsv'
CTDT_train_80 = '../features/iFeature/round2/CTD/CTDT/CTDT_80_mixed_train.tsv'

CTDD_train_100 = '../features/iFeature/round2/CTD/CTDD/CTDD_100_mixed_train.tsv'
CTDD_train_90 = '../features/iFeature/round2/CTD/CTDD/CTDD_90_mixed_train.tsv'
CTDD_train_80 = '../features/iFeature/round2/CTD/CTDD/CTDD_80_mixed_train.tsv'

# ------------ output files -------------
combineCTD_train_100 = '../features/iFeature/round2/CTD/combine/combineCTD_100_mixed_train.tsv'
combineCTD_train_90 = '../features/iFeature/round2/CTD/combine/combineCTD_90_mixed_train.tsv'
combineCTD_train_80 = '../features/iFeature/round2/CTD/combine/combineCTD_80_mixed_train.tsv'
# ---------------------------------------
# combine  C, T, D   cdhit100
CTDC_train_100_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDC_train_100)
CTDT_train_100_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDT_train_100)
CTDD_train_100_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDD_train_100)

combined_CTD_train100_df = pd.concat([CTDC_train_100_df, CTDT_train_100_df.iloc[:, 1:], CTDD_train_100_df.iloc[:, 1:]],
                                     axis=1)

tsv_file_utils.write_data_frame_to_tsv_file(combined_CTD_train100_df, combineCTD_train_100)
# ---------------------------------------
# combine  C, T, D   cdhit90
CTDC_train_90_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDC_train_90)
CTDT_train_90_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDT_train_90)
CTDD_train_90_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDD_train_90)

combined_CTD_train90_df = pd.concat([CTDC_train_90_df, CTDT_train_90_df.iloc[:, 1:], CTDD_train_90_df.iloc[:, 1:]],
                                    axis=1)

tsv_file_utils.write_data_frame_to_tsv_file(combined_CTD_train90_df, combineCTD_train_90)
# ---------------------------------------
# combine  C, T, D   cdhit80
CTDC_train_80_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDC_train_80)
CTDT_train_80_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDT_train_80)
CTDD_train_80_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDD_train_80)

combined_CTD_train80_df = pd.concat([CTDC_train_80_df, CTDT_train_80_df.iloc[:, 1:], CTDD_train_80_df.iloc[:, 1:]],
                                    axis=1)

tsv_file_utils.write_data_frame_to_tsv_file(combined_CTD_train80_df, combineCTD_train_80)

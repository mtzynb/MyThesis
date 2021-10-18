import pandas as pd
import tsv_file_utils as tsv_file_utils

# ----------------- combine CTD features together ----------------------

# ------------ input files -------------

CTDC_90 = '../features/iFeature/round3/CTD/CTDC/CTDC_90_mixed.tsv'
CTDC_80 = '../features/iFeature/round3/CTD/CTDC/CTDC_80_mixed.tsv'

CTDT_90 = '../features/iFeature/round3/CTD/CTDT/CTDT_90_mixed.tsv'
CTDT_80 = '../features/iFeature/round3/CTD/CTDT/CTDT_80_mixed.tsv'

CTDD_90 = '../features/iFeature/round3/CTD/CTDD/CTDD_90_mixed.tsv'
CTDD_80 = '../features/iFeature/round3/CTD/CTDD/CTDD_80_mixed.tsv'

# ------------ output files -------------
combineCTD_90 = '../features/iFeature/round3/CTD/combine/combineCTD_90_mixed.tsv'
combineCTD_80 = '../features/iFeature/round3/CTD/combine/combineCTD_80_mixed.tsv'
# ---------------------------------------
# combine  C, T, D   cdhit90
CTDC_90_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDC_90)
CTDT_90_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDT_90)
CTDD_90_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDD_90)

combined_CTD90_df = pd.concat([CTDC_90_df, CTDT_90_df.iloc[:, 1:], CTDD_90_df.iloc[:, 1:]],
                              axis=1)

tsv_file_utils.write_data_frame_to_tsv_file(combined_CTD90_df, combineCTD_90)
# ---------------------------------------
# combine  C, T, D   cdhit80
CTDC_80_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDC_80)
CTDT_80_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDT_80)
CTDD_80_df = tsv_file_utils.get_data_frame_from_tsv_file(CTDD_80)

combined_CTD80_df = pd.concat([CTDC_80_df, CTDT_80_df.iloc[:, 1:], CTDD_80_df.iloc[:, 1:]],
                              axis=1)

tsv_file_utils.write_data_frame_to_tsv_file(combined_CTD80_df, combineCTD_80)

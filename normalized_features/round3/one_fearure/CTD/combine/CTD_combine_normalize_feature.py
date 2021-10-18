from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------

combineCTD_90 = '../../../../../features/iFeature/round3/CTD/combine/combineCTD_90_mixed.tsv'
combineCTD_80 = '../../../../../features/iFeature/round3/CTD/combine/combineCTD_80_mixed.tsv'

# ------------ output files -------------
normalized_90 = 'combineCTD_90_mixed_normalized.tsv'
normalized_80 = 'combineCTD_80_mixed_normalized.tsv'
# ---------------------------------------
# normalize cdhit 90 train data
combineCTD_90_df = get_data_frame_from_tsv_file(combineCTD_90)
print(combineCTD_90_df)
normalized_data_90 = normalize_data(combineCTD_90_df)
write_data_frame_to_tsv_file(normalized_data_90, normalized_90)
# ---------------------------------------
# normalize cdhit 80 train data
combineCTD_80_df = get_data_frame_from_tsv_file(combineCTD_80)
print(combineCTD_80_df)
normalized_data_80 = normalize_data(combineCTD_80_df)
write_data_frame_to_tsv_file(normalized_data_80, normalized_80)

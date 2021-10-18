from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------

CKSAAP_90 = '../../../../features/iFeature/round3/CKSAAP/CKSAAP_90_mixed.tsv'
CKSAAP_80 = '../../../../features/iFeature/round3/CKSAAP/CKSAAP_80_mixed.tsv'

# ------------ output files -------------
normalized_90 = 'CKSAAP_90_mixed_normalized.tsv'
normalized_80 = 'CKSAAP_80_mixed_normalized.tsv'
# ---------------------------------------
# normalize cdhit 90 train data
CKSAAP_90_df = get_data_frame_from_tsv_file(CKSAAP_90)
print(CKSAAP_90_df)
normalized_data_90 = normalize_data(CKSAAP_90_df)
write_data_frame_to_tsv_file(normalized_data_90, normalized_90)
# ---------------------------------------
# normalize cdhit 80 train data
CKSAAP_80_df = get_data_frame_from_tsv_file(CKSAAP_80)
print(CKSAAP_80_df)
normalized_data_80 = normalize_data(CKSAAP_80_df)
write_data_frame_to_tsv_file(normalized_data_80, normalized_80)

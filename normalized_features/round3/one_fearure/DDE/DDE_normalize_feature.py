from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------
DDE_90 = '../../../../features/iFeature/round3/DDE/DDE_90_mixed.tsv'
DDE_80 = '../../../../features/iFeature/round3/DDE/DDE_80_mixed.tsv'

# ------------ output files -------------
normalized_90 = 'DDE_90_mixed_normalized.tsv'
normalized_80 = 'DDE_80_mixed_normalized.tsv'
# ---------------------------------------
# normalize cdhit 90 train data
DDE_90_df = get_data_frame_from_tsv_file(DDE_90)
print(DDE_90_df)
normalized_data_90 = normalize_data(DDE_90_df)
write_data_frame_to_tsv_file(normalized_data_90, normalized_90)
# ---------------------------------------
# normalize cdhit 80 train data
DDE_80_df = get_data_frame_from_tsv_file(DDE_80)
print(DDE_80_df)
normalized_data_80 = normalize_data(DDE_80_df)
write_data_frame_to_tsv_file(normalized_data_80, normalized_80)

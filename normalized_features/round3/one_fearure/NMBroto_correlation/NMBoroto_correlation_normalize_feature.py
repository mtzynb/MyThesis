from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------
NMBroto_90 = '../../../../features/iFeature/round3/NMBroto_correlation/NMBroto_90_mixed.tsv'
NMBroto_80 = '../../../../features/iFeature/round3/NMBroto_correlation/NMBroto_80_mixed.tsv'

# ------------ output files -------------
normalized_90 = 'NMBroto_90_mixed_normalized.tsv'
normalized_80 = 'NMBroto_80_mixed_normalized.tsv'
# ---------------------------------------
# normalize cdhit 90 data
NMBroto_90_df = get_data_frame_from_tsv_file(NMBroto_90)
print(NMBroto_90_df)
normalized_data_90 = normalize_data(NMBroto_90_df)
write_data_frame_to_tsv_file(normalized_data_90, normalized_90)
# ---------------------------------------
# normalize cdhit 80 data
NMBroto_80_df = get_data_frame_from_tsv_file(NMBroto_80)
print(NMBroto_80_df)
normalized_data_80 = normalize_data(NMBroto_80_df)
write_data_frame_to_tsv_file(normalized_data_80, normalized_80)

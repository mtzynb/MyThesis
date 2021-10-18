from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------
Geary_90 = '../../../../features/iFeature/round3/Geary_correlation/Geary_90_mixed.tsv'
Geary_80 = '../../../../features/iFeature/round3/Geary_correlation/Geary_80_mixed.tsv'

# ------------ output files -------------
normalized_90 = 'Geary_90_mixed_normalized.tsv'
normalized_80 = 'Geary_80_mixed_normalized.tsv'
# ---------------------------------------
# normalize cdhit 90  data
Geary_90_df = get_data_frame_from_tsv_file(Geary_90)
print(Geary_90_df)
normalized_data_90 = normalize_data(Geary_90_df)
write_data_frame_to_tsv_file(normalized_data_90, normalized_90)
# ---------------------------------------
# normalize cdhit 80  data
Geary_80_df = get_data_frame_from_tsv_file(Geary_80)
print(Geary_80_df)
normalized_data_80 = normalize_data(Geary_80_df)
write_data_frame_to_tsv_file(normalized_data_80, normalized_80)

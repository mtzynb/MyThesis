from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------

Moran_90 = '../../../../features/iFeature/round3/Moran_correlation/Moran_90_mixed.tsv'
Moran_80 = '../../../../features/iFeature/round3/Moran_correlation/Moran_80_mixed.tsv'

# ------------ output files -------------
normalized_90 = 'Moran_90_mixed_normalized.tsv'
normalized_80 = 'Moran_80_mixed_normalized.tsv'
# ---------------------------------------
# normalize cdhit 90 data
Moran_90_df = get_data_frame_from_tsv_file(Moran_90)
print(Moran_90_df)
normalized_data_90= normalize_data(Moran_90_df)
write_data_frame_to_tsv_file(normalized_data_90, normalized_90)
# ---------------------------------------
# normalize cdhit 80 data
Moran_80_df = get_data_frame_from_tsv_file(Moran_80)
print(Moran_80_df)
normalized_data_80= normalize_data(Moran_80_df)
write_data_frame_to_tsv_file(normalized_data_80, normalized_80)

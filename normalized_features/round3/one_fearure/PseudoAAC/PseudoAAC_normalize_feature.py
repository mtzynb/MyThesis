from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------
PseudoAAC_90 = '../../../../features/iFeature/round3/PseudoAAC/PseudoAAC_90_mixed.tsv'
PseudoAAC_80 = '../../../../features/iFeature/round3/PseudoAAC/PseudoAAC_80_mixed.tsv'

# ------------ output files -------------
normalized_90 = 'PseudoAAC_90_mixed_normalized.tsv'
normalized_80 = 'PseudoAAC_80_mixed_normalized.tsv'
# ---------------------------------------
# normalize cdhit 90 data
PseudoAAC_90_df = get_data_frame_from_tsv_file(PseudoAAC_90)
print(PseudoAAC_90_df)
normalized_data_90 = normalize_data(PseudoAAC_90_df)
write_data_frame_to_tsv_file(normalized_data_90, normalized_90)
# ---------------------------------------
# normalize cdhit 80 data
PseudoAAC_80_df = get_data_frame_from_tsv_file(PseudoAAC_80)
print(PseudoAAC_80_df)
normalized_data_80 = normalize_data(PseudoAAC_80_df)
write_data_frame_to_tsv_file(normalized_data_80, normalized_80)

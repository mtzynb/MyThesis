from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------

APseudoAAC_90 = '../../../../features/iFeature/round3/APseudoAAC/APseudoAAC_90_mixed.tsv'
APseudoAAC_80 = '../../../../features/iFeature/round3/APseudoAAC/APseudoAAC_80_mixed.tsv'

# ------------ output files -------------
normalized_90 = 'APseudoAAC_90_mixed_normalized.tsv'
normalized_80 = 'APseudoAAC_80_mixed_normalized.tsv'
# ---------------------------------------
# normalize cdhit 90 train data
APseudoAAC_90_df = get_data_frame_from_tsv_file(APseudoAAC_90)
print(APseudoAAC_90_df)
normalized_data_90 = normalize_data(APseudoAAC_90_df)
write_data_frame_to_tsv_file(normalized_data_90, normalized_90)
# ---------------------------------------
# normalize cdhit 80 train data
APseudoAAC_80_df = get_data_frame_from_tsv_file(APseudoAAC_80)
print(APseudoAAC_80_df)
normalized_data_80 = normalize_data(APseudoAAC_80_df)
write_data_frame_to_tsv_file(normalized_data_80, normalized_80)

from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------
KSCTriad_90 = '../../../../features/iFeature/round3/KSCTriad/KSCTriad_90_mixed.tsv'
KSCTriad_80 = '../../../../features/iFeature/round3/KSCTriad/KSCTriad_80_mixed.tsv'
# ------------ output files -------------
normalized_90 = 'KSCTriad_90_mixed_normalized.tsv'
normalized_80 = 'KSCTriad_80_mixed_normalized.tsv'
# ---------------------------------------
# normalize cdhit 90 data
KSCTriad_90_df = get_data_frame_from_tsv_file(KSCTriad_90)
print(KSCTriad_90_df)
normalized_data_90 = normalize_data(KSCTriad_90_df)
write_data_frame_to_tsv_file(normalized_data_90, normalized_90)
# ---------------------------------------
# normalize cdhit 80 data
KSCTriad_80_df = get_data_frame_from_tsv_file(KSCTriad_80)
print(KSCTriad_80_df)
normalized_data_80 = normalize_data(KSCTriad_80_df)
write_data_frame_to_tsv_file(normalized_data_80, normalized_80)

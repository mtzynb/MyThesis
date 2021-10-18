from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------
QSOrder_90 = '../../../../features/iFeature/round3/QSOrder/QSOrder_90_mixed.tsv'
QSOrder_80 = '../../../../features/iFeature/round3/QSOrder/QSOrder_80_mixed.tsv'
# ------------ output files -------------
normalized_90 = 'QSOrder_90_mixed_normalized.tsv'
normalized_80 = 'QSOrder_80_mixed_normalized.tsv'
# ---------------------------------------
# normalize cdhit 90 data
QSOrder_90_df = get_data_frame_from_tsv_file(QSOrder_90)
print(QSOrder_90_df)
normalized_data_90 = normalize_data(QSOrder_90_df)
write_data_frame_to_tsv_file(normalized_data_90, normalized_90)
# ---------------------------------------
# normalize cdhit 80 data
QSOrder_80_df = get_data_frame_from_tsv_file(QSOrder_80)
print(QSOrder_80_df)
normalized_data_80 = normalize_data(QSOrder_80_df)
write_data_frame_to_tsv_file(normalized_data_80, normalized_80)

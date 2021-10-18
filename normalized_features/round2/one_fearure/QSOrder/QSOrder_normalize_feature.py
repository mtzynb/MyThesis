from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------

QSOrder_train_100 = '../../../features/iFeature/round2/QSOrder/QSOrder_100_mixed_train.tsv'
QSOrder_train_90 = '../../../features/iFeature/round2/QSOrder/QSOrder_90_mixed_train.tsv'
QSOrder_train_80 = '../../../features/iFeature/round2/QSOrder/QSOrder_80_mixed_train.tsv'

# ------------ output files -------------
normalized_train_100 = 'QSOrder_100_mixed_train_normalized.tsv'
normalized_train_90 = 'QSOrder_90_mixed_train_normalized.tsv'
normalized_train_80 = 'QSOrder_80_mixed_train_normalized.tsv'
# ---------------------------------------
# # normalize cdhit 100 train data
QSOrder_train_100_df = get_data_frame_from_tsv_file(QSOrder_train_100)
print(QSOrder_train_100_df)
normalized_data_100_train = normalize_data(QSOrder_train_100_df)
write_data_frame_to_tsv_file(normalized_data_100_train, normalized_train_100)
# ---------------------------------------

# normalize cdhit 90 train data
QSOrder_train_90_df = get_data_frame_from_tsv_file(QSOrder_train_90)
print(QSOrder_train_90_df)
normalized_data_90_train = normalize_data(QSOrder_train_90_df)
write_data_frame_to_tsv_file(normalized_data_90_train, normalized_train_90)
# ---------------------------------------
# normalize cdhit 80 train data
QSOrder_train_80_df = get_data_frame_from_tsv_file(QSOrder_train_80)
print(QSOrder_train_80_df)
normalized_data_80_train = normalize_data(QSOrder_train_80_df)
write_data_frame_to_tsv_file(normalized_data_80_train, normalized_train_80)
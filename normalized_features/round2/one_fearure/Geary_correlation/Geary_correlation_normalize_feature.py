from codes.normalization import normalize_data
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------

Geary_train_100 = '../../../features/iFeature/round2/Geary_correlation/Geary_100_mixed_train.tsv'
Geary_train_90 = '../../../features/iFeature/round2/Geary_correlation/Geary_90_mixed_train.tsv'
Geary_train_80 = '../../../features/iFeature/round2/Geary_correlation/Geary_80_mixed_train.tsv'

# ------------ output files -------------
normalized_train_100 = 'Geary_100_mixed_train_normalized.tsv'
normalized_train_90 = 'Geary_90_mixed_train_normalized.tsv'
normalized_train_80 = 'Geary_80_mixed_train_normalized.tsv'
# ---------------------------------------
# # normalize cdhit 100 train data
Geary_train_100_df = get_data_frame_from_tsv_file(Geary_train_100)
print(Geary_train_100_df)
normalized_data_100_train = normalize_data(Geary_train_100_df)
write_data_frame_to_tsv_file(normalized_data_100_train, normalized_train_100)
# ---------------------------------------

# normalize cdhit 90 train data
Geary_train_90_df = get_data_frame_from_tsv_file(Geary_train_90)
print(Geary_train_90_df)
normalized_data_90_train = normalize_data(Geary_train_90_df)
write_data_frame_to_tsv_file(normalized_data_90_train, normalized_train_90)
# ---------------------------------------
# normalize cdhit 80 train data
Geary_train_80_df = get_data_frame_from_tsv_file(Geary_train_80)
print(Geary_train_80_df)
normalized_data_80_train = normalize_data(Geary_train_80_df)
write_data_frame_to_tsv_file(normalized_data_80_train, normalized_train_80)

import codes.drop_duplicatess as dropdup
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------

Geary_train_100 = '../../../normalized_features/one_fearure/Geary_correlation/Geary_100_mixed_train_normalized.tsv'
Geary_train_90 = '../../../normalized_features/one_fearure/Geary_correlation/Geary_90_mixed_train_normalized.tsv'
Geary_train_80 = '../../../normalized_features/one_fearure/Geary_correlation/Geary_80_mixed_train_normalized.tsv'

# ------------ output files -------------
dropdup_train_100 = 'Geary_100_mixed_train_dropdup.tsv'
dropdup_train_90 = 'Geary_90_mixed_train_dropdup.tsv'
dropdup_train_80 = 'Geary_80_mixed_train_dropdup.tsv'
# ---------------------------------------
# drop dups cdhit 100 train data
Geary_train_100_df = get_data_frame_from_tsv_file(Geary_train_100)
print("before drop 100 cdhit, shape= ", Geary_train_100_df.shape)
print(Geary_train_100_df)

dups = dropdup.find_duplicated_columns(Geary_train_100_df)
df100 = Geary_train_100_df.drop(dups, axis=1)
print("duplicate cols", dups)

df100 = dropdup.drop_columns_with_same_values(df100)
df100 = dropdup.drop_row_duplicates(df100)
df100.reset_index(drop=True, inplace=True)

print("After drop 100 cdhit, shape= ", df100.shape)

write_data_frame_to_tsv_file(df100, dropdup_train_100)
# ---------------------------------------

# drop dups cdhit 90 train data
Geary_train_90_df = get_data_frame_from_tsv_file(Geary_train_90)
print("before drop 90 cdhit, shape= ", Geary_train_90_df.shape)
print(Geary_train_90_df)

dups = dropdup.find_duplicated_columns(Geary_train_90_df)
df90 = Geary_train_90_df.drop(dups, axis=1)
print("duplicate cols", dups)

df90 = dropdup.drop_columns_with_same_values(df90)
df90 = dropdup.drop_row_duplicates(df90)
df90.reset_index(drop=True, inplace=True)

print("After drop 90 cdhit, shape= ", df90.shape)

write_data_frame_to_tsv_file(df90, dropdup_train_90)
# ---------------------------------------
# drop dups cdhit 80 train data
Geary_train_80_df = get_data_frame_from_tsv_file(Geary_train_80)
print("before drop 80 cdhit, shape= ", Geary_train_80_df.shape)
print(Geary_train_80_df)

dups = dropdup.find_duplicated_columns(Geary_train_80_df)
df80 = Geary_train_80_df.drop(dups, axis=1)
print("duplicate cols", dups)

df80 = dropdup.drop_columns_with_same_values(df80)
df80 = dropdup.drop_row_duplicates(df80)
df80.reset_index(drop=True, inplace=True)

print("After drop 80 cdhit, shape= ", df80.shape)

write_data_frame_to_tsv_file(df80, dropdup_train_80)

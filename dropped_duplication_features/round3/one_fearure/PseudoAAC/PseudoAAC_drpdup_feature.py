import codes.drop_duplicatess as dropdup
from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file

# ------------ input files -------------
PseudoAAC_90 = '../../../../normalized_features/round3/one_fearure/PseudoAAC/PseudoAAC_90_mixed_normalized.tsv'
PseudoAAC_80 = '../../../../normalized_features/round3/one_fearure/PseudoAAC/PseudoAAC_80_mixed_normalized.tsv'
# ------------ output files -------------
dropdup_90 = 'PseudoAAC_90_mixed_dropdup.tsv'
dropdup_80 = 'PseudoAAC_80_mixed_dropdup.tsv'
# ---------------------------------------
# drop dups cdhit 90 data
PseudoAAC_90_df = get_data_frame_from_tsv_file(PseudoAAC_90)
print("before drop 90 cdhit, shape= ", PseudoAAC_90_df.shape)
print(PseudoAAC_90_df)

dups = dropdup.find_duplicated_columns(PseudoAAC_90_df)
df90 = PseudoAAC_90_df.drop(dups, axis=1)
print("duplicate cols", dups)

df90 = dropdup.drop_columns_with_same_values(df90)
df90 = dropdup.drop_row_duplicates(df90)
df90.reset_index(drop=True, inplace=True)

print("After drop 90 cdhit, shape= ", df90.shape)

write_data_frame_to_tsv_file(df90, dropdup_90)
# ---------------------------------------
# drop dups cdhit 80 data
PseudoAAC_80_df = get_data_frame_from_tsv_file(PseudoAAC_80)
print("before drop 80 cdhit, shape= ", PseudoAAC_80_df.shape)
print(PseudoAAC_80_df)

dups = dropdup.find_duplicated_columns(PseudoAAC_80_df)
df80 = PseudoAAC_80_df.drop(dups, axis=1)
print("duplicate cols", dups)

df80 = dropdup.drop_columns_with_same_values(df80)
df80 = dropdup.drop_row_duplicates(df80)
df80.reset_index(drop=True, inplace=True)

print("After drop 80 cdhit, shape= ", df80.shape)

write_data_frame_to_tsv_file(df80, dropdup_80)

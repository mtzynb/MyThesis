from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file
from codes.df_utils import add_suffix_to_df_cols_name

# ------------ input files -------------

QSOrder_normalized_90 = '../../../../normalized_features/round3/one_fearure/QSOrder' \
                           '/QSOrder_90_mixed_normalized.tsv '
# ------------ output files -------------
modified_90 = 'QSOrder_90_mixed_normalized_modified_cols_name.tsv'
# ---------------------------------------
# add feature name to the columns of normalized cdhit 90 data
QSOrder_90_df = get_data_frame_from_tsv_file(QSOrder_normalized_90)

new_df = add_suffix_to_df_cols_name(QSOrder_90_df, "__QSOrder")
write_data_frame_to_tsv_file(new_df, modified_90)

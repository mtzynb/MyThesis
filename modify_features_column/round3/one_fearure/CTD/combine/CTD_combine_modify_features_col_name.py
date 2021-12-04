from codes.tsv_file_utils import get_data_frame_from_tsv_file, write_data_frame_to_tsv_file
from codes.df_utils import add_suffix_to_df_cols_name

# ------------ input files -------------

CTD_normalized_90 = '../../../../../normalized_features/round3/one_fearure/CTD/combine' \
                           '/combineCTD_90_mixed_normalized.tsv '
# ------------ output files -------------
modified_90 = 'combineCTD_90_mixed_normalized_modified_cols_name.tsv'
# ---------------------------------------
# add feature name to the columns of normalized cdhit 90 data
CTD_90_df = get_data_frame_from_tsv_file(CTD_normalized_90)

new_df = add_suffix_to_df_cols_name(CTD_90_df, "__CTD")
write_data_frame_to_tsv_file(new_df, modified_90)

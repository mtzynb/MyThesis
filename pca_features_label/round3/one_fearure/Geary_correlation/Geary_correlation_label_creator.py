from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

Geary_90 = '../../../../pca_features/round3/one_fearure/Geary_correlation/Geary_90_mixed_pca.tsv'
# Geary_80 = '../../../../pca_features/round3/one_fearure/Geary_correlation/Geary_80_mixed_pca.tsv'

# ------------ output files -------------
label_90 = 'Geary_90_mixed_pca_label.tsv'
# label_80 = 'Geary_80_mixed_pca_label.tsv'
# ---------------------------------------
# # drop dups cdhit 90 data
get_label_data_from_tsv_file(Geary_90, label_90)
# # ---------------------------------------
# # drop dups cdhit 80 data
# get_label_data_from_tsv_file(Geary_80, label_80)

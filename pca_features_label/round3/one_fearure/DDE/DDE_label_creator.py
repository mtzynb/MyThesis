from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

DDE_90 = '../../../../pca_features/round3/one_fearure/DDE/DDE_90_mixed_pca.tsv'
DDE_80 = '../../../../pca_features/round3/one_fearure/DDE/DDE_80_mixed_pca.tsv'

# ------------ output files -------------
label_90 = 'DDE_90_mixed_pca_label.tsv'
label_80 = 'DDE_80_mixed_pca_label.tsv'
# ---------------------------------------
# # drop dups cdhit 90 data
get_label_data_from_tsv_file(DDE_90, label_90)
# # ---------------------------------------
# # drop dups cdhit 80 data
get_label_data_from_tsv_file(DDE_80, label_80)

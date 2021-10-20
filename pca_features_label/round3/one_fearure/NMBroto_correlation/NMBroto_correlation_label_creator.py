from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

NMBroto_90 = '../../../../pca_features/round3/one_fearure/NMBroto_correlation/NMBroto_90_mixed_pca.tsv'
NMBroto_80 = '../../../../pca_features/round3/one_fearure/NMBroto_correlation/NMBroto_80_mixed_pca.tsv'

# ------------ output files -------------
label_90 = 'NMBroto_90_mixed_pca_label.tsv'
label_80 = 'NMBroto_80_mixed_pca_label.tsv'
# ---------------------------------------
# # drop dups cdhit 90 data
get_label_data_from_tsv_file(NMBroto_90, label_90)
# # ---------------------------------------
# # drop dups cdhit 80 data
get_label_data_from_tsv_file(NMBroto_80, label_80)

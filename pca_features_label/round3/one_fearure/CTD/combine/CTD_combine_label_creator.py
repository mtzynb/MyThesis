from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

combineCTD_90 = '../../../../../pca_features/round3/one_fearure/CTD/combine/combineCTD_90_mixed_pca.tsv'
combineCTD_80 = '../../../../../pca_features/round3/one_fearure/CTD/combine/combineCTD_80_mixed_pca.tsv'

# ------------ output files -------------
label_90 = 'combineCTD_90_mixed_pca_label.tsv'
label_80 = 'combineCTD_80_mixed_pca_label.tsv'
# ---------------------------------------
# # drop dups cdhit 90 data
get_label_data_from_tsv_file(combineCTD_90, label_90)
# # ---------------------------------------
# # drop dups cdhit 80 data
get_label_data_from_tsv_file(combineCTD_80, label_80)

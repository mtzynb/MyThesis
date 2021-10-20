from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

APseudoAAC_90 = '../../../../pca_features/round3/one_fearure/APseudoAAC/APseudoAAC_90_mixed_pca.tsv'
APseudoAAC_80 = '../../../../pca_features/round3/one_fearure/APseudoAAC/APseudoAAC_80_mixed_pca.tsv'

# ------------ output files -------------
label_90 = 'APseudoAAC_90_mixed_pca_label.tsv'
label_80 = 'APseudoAAC_80_mixed_pca_label.tsv'
# ---------------------------------------
# # drop dups cdhit 90  data
get_label_data_from_tsv_file(APseudoAAC_90, label_90)
# # ---------------------------------------
# # drop dups cdhit 80  data
get_label_data_from_tsv_file(APseudoAAC_80, label_80)

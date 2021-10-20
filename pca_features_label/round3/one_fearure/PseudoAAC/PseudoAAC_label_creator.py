from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

PseudoAAC_90 = '../../../../pca_features/round3/one_fearure/PseudoAAC/PseudoAAC_90_mixed_pca.tsv'
PseudoAAC_80 = '../../../../pca_features/round3/one_fearure/PseudoAAC/PseudoAAC_80_mixed_pca.tsv'

# ------------ output files -------------
label_90 = 'PseudoAAC_90_mixed_pca_label.tsv'
label_80 = 'PseudoAAC_80_mixed_pca_label.tsv'
# ---------------------------------------
# # drop dups cdhit 90 data
get_label_data_from_tsv_file(PseudoAAC_90, label_90)
# # ---------------------------------------
# # drop dups cdhit 80 data
get_label_data_from_tsv_file(PseudoAAC_80, label_80)

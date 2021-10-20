from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

CKSAAP_90 = '../../../../pca_features/round3/one_fearure/CKSAAP/CKSAAP_90_mixed_pca.tsv'
CKSAAP_80 = '../../../../pca_features/round3/one_fearure/CKSAAP/CKSAAP_80_mixed_pca.tsv'

# ------------ output files -------------
label_90 = 'CKSAAP_90_mixed_pca_label.tsv'
label_80 = 'CKSAAP_80_mixed_pca_label.tsv'
# ---------------------------------------
# # drop dups cdhit 90 data
get_label_data_from_tsv_file(CKSAAP_90, label_90)
# # ---------------------------------------
# # drop dups cdhit 80 data
get_label_data_from_tsv_file(CKSAAP_80, label_80)

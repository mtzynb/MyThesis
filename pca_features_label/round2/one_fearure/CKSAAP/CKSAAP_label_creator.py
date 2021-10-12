from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

CKSAAP_train_100 = '../../../pca_features/one_fearure/CKSAAP/CKSAAP_100_mixed_train_pca.tsv'
CKSAAP_train_90 = '../../../pca_features/one_fearure/CKSAAP/CKSAAP_90_mixed_train_pca.tsv'
CKSAAP_train_80 = '../../../pca_features/one_fearure/CKSAAP/CKSAAP_80_mixed_train_pca.tsv'

# ------------ output files -------------
label_train_100 = 'CKSAAP_100_mixed_train_pca_label.txt'
label_train_90 = 'CKSAAP_90_mixed_train_pca_label.txt'
label_train_80 = 'CKSAAP_80_mixed_train_pca_label.txt'
# ---------------------------------------
# drop dups cdhit 100 train data
get_label_data_from_tsv_file(CKSAAP_train_100, label_train_100)
# ---------------------------------------
# # drop dups cdhit 90 train data
get_label_data_from_tsv_file(CKSAAP_train_90, label_train_90)
# # ---------------------------------------
# # drop dups cdhit 80 train data
get_label_data_from_tsv_file(CKSAAP_train_80, label_train_80)

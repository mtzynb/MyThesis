from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

NMBroto_train_100 = '../../../pca_features/one_fearure/NMBroto_correlation/NMBroto_100_mixed_train_pca.tsv'
NMBroto_train_90 = '../../../pca_features/one_fearure/NMBroto_correlation/NMBroto_90_mixed_train_pca.tsv'
NMBroto_train_80 = '../../../pca_features/one_fearure/NMBroto_correlation/NMBroto_80_mixed_train_pca.tsv'

# ------------ output files -------------
label_train_100 = 'NMBroto_100_mixed_train_pca_label.txt'
label_train_90 = 'NMBroto_90_mixed_train_pca_label.txt'
label_train_80 = 'NMBroto_80_mixed_train_pca_label.txt'
# ---------------------------------------
# drop dups cdhit 100 train data
get_label_data_from_tsv_file(NMBroto_train_100, label_train_100)
# ---------------------------------------
# # drop dups cdhit 90 train data
get_label_data_from_tsv_file(NMBroto_train_90, label_train_90)
# # ---------------------------------------
# # drop dups cdhit 80 train data
get_label_data_from_tsv_file(NMBroto_train_80, label_train_80)

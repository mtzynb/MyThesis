from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

Geary_train_100 = '../../../pca_features/one_fearure/Geary_correlation/Geary_100_mixed_train_pca.tsv'
Geary_train_90 = '../../../pca_features/one_fearure/Geary_correlation/Geary_90_mixed_train_pca.tsv'
Geary_train_80 = '../../../pca_features/one_fearure/Geary_correlation/Geary_80_mixed_train_pca.tsv'

# ------------ output files -------------
label_train_100 = 'Geary_100_mixed_train_pca_label.txt'
label_train_90 = 'Geary_90_mixed_train_pca_label.txt'
label_train_80 = 'Geary_80_mixed_train_pca_label.txt'
# ---------------------------------------
# drop dups cdhit 100 train data
get_label_data_from_tsv_file(Geary_train_100, label_train_100)
# ---------------------------------------
# # drop dups cdhit 90 train data
get_label_data_from_tsv_file(Geary_train_90, label_train_90)
# # ---------------------------------------
# # drop dups cdhit 80 train data
get_label_data_from_tsv_file(Geary_train_80, label_train_80)

from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

Moran_train_100 = '../../../pca_features/one_fearure/Moran_correlation/Moran_100_mixed_train_pca.tsv'
Moran_train_90 = '../../../pca_features/one_fearure/Moran_correlation/Moran_90_mixed_train_pca.tsv'
Moran_train_80 = '../../../pca_features/one_fearure/Moran_correlation/Moran_80_mixed_train_pca.tsv'

# ------------ output files -------------
label_train_100 = 'Moran_100_mixed_train_pca_label.txt'
label_train_90 = 'Moran_90_mixed_train_pca_label.txt'
label_train_80 = 'Moran_80_mixed_train_pca_label.txt'
# ---------------------------------------
# drop dups cdhit 100 train data
get_label_data_from_tsv_file(Moran_train_100, label_train_100)
# ---------------------------------------
# # drop dups cdhit 90 train data
get_label_data_from_tsv_file(Moran_train_90, label_train_90)
# # ---------------------------------------
# # drop dups cdhit 80 train data
get_label_data_from_tsv_file(Moran_train_80, label_train_80)

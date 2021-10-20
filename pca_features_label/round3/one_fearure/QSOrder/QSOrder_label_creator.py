from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

QSOrder_90 = '../../../../pca_features/round3/one_fearure/QSOrder/QSOrder_90_mixed_pca.tsv'
QSOrder_80 = '../../../../pca_features/round3/one_fearure/QSOrder/QSOrder_80_mixed_pca.tsv'

# ------------ output files -------------
label_90 = 'QSOrder_90_mixed_pca_label.tsv'
label_80 = 'QSOrder_80_mixed_pca_label.tsv'
# ---------------------------------------
# # drop dups cdhit 90 data
get_label_data_from_tsv_file(QSOrder_90, label_90)
# # ---------------------------------------
# # drop dups cdhit 80 data
get_label_data_from_tsv_file(QSOrder_80, label_80)

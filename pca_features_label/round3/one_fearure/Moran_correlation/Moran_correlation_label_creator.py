from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

Moran_90 = '../../../../pca_features/round3/one_fearure/Moran_correlation/Moran_90_mixed_pca.tsv'
# Moran_80 = '../../../../pca_features/round3/one_fearure/Moran_correlation/Moran_80_mixed_pca.tsv'

# ------------ output files -------------
label_90 = 'Moran_90_mixed_pca_label.tsv'
# label_80 = 'Moran_80_mixed_pca_label.tsv'
# ---------------------------------------
# # drop dups cdhit 90 data
get_label_data_from_tsv_file(Moran_90, label_90)
# # ---------------------------------------
# # drop dups cdhit 80 data
# get_label_data_from_tsv_file(Moran_80, label_80)

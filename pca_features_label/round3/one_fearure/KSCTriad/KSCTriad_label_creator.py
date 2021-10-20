from codes.label_creator import get_label_data_from_tsv_file

# ------------ input files -------------

KSCTriad_90 = '../../../../pca_features/round3/one_fearure/KSCTriad/KSCTriad_90_mixed_pca.tsv'
KSCTriad_80 = '../../../../pca_features/round3/one_fearure/KSCTriad/KSCTriad_80_mixed_pca.tsv'

# ------------ output files -------------
label_90 = 'KSCTriad_90_mixed_pca_label.tsv'
label_80 = 'KSCTriad_80_mixed_pca_label.tsv'
# ---------------------------------------
# # drop dups cdhit 90 data
get_label_data_from_tsv_file(KSCTriad_90, label_90)
# # ---------------------------------------
# # drop dups cdhit 80 data
get_label_data_from_tsv_file(KSCTriad_80, label_80)

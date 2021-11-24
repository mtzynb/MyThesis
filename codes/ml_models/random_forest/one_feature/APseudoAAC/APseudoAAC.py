from codes.tsv_file_utils import get_data_frame_from_tsv_file
from codes.ml_models.random_forest.random_forest import train_rf_with_cv, train_rf_with_independent_test_data
from codes.utility import split_test_train

# -------------- X ---------------------
APseudoAAC_90 = '../../../../../pca_features/round3/one_fearure/APseudoAAC/APseudoAAC_90_mixed_pca.tsv'
APseudoAAC_80 = '../../../../../pca_features/round3/one_fearure/APseudoAAC/APseudoAAC_80_mixed_pca.tsv'
# -------------- Y ---------------------
label_90 = '../../../../../pca_features_label/round3/one_fearure/APseudoAAC/APseudoAAC_90_mixed_pca_label.tsv'
label_80 = '../../../../../pca_features_label/round3/one_fearure/APseudoAAC/APseudoAAC_80_mixed_pca_label.tsv'
# -------------------------
APseudoAAC_90_X = get_data_frame_from_tsv_file(APseudoAAC_90)
APseudoAAC_90_X = APseudoAAC_90_X.iloc[:, 1:11]
print("APseudoAAC_90_X size: ")
print(len(APseudoAAC_90_X))

label_90_Y = get_data_frame_from_tsv_file(label_90)
label_90_Y = label_90_Y.iloc[:, 1]

print("label_90_Y size: ")
print(len(label_90_Y))

x_train, x_test, y_train, y_test = split_test_train(APseudoAAC_90_X, label_90_Y)

# print("x_train")
# print(len(x_train))
#
# print("x_test")
# print(len(x_test))
#
# print("y_train")
# print(len(y_train))

print("y_test")
print(len(y_test))
print(y_test)
# print("label_90_Y")
# print(label_90_Y)
# -------------------------
# APseudoAAC_80_X = get_data_frame_from_tsv_file(APseudoAAC_80)
# APseudoAAC_80_X = APseudoAAC_80_X.iloc[:, 1:11]
# print(APseudoAAC_80_X)
# label_80_Y = get_data_frame_from_tsv_file(label_80)
# label_80_Y = label_80_Y.iloc[:, 1]
#
# # print("label_80_Y")
# # print(label_80_Y)
# # ---------------------------
train_rf_with_cv(x_train, y_train, "APseudoAAC_90_X")
# train_rf_with_independent_test_data(APseudoAAC_90_X, label_90_Y, "APseudoAAC_90_X")

import numpy as np
import codes.utility as utility
import codes.plot_bar as plot_bar
from bidi.algorithm import get_display
from arabic_reshaper import reshape

# --------------------------------------------------
sfs_model_result_file = '../../../../codes/feature_selection/wrapper_methods/50_features/50_combined_90_model.sav'
sfs = utility.load_model(sfs_model_result_file)
# --------------------------------------------------
print('k_feature_names_')
print(sfs.k_feature_names_)
k_f_names = np.array(sfs.k_feature_names_)

print(k_f_names)
print("k_f_names:", len(k_f_names))

features = ['APseudoAAC', 'CKSAAP', 'CTD', 'DDE', 'KSCTriad', 'PseudoAAC', 'QSOrder']
features_count = [0, 0, 0, 0, 0, 0, 0]

for i in k_f_names:

    if utility.isStringContainsOf(i, '__APseudoAAC'):
        features_count[0] = features_count[0] + 1

    if utility.isStringContainsOf(i, '__CKSAAP'):
        features_count[1] = features_count[1] + 1

    if utility.isStringContainsOf(i, '__CTD'):
        features_count[2] = features_count[2] + 1

    if utility.isStringContainsOf(i, '__DDE'):
        features_count[3] = features_count[3] + 1

    if utility.isStringContainsOf(i, '__KSCTriad'):
        features_count[4] = features_count[4] + 1

    if utility.isStringContainsOf(i, '__PseudoAAC'):
        features_count[5] = features_count[5] + 1

    if utility.isStringContainsOf(i, '__QSOrder'):
        features_count[6] = features_count[6] + 1

print('features')
print(features)

print('features_count')
print(features_count)

title_ = 'نمودار 50 ویژگی انتخاب شده توسط انتخاب متوالی رو به جلو'

plot_bar.plot_bar(x=features,
                  y=features_count,
                  plot_out_file='50_f_selected_plot_farsi.png',
                  plot_title=get_display(reshape(title_)),
                  x_label=get_display(reshape('ویژگی های استخراج شده مبتنی بر توالی')),
                  y_label=get_display(reshape('تعداد ویژگی های انتخاب شده')))
print('plot saved')

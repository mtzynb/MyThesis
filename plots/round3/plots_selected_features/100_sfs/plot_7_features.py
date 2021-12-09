import numpy as np
import codes.utility as utility
import codes.plot_bar as plot_bar

# --------------------------------------------------
sfs_model_result_file = '../../../../codes/feature_selection/wrapper_methods/100_features/100_combined_90_model.sav'
sfs = utility.load_model(sfs_model_result_file)
# --------------------------------------------------
print('k_feature_names_')
print(sfs.k_feature_names_)
k_f_names = np.array(sfs.k_feature_names_)

print(k_f_names)

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

plot_bar.plot_bar(x=features, y=features_count, plot_out_file='100_f_selected_plot.png',
                  plot_title='Plot of 100 Selected Features Based on SFS',
                  x_label='Seq Based Features', y_label='Selected Count')
print('plot saved')

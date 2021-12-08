from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt


def plot_f_selection(f_selector, title, figname):

    fig = plot_sfs(f_selector.get_metric_dict(), kind='std_dev')
    plt.ylim([0.6, 1])
    plt.xlim([1, 200])
    plt.title(title)
    plt.grid()
    # plt.show()
    plt.savefig(figname)

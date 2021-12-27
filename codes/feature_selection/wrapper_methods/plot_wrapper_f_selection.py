from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import codes.feature_selection.wrapper_methods.plot_sfss as my_plot_sfs
import matplotlib.pyplot as plt


def plot_f_selection(f_selector, title, figname):
    fig = plot_sfs(f_selector.get_metric_dict(), kind='std_dev')
    plt.ylim([0.6, 1])
    plt.xlim([1, 200])
    plt.title(title)
    plt.grid()
    # plt.show()
    plt.savefig(figname)


def plot_f_selection3(f_selector, title, figname, feature_no, x_lable_steps):
    fig = my_plot_sfs.plot_sequential_feature_selection(
        metric_dict=f_selector.get_metric_dict(),
        # figsize=(12, 6),
        title=title,
        # color='purple',
        # bcolor='violet',
        figname=figname,
        feature_no=feature_no,
        x_lable_steps=x_lable_steps,
        ylabel='Performance (10-foldCV accuracy)'
    )

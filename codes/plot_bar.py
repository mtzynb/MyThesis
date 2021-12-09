import matplotlib.pyplot as plt


def plot_bar(x, y, plot_out_file, plot_title, x_label, y_label, width=0.1):
    plt.bar(x, y, width=0.1)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_title)
    # plt.show()
    plt.savefig(plot_out_file)

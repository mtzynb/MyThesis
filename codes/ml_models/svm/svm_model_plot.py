import numpy as np
from matplotlib import pyplot as plt


def plot_svm_model(model_cv_result, figname):
    plt.figure(figsize=(13, 13))
    plt.title("RandomizedSearchCV evaluating using multiple scorers simultaneously", fontsize=16)

    plt.xlabel("Regularization parameter (c)")
    plt.ylabel("Score")

    ax = plt.gca()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Get the regular numpy array from the MaskedArray
    X_axis = np.array(model_cv_result["param_n_estimators"].data, dtype=float)

    scoring = ['accuracy', 'roc_auc']

    for scorer, color in zip(sorted(scoring), ["g", "k"]):
        for sample, style in (("train", "--"), ("test", "-")):
            sample_score_mean = model_cv_result["mean_%s_%s" % (sample, scorer)]
            sample_score_std = model_cv_result["std_%s_%s" % (sample, scorer)]
            ax.fill_between(
                X_axis,
                sample_score_mean - sample_score_std,
                sample_score_mean + sample_score_std,
                alpha=0.1 if sample == "test" else 0,
                color=color,
            )
            ax.plot(
                X_axis,
                sample_score_mean,
                style,
                color=color,
                alpha=1 if sample == "test" else 0.7,
                label="%s (%s)" % (scorer, sample),
            )

        best_index = np.nonzero(model_cv_result["rank_test_%s" % scorer] == 1)[0][0]
        best_score = model_cv_result["mean_test_%s" % scorer][best_index]
        print("$$$$$$$$$$$$$ scorer $$$$$$$$$$$$$$$", scorer)

        # Plot a dotted vertical line at the best score for that scorer marked by x
        ax.plot(
            [
                X_axis[best_index],
            ]
            * 2,
            [0, best_score],
            linestyle="-.",
            color=color,
            marker="x",
            markeredgewidth=3,
            ms=8,
        )

        # Annotate the best score for that scorer
        ax.annotate("%0.2f" % best_score, (X_axis[best_index], best_score + 0.005))

    plt.legend(loc="best")
    plt.grid(False)
    plt.savefig(figname)
    print("plot created")
    # plt.show()

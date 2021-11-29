def rf_model_log(filename, rf_random, best_estimator_,
                 best_params_, best_score_, best_index_, scorer_,
                 scoring, cv_results_,
                 execution_time):
    f = open(filename, "a")

    f.write("rf_random: \n")
    f.write(str(rf_random))

    f.write("\n\n rf_random.best_estimator_: \n")
    f.write(str(best_estimator_))

    f.write("\n\n rf_random.best_params_: \n")
    f.write(str(best_params_))

    f.write("\n\n rf_random.best_score_: \n")
    f.write(str(best_score_))

    f.write("\n\n rf_random.best_index_: \n")
    f.write(str(best_index_))

    f.write("\n\n rf_random.scorer_: \n")
    f.write(str(scorer_))

    f.write("\n\n rf_random.scoring: \n")
    f.write(str(scoring))

    f.write("\n\n rf_random.cv_results_: \n")
    f.write(str(cv_results_))

    f.write("\n\n hyper parameter execution_time: (sec) \n")
    f.write(str(execution_time))

    f.close()

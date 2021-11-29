from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


def train_rf_classifier(x_train, y_train, params):
    rfc_model = RandomForestClassifier(n_estimators=params["n_estimators"],
                                       max_features=params["max_features"],
                                       max_depth=params["max_depth"],
                                       min_samples_split=params["min_samples_split"],
                                       min_samples_leaf=params["min_samples_leaf"],
                                       bootstrap=params["bootstrap"])
    # , random_state=0)
    rfc_model.fit(x_train, y_train)
    return rfc_model


def evaluate_and_log(model, x_test, y_test, log_filename):
    predictions = model.predict(x_test)
    f = open(log_filename, "a")
    f.write('Model Performance\n')
    f.write("\n=== Confusion Matrix ===\n")
    f.write(str(confusion_matrix(y_test, predictions)))
    f.write("\n=== Classification Report ===\n")
    class_report = classification_report(y_test, predictions)
    print("class_report %s " % class_report)
    f.write(class_report)

    return class_report

from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import time


def train_predict_log(x_train, y_train, x_test, y_test, params, log_filename):
    start = time.time()

    print("params")
    print(params)

    svc_model = SVC(kernel=params['kernel'],
                    C=params['C'],
                    gamma=params['gamma'],
                    random_state=0)
    svc_model.fit(x_train, y_train)
    fit_time = time.time() - start

    predictions = svc_model.predict(x_test)

    f = open(log_filename, "a")
    f.write('Model Performance\n')
    f.write("\n=== Confusion Matrix ===\n")
    f.write(str(confusion_matrix(y_test, predictions)))
    f.write("\n=== Classification Report ===\n")
    class_report = classification_report(y_test, predictions)
    print("class_report %s " % class_report)
    f.write(class_report)

    f.write("\n\n train execution_time: (sec) \n")
    f.write(str(fit_time))

    return svc_model

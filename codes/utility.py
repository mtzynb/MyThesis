from sklearn.model_selection import train_test_split
import pickle


def split_test_train(X, Y, test_size=0.2):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=66)
    return x_train, x_test, y_train, y_test


def save_model(filename, model):
    pickle.dump(model, open(filename, 'wb'))


def load_model(filename):
    # load the model from disk
    return pickle.load(open(filename, 'rb'))
    # result = loaded_model.score(X_test, Y_test)


def isStringContainsOf(str, qry):
    if str.find(qry) == -1:
        return False
    else:
        return True

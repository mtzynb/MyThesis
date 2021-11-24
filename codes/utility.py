from sklearn.model_selection import train_test_split


def split_test_train(X, Y, test_size=0.2):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=66)
    return x_train, x_test, y_train, y_test

import pandas as pd


def find_duplicated_columns(df):
    dupes = []
    columns = df.columns
    for i in range(len(columns)):
        col1 = df.iloc[:, i]
        for j in range(i + 1, len(columns)):
            col2 = df.iloc[:, j]
            # break early if dtypes aren't the same (helps deal with
            # categorical dtypes)
            if col1.dtype is not col2.dtype:
                break
            # otherwise compare values
            if col1.equals(col2):
                dupes.append(columns[i])
                break

    return dupes


def drop_row_duplicates(df):
    df.drop_duplicates(keep='first', inplace=True)
    return df


def drop_columns_with_same_values(df):
    df = df[[i for i in df if len(set(df[i])) > 1]]
    return df


# data = [
#     {'x': 2, 'z': 3, 'w': 3, 'r': 1, 't': 0.0, 'l': 1},
#     {'x': 10, 'y': 20, 'z': 30, 'w': 30, 'r': 1, 't': 0.0, 'l': 1},
#     {'x': 2, 'z': 3, 'w': 3, 'r': 1, 't': 0.0, 'l': 1},
#     {'x': 11, 'y': 22, 'z': 30, 'w': 30, 'r': 1, 't': 0.0, 'l': 1},
#     {'x': 10, 'y': 20, 'z': 30, 'w': 30, 'r': 1, 't': 0.0, 'l': 1},
#     {'x': 11, 'y': 22, 'z': 30, 'w': 30, 'r': 1, 't': 0.0, 'l': 1},
#     {'x': 2, 'z': 3, 'w': 3, 'r': 1, 't': 0.0, 'l': 1}
#
# ]
# dframe = pd.DataFrame(data, index=['0', '1', '2', '3', '4', '5', '6'])
#
# print(dframe)
# print("*************")
# dups = find_duplicated_columns(dframe)
# frame = dframe.drop(dups, axis=1)
# frame = drop_row_duplicates(frame)
# new = drop_columns_with_same_values(frame)
# print(new)
#
# new.reset_index(drop=True, inplace=True)
# print(new)

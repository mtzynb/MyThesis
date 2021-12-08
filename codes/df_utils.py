import pandas as pd


def add_suffix_to_df_cols_name(df, suffix):
    col_name_list = df.columns.values.tolist()
    print("--add_suffix_to_df_cols_name--")
    print("before modify cols name list: ", col_name_list)
    for i in range(len(col_name_list)):
        col_name_list[i] = col_name_list[i] + suffix + str(i)

    df.set_axis(col_name_list, axis=1, inplace=True)

    print("after modify cols name list: ", col_name_list)
    return df


def save_df_to_pkl(df, file_name):
    df.to_pickle(file_name)  # where to save it, usually as a .pkl


def load_pkl_to_df(file_name):
    return pd.read_pickle(file_name)

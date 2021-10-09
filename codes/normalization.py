from sklearn.preprocessing import MinMaxScaler
import pandas as pd


def normalize_data(input_df):
    input_df_without_first_column = input_df.iloc[:, 1:]
    scaler = MinMaxScaler()
    arr_scaled = scaler.fit_transform(input_df_without_first_column)
    df_scaled = pd.DataFrame(arr_scaled, columns=input_df_without_first_column.columns,
                             index=input_df_without_first_column.index)
    df_scaled.insert(0, "ID", input_df.iloc[:, 0], True)
    return df_scaled

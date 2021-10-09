from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from tsv_file_utils import get_data_frame_from_tsv_file


def normalize_data(input_df):
    input_df_without_first_column = input_df.iloc[:, 1:]
    scaler = MinMaxScaler()
    arr_scaled = scaler.fit_transform(input_df_without_first_column)
    df_scaled = pd.DataFrame(arr_scaled, columns=input_df_without_first_column.columns,
                             index=input_df_without_first_column.index)
    df_scaled.insert(0, "ID", input_df.iloc[:, 0], True)
    return df_scaled


AAC_train_100 = '../features/iFeature/round2/AAC/AAC_100_mixed_train.tsv'
AAC_train_100_df = get_data_frame_from_tsv_file(AAC_train_100)
print(AAC_train_100_df)
normalized_data = normalize_data(AAC_train_100_df)
print(normalized_data)

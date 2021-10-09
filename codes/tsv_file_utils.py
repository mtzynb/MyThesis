import pandas as pd


def get_data_frame_from_tsv_file(tsv_file):
    return pd.read_csv(tsv_file, sep="\t")


def write_data_frame_to_tsv_file(input_df, output_tsv_file):
    input_df.to_csv(output_tsv_file, sep="\t", index=False)
    print("write_data_frame_to_tsv_file DONE!")

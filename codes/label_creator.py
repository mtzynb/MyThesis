from Bio import SeqIO

from codes.tsv_file_utils import get_data_frame_from_tsv_file


def get_label_data(fasta_input_dir, output_file_dir):
    labels = ''
    for seq_record in SeqIO.parse(open(fasta_input_dir, mode='r'), 'fasta'):
        peptide_id, label_id = seq_record.id.split('|')
        label_record = seq_record.id + "\t" + label_id + "\n"
        labels = labels + label_record

    f = open(output_file_dir, "w")
    f.write(labels)
    f.close()


def get_label_data_from_tsv_file(tsv_input, output_file):
    labels = ''
    input_df = get_data_frame_from_tsv_file(tsv_input)
    first_col = input_df.iloc[:, 0]
    for i in range(len(first_col)):
        peptide_id, label_id = first_col[i].split('|')
        label_record = first_col[i] + "\t" + label_id + "\n"
        labels = labels + label_record

    f = open(output_file, "w")
    f.write(labels)
    f.close()

# # --------------------------------------------------------------------------
#
# train_mixed_100_input_dir = '../data/split_data/test_train_data_main/mixed_data/train_mixed_100.fasta'
# train_mixed_100_output_dir = '../data/split_data/test_train_data_main/mixed_data/label/train_mixed_100_label.txt'
#
# get_label_data(train_mixed_100_input_dir, train_mixed_100_output_dir)
#
# # --------------------------------------------------------------------------
#
# train_mixed_90_input_dir = '../data/split_data/test_train_data_main/mixed_data/train_mixed_90.fasta'
# train_mixed_90_output_dir = '../data/split_data/test_train_data_main/mixed_data/label/train_mixed_90_label.txt'
#
# get_label_data(train_mixed_90_input_dir, train_mixed_90_output_dir)
#
# # --------------------------------------------------------------------------
#
# train_mixed_80_input_dir = '../data/split_data/test_train_data_main/mixed_data/train_mixed_80.fasta'
# train_mixed_80_output_dir = '../data/split_data/test_train_data_main/mixed_data/label/train_mixed_80_label.txt'
#
# get_label_data(train_mixed_80_input_dir, train_mixed_80_output_dir)
#
# # ------------------------------------ TEST DATA ----------------------------------
#
# test_mixed_100_input_dir = '../data/split_data/test_train_data_main/mixed_data/test_mixed_100.fasta'
# test_mixed_100_output_dir = '../data/split_data/test_train_data_main/mixed_data/label/test_mixed_100_label.txt'
#
# get_label_data(test_mixed_100_input_dir, test_mixed_100_output_dir)
#
# # --------------------------------------------------------------------------
# test_mixed_90_input_dir = '../data/split_data/test_train_data_main/mixed_data/test_mixed_90.fasta'
# test_mixed_90_output_dir = '../data/split_data/test_train_data_main/mixed_data/label/test_mixed_90_label.txt'
#
# get_label_data(test_mixed_90_input_dir, test_mixed_90_output_dir)
# # --------------------------------------------------------------------------
# test_mixed_80_input_dir = '../data/split_data/test_train_data_main/mixed_data/test_mixed_80.fasta'
# test_mixed_80_output_dir = '../data/split_data/test_train_data_main/mixed_data/label/test_mixed_80_label.txt'
#
# get_label_data(test_mixed_80_input_dir, test_mixed_80_output_dir)

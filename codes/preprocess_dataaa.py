from Bio import SeqIO


def filter_seq_length(fasta_file_name, output_file, min_len, max_len):
    result = []
    c = 0
    for seq_record in SeqIO.parse(open(fasta_file_name, mode='r'), 'fasta'):
        if min_len < len(seq_record) < max_len:
            c += 1
            result.append(seq_record)

    SeqIO.write(result, output_file, "fasta")
    print("C : ", c)


def count_seq_samples(fasta_input_file):
    count_seq = len([1 for line in open(fasta_input_file) if line.startswith(">")])
    return count_seq


def count_seq_samples_by_class_label(input_fasta, class_label):
    query = "|" + class_label
    count = 0
    for seq_record in SeqIO.parse(open(input_fasta, mode='r'), 'fasta'):
        if query in seq_record.id:
            count += 1

    return count


# filter_seq_length("../data/new_cdhit/round3/corrected_files/new-corrected-ACP-Mixed-90.fasta",
#                   "../data/split_data/round3/preprocess_level1_length_filter/ACP-Mixed-90_preprocess_level1.fasta",
#                   4, 51)
# filter_seq_length("../data/new_cdhit/round3/corrected_files/new-corrected-ACP-Mixed-80.fasta",
#                   "../data/split_data/round3/preprocess_level1_length_filter/ACP-Mixed-80_preprocess_level1.fasta",
#                   4, 51)
# count_seq_samples(
#     "../data/split_data/round3/preprocess_level1_length_filter/ACP-Mixed-80_preprocess_level1.fasta")  # 4714
# count_seq_samples(
#     "../data/split_data/round3/preprocess_level1_length_filter/ACP-Mixed-80_preprocess_level1.fasta")  # 4423


# filter_seq_length("../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_90_pos.fasta",
#                   "../data/split_data/round3/preprocess_level1_length_filter/ACP_90_pos_preprocess_level1.fasta", 4, 51)
# filter_seq_length("../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_90_neg.fasta",
#                   "../data/split_data/round3/preprocess_level1_length_filter/ACP_90_neg_preprocess_level1.fasta", 4, 51)
# count_seq_samples(
#     "../data/split_data/round3/preprocess_level1_length_filter/ACP_90_pos_preprocess_level1.fasta")  # 470
# count_seq_samples(
#     "../data/split_data/round3/preprocess_level1_length_filter/ACP_90_neg_preprocess_level1.fasta")  # 4244

# filter_seq_length("../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_80_pos.fasta",
#                   "../data/split_data/round3/preprocess_level1_length_filter/ACP_80_pos_preprocess_level1.fasta"
#                   , 4, 51)
# filter_seq_length("../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_80_neg.fasta",
#                   "../data/split_data/round3/preprocess_level1_length_filter/ACP_80_neg_preprocess_level1.fasta"
#                   , 4, 51)
# count_seq_samples(
#     "../data/split_data/round3/preprocess_level1_length_filter/ACP_80_pos_preprocess_level1.fasta")  # 341
# count_seq_samples(
#     "../data/split_data/round3/preprocess_level1_length_filter/ACP_80_neg_preprocess_level1.fasta")  # 4082


# filter_seq_length("../data/ACP_dataset/fasta/ACP_mixed_all_pos_neg.fasta",
#                   "../data/split_data/round3/preprocess_level1_length_filter/ACP_mixed_all_pos_neg_preprocess_level1.fasta"
#                   , 4, 51)
# count_seq_samples(
#     "../data/split_data/round3/preprocess_level1_length_filter/ACP_mixed_all_pos_neg_preprocess_level1.fasta")  # 5190

from Bio import SeqIO


def check_seq_length(fasta_file_name, output_file):
    result = []
    c = 0
    for seq_record in SeqIO.parse(open(fasta_file_name, mode='r'), 'fasta'):
        if 10 < len(seq_record) < 100:
            c += 1
            result.append(seq_record)

    SeqIO.write(result, output_file, "fasta")
    print("C : ", c)


def count_seq_samples(fasta_input_file):
    count_seq = len([1 for line in open(fasta_input_file) if line.startswith(">")])
    return count_seq

# check_seq_length("../../data/ACP_dataset/fasta/ACP-Mixed-100.fasta", "ACP-Mixed-100_preprocess_level1.fasta")
# check_seq_length("../../data/ACP_dataset/fasta/ACP-Mixed-90.fasta", "ACP-Mixed-90_preprocess_level1.fasta")
# check_seq_length("../../data/ACP_dataset/fasta/ACP-Mixed-80.fasta", "ACP-Mixed-80_preprocess_level1.fasta")
# count_seq_samples("ACP-Mixed-100_preprocess_level1.fasta", None)  # 4785
# count_seq_samples("ACP-Mixed-90_preprocess_level1.fasta", None)  # 4322
# count_seq_samples("ACP-Mixed-80_preprocess_level1.fasta", None)  # 4066

# check_seq_length("../../data/split_data/ACP_100_pos.fasta", "ACP_100_pos_preprocess_level1.fasta")
# check_seq_length("../../data/split_data/ACP_100_neg.fasta", "ACP_100_neg_preprocess_level1.fasta")
# count_seq_samples("ACP_100_pos_preprocess_level1.fasta", None)  #
# count_seq_samples("ACP_100_neg_preprocess_level1.fasta", None)  #
#
# check_seq_length("../../data/split_data/ACP_90_pos.fasta", "ACP_90_pos_preprocess_level1.fasta")
# check_seq_length("../../data/split_data/ACP_90_neg.fasta", "ACP_90_neg_preprocess_level1.fasta")
# count_seq_samples("ACP_90_pos_preprocess_level1.fasta", None)  #
# count_seq_samples("ACP_90_neg_preprocess_level1.fasta", None)  #

# check_seq_length("../../data/split_data/ACP_80_pos.fasta", "ACP_80_pos_preprocess_level1.fasta")
# check_seq_length("../../data/split_data/ACP_80_neg.fasta", "ACP_80_neg_preprocess_level1.fasta")
# count_seq_samples("ACP_80_pos_preprocess_level1.fasta", None)  #
# count_seq_samples("ACP_80_neg_preprocess_level1.fasta", None)  #

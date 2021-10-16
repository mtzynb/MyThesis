from Bio import SeqIO


def get_seq_by_class_label(file_name, class_label, output_file):
    query = "|" + class_label
    result = []
    for seq_record in SeqIO.parse(open(file_name, mode='r'), 'fasta'):
        if query in seq_record.id:
            result.append(seq_record)

    SeqIO.write(result, output_file, "fasta")

    return result


def split_all_data():
    get_seq_by_class_label("../data/new_cdhit/round3/corrected_files/new-corrected-ACP-Mixed-80.fasta", "1",
                           "../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_80_pos.fasta")
    get_seq_by_class_label("../data/new_cdhit/round3/corrected_files/new-corrected-ACP-Mixed-80.fasta", "0",
                           "../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_80_neg.fasta")

    get_seq_by_class_label("../data/new_cdhit/round3/corrected_files/new-corrected-ACP-Mixed-90.fasta", "1",
                           "../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_90_pos.fasta")
    get_seq_by_class_label("../data/new_cdhit/round3/corrected_files/new-corrected-ACP-Mixed-90.fasta", "0",
                           "../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_90_neg.fasta")

split_all_data()
print("done")

from Bio import SeqIO


def correct_fasta_file(input_fasta, output_fasta):
    with open(input_fasta) as f:
        seqs = SeqIO.parse(f, "fasta")
        seqs_list = list(seqs)
        SeqIO.write(seqs_list, output_fasta, "fasta")  # write samples in a new file


def get_data_frame_from_fasta_file(fasta_file):
    return SeqIO.parse(open(fasta_file, mode='r'), 'fasta')


def write_data_frame_to_fasta_file(input_df, output_fasta_file):
    SeqIO.write(input_df, output_fasta_file, "fasta")
    print("write_data_frame_to_fasta_file DONE!")

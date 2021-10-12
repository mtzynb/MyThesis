from Bio import SeqIO


def correct_fasta_file(input_fasta, output_fasta):
    with open(input_fasta) as f:
        seqs = SeqIO.parse(f, "fasta")
        seqs_list = list(seqs)
        SeqIO.write(seqs_list, output_fasta, "fasta")  # write samples in a new file



import numpy as np
import pylab
from Bio import SeqIO


def draw_line_plot(fasta_input_file, plot_title, plot_out_file, x_text, y_text):
    len_of_records = [len(rec.seq) for rec in SeqIO.parse(fasta_input_file, "fasta")]
    length, count = np.unique(len_of_records, return_counts=True)
    max_len = max(length)
    min_len = min(length)
    print(length)
    print(count)
    print("max_len: " + str(max_len))
    print("min_len: " + str(min_len))

    pylab.xlabel('Peptide Sequence Length')
    pylab.ylabel('Count of Peptides')
    pylab.title(plot_title)
    pylab.text(x_text, y_text, 'MAX_Length=' + str(max_len) + '\nMIN_Length=' + str(min_len) +
               '\nTotal Count=' + str(sum(count)))
    pylab.grid()
    pylab.plot(length, count)
    pylab.savefig(plot_out_file)

    pylab.cla()
    pylab.clf()


def draw_all_plots():
    # -----------------------------
    draw_line_plot('../../../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_80_pos.fasta', 'Plot of ACP Peptide Sequences With 80% cd-hit ',
                   'plots/ACP_80_pos', 150, 30)
    draw_line_plot('../../../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_80_neg.fasta', 'Plot of non-ACP Peptide Sequences With 80% cd-hit ',
                   'plots/ACP_80_neg', 60, 120)
    # -----------------------------
    draw_line_plot('../../../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_90_pos.fasta', 'Plot of ACP Peptide Sequences With 90% cd-hit ',
                   'plots/ACP_90_pos', 150, 35)
    draw_line_plot('../../../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_90_neg.fasta', 'Plot of non-ACP Peptide Sequences With 90% cd-hit ',
                   'plots/ACP_90_neg', 70, 120)
    # -----------------------------
    # draw_line_plot('../data/ACP_dataset/fasta/ACP_mixed_all_pos.fasta',
    #                'Plot of Original ACP Peptide Sequences Length(no cd-hit)',
    #                'Original_ACP_pos', 150, 65)
    # draw_line_plot('../data/ACP_dataset/fasta/ACP_mixed_all_neg.fasta',
    #                'Plot of Original non-ACP Peptide Sequences Length(no cd-hit)',
    #                'Original_ACP_neg', 70, 150)
    # -----------------------------


draw_all_plots()

print("DONE!")

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


def draw_all_plots(data_base_dir):
    draw_line_plot(data_base_dir + 'ACP-Mixed-80_preprocess_level1.fasta',
                   'Plot of ACP Peptide Sequences With 80% cd-hit ',
                   'ACP_80_mixed', 37, 140)
    draw_line_plot(data_base_dir + 'ACP_80_pos_preprocess_level1.fasta',
                   'Plot of ACP Peptide Sequences With 80% cd-hit ',
                   'ACP_80_pos', 35, 32)
    draw_line_plot(data_base_dir + 'ACP_80_neg_preprocess_level1.fasta',
                   'Plot of non-ACP Peptide Sequences With 80% cd-hit ',
                   'ACP_80_neg', 37, 125)
    # -----------------------------
    draw_line_plot(data_base_dir + 'ACP-Mixed-90_preprocess_level1.fasta',
                   'Plot of ACP Peptide Sequences With 90% cd-hit ',
                   'ACP_90_mixed', 35, 160)
    draw_line_plot(data_base_dir + 'ACP_90_pos_preprocess_level1.fasta',
                   'Plot of ACP Peptide Sequences With 90% cd-hit ',
                   'ACP_90_pos', 35, 35)
    draw_line_plot(data_base_dir + 'ACP_90_neg_preprocess_level1.fasta',
                   'Plot of non-ACP Peptide Sequences With 90% cd-hit ',
                   'ACP_90_neg', 38, 142)
    # -----------------------------
    draw_line_plot(data_base_dir + 'ACP_mixed_all_pos_neg_preprocess_level1.fasta',
                   'Plot of Original ACP Peptide Sequences Length(no cd-hit)',
                   'Mixed_ACP_Main', 35, 175)
    # -----------------------------


data_base_dir = '../../../data/split_data/round3/preprocess_level1_length_filter/'
draw_all_plots(data_base_dir)

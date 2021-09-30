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
    draw_line_plot('../../data/split_data/test_train_data_main/mixed_data/test_mixed_80.fasta',
                   'Plot of Test Mixed ACP and non-ACP Peptide Sequences With 80% cd-hit ',
                   'test_mixed_80', 60, 9)
    draw_line_plot('../../data/split_data/test_train_data_main/mixed_data/train_mixed_80.fasta',
                   'Plot of Train Mixed ACP and non-ACP Peptide Sequences With 80% cd-hit ',
                   'train_mixed_80', 70, 30)
    # -----------------------------
    draw_line_plot('../../data/split_data/test_train_data_main/mixed_data/test_mixed_90.fasta',
                   'Plot of Test Mixed ACP and non-ACP Peptide Sequences With 90% cd-hit ',
                   'test_mixed_90', 50, 10)
    draw_line_plot('../../data/split_data/test_train_data_main/mixed_data/train_mixed_90.fasta',
                   'Plot of Train Mixed ACP and non-ACP Peptide Sequences With 90% cd-hit ',
                   'train_mixed_90', 70, 35)
    # -----------------------------
    draw_line_plot('../../data/split_data/test_train_data_main/mixed_data/test_mixed_100.fasta',
                   'Plot of Test Mixed ACP and non-ACP Peptide Sequences With 100% cd-hit ',
                   'test_mixed_100', 60, 15)
    draw_line_plot('../../data/split_data/test_train_data_main/mixed_data/train_mixed_100.fasta',
                   'Plot of Train Mixed ACP and non-ACP Peptide Sequences With 100% cd-hit ',
                   'train_mixed_100', 70, 70)
    # -----------------------------


draw_all_plots()

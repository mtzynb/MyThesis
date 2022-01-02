import numpy as np
import pylab
from Bio import SeqIO
from bidi.algorithm import get_display
from arabic_reshaper import reshape


def draw_line_plot(fasta_input_file, plot_title, plot_out_file, x_text, y_text):
    len_of_records = [len(rec.seq) for rec in SeqIO.parse(fasta_input_file, "fasta")]
    length, count = np.unique(len_of_records, return_counts=True)
    max_len = max(length)
    min_len = min(length)
    print(length)
    print(count)
    print("max_len: " + str(max_len))
    print("min_len: " + str(min_len))

    pylab.xlabel(get_display(reshape('طول توالی پپتیدها')))
    pylab.ylabel(get_display(reshape('تعداد پپتیدها')))
    pylab.title(plot_title)
    pylab.text(x_text, y_text,
               get_display(reshape('=ماکزیمم طول ')) + str(max_len) + get_display(reshape('\n=مینیمم طول ')) +
               str(min_len) + get_display(reshape('\n=تعداد کل توالی ها'))
               + str(sum(count)))
    pylab.grid()
    pylab.plot(length, count)
    pylab.savefig(plot_out_file)

    pylab.cla()
    pylab.clf()


def draw_all_plots():
    # -----------------------------
    # draw_line_plot(
    #     '../../../data/split_data/round3/combine_random_neg_with_equal_pos_data/ACP_Mixed_equal_pos_neg_80.fasta',
    #     'Equal Mixed ACP,non-ACP Peptide Seqs With 80% cdhit (random neg)',
    #     'ACP_Mixed_equal_pos_neg_80', 35, 36)

    # -----------------------------

    title_all = 'نمودار تمام پپتیدهای ضدسرطانی و غیرضدسرطانی'

    draw_line_plot(
        '../../../data/split_data/round3/combine_random_neg_with_equal_pos_data/ACP_Mixed_equal_pos_neg_90.fasta',
        # 'Equal Mixed ACP,non-ACP Peptide Seqs With 90% cdhit (random neg)',
        get_display(reshape(title_all)),
        'ACP_Mixed_equal_pos_neg_90_farsi', 35, 48)
    # -----------------------------


draw_all_plots()

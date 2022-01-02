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


def draw_all_plots(data_base_dir):
    # draw_line_plot(data_base_dir + 'ACP_80_neg_random.fasta',
    #                'Plot of non-ACP Peptide Sequences With 80% cd-hit ',
    #                'ACP_80_neg', 38, 12)
    # -----------------------------
    title_neg = 'نمودار طول توالی پپتیدهای غیرضدسرطانی پس از انتخاب رندوم'
    draw_line_plot(data_base_dir + 'ACP_90_neg_random.fasta',
                   get_display(reshape(title_neg)),
                   'ACP_90_neg_farsi', 35, 17)
    # -----------------------------


data_base_dir = '../../../../data/split_data/round3/random_neg_data/'
draw_all_plots(data_base_dir)

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
    # -----------------------------
    title_all = 'نمودار طول همه پپتیدهای cdhit90 پس از اعمال فیلتر طول'
    title_pos = 'نمودار طول پپتیدهای ضدسرطانی cdhit90 پس از اعمال فیلتر طول'
    title_neg = 'نمودار طول پپتیدهای غیرضدسرطانی cdhit90 پس از اعمال فیلتر طول'

    draw_line_plot(data_base_dir + 'ACP-Mixed-90_preprocess_level1.fasta',
                   get_display(reshape(title_all)),
                   'ACP_90_mixed_farsi', 35, 160)
    draw_line_plot(data_base_dir + 'ACP_90_pos_preprocess_level1.fasta',
                   get_display(reshape(title_pos)),
                   'ACP_90_pos_farsi', 35, 35)
    draw_line_plot(data_base_dir + 'ACP_90_neg_preprocess_level1.fasta',
                   get_display(reshape(title_neg)),
                   'ACP_90_neg_farsi', 34, 142)
    # -----------------------------

    # -----------------------------


data_base_dir = '../../../data/split_data/round3/preprocess_level1_length_filter/'
draw_all_plots(data_base_dir)

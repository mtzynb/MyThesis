import numpy as np
import pylab
from Bio import SeqIO
from bidi.algorithm import get_display
from arabic_reshaper import reshape


def en_to_fa(num, formatter='%1.1f%%'):
    num_as_string = formatter % num
    mapping = dict(list(zip('0123456789.%', '۰۱۲۳۴۵۶۷۸۹%')))
    return ''.join(mapping[digit] for digit in num_as_string)


def draw_line_plot(fasta_input_file, plot_title, plot_out_file, x_text, y_text):
    len_of_records = [len(rec.seq) for rec in SeqIO.parse(fasta_input_file, "fasta")]
    length, count = np.unique(len_of_records, return_counts=True)
    max_len = max(length)
    min_len = min(length)
    print(length)
    print(count)
    print("max_len: " + str(max_len))
    print("min_len: " + str(min_len))
    font = {"family": "Sahel", "size": 12}

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
    title_pos = 'نمودار طول توالی پپتیدهای ضدسرطانی پس از اعمال cd-hit 80%'
    title_neg = 'نمودار طول توالی پپتیدهای غیرضدسرطانی پس از اعمال cd-hit 80%'
    draw_line_plot('../../../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_80_pos.fasta',
                   get_display(reshape(title_pos)),
                   'ACP_80_pos_farsi', 150, 30)
    draw_line_plot('../../../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_80_neg.fasta',
                   get_display(reshape(title_neg)),
                   'ACP_80_neg_farsi', 60, 120)
    # # -----------------------------
    # title_pos = 'نمودار طول توالی پپتیدهای ضدسرطانی پس از اعمال cd-hit 90%'
    # title_neg = 'نمودار طول توالی پپتیدهای غیرضدسرطانی پس از اعمال cd-hit 90%'
    # draw_line_plot('../../../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_90_pos.fasta',
    #                get_display(reshape(title_pos)),
    #                'ACP_90_pos_farsi', 150, 35)
    # draw_line_plot('../../../data/split_data/round3/raw_data_after_split_pos_and_neg/ACP_90_neg.fasta',
    #                get_display(reshape(title_neg)),
    #                'ACP_90_neg_farsi', 70, 120)
    # -----------------------------
    # title_pos = 'نمودار طول توالی پپتیدهای ضدسرطانی بدون اعمال cd-hit'
    # title_neg = 'نمودار طول توالی پپتیدهای غیرضدسرطانی بدون اعمال cd-hit'
    #
    # draw_line_plot('../../../data/ACP_dataset/fasta/ACP_mixed_all_pos.fasta',
    #                get_display(reshape(title_pos)),
    #                'Original_ACP_pos_farsi', 150, 65)
    #
    # draw_line_plot('../../../data/ACP_dataset/fasta/ACP_mixed_all_neg.fasta',
    #                get_display(reshape(title_neg)),
    #                'Original_ACP_neg_farsi', 70, 150)
    # -----------------------------


draw_all_plots()

print("DONE!")

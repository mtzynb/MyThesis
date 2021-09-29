from Bio import SeqIO
import random
from get_random_seq import get_random_seq

data_pos_dir100 = '../data/split_data/preprocess_level1_length_filter/ACP_100_pos_preprocess_level1.fasta'
data_neg_dir100 = '../data/split_data/preprocess_level1_length_filter/ACP_100_neg_preprocess_level1.fasta'
output_new_neg_file100 = '../data/split_data/random_neg_data/ACP_100_neg_random.fasta'

# data_pos_dir90 = '../data/split_data/preprocess_level1_length_filter/ACP_90_pos_preprocess_level1.fasta'
# data_neg_dir90 = '../data/split_data/preprocess_level1_length_filter/ACP_90_neg_preprocess_level1.fasta'
# output_new_neg_file90 = '../data/split_data/random_neg_data/ACP_90_neg_random.fasta'

# data_pos_dir80 = '../data/split_data/preprocess_level1_length_filter/ACP_80_pos_preprocess_level1.fasta'
# data_neg_dir80 = '../data/split_data/preprocess_level1_length_filter/ACP_80_neg_preprocess_level1.fasta'
# output_new_neg_file80 = '../data/split_data/random_neg_data/ACP_80_neg_random.fasta'

# count_pos_seq100 = count_seq_samples(data_pos_dir100)
# print("count_pos_seq100: ", count_pos_seq100)
# get_random_seq(data_neg_dir100, count_pos_seq100, output_new_neg_file100)

# count_pos_seq90 = count_seq_samples(data_pos_dir90)
# print("count_pos_seq90: ", count_pos_seq90)
# get_random_seq(data_neg_dir90, count_pos_seq90, output_new_neg_file90)

# count_pos_seq80 = count_seq_samples(data_pos_dir80)
# print("count_pos_seq80: ", count_pos_seq80)
# get_random_seq(data_neg_dir80, count_pos_seq80, output_new_neg_file80)

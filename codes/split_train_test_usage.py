from split_train_test_data_split import calc_test_train_data_count, split_train_test_data
from preprocess_data import count_seq_samples

## --------------------------------------------------------------------------
input_data_pos_dir100 = '../data/split_data/preprocess_level1_length_filter/ACP_100_pos_preprocess_level1.fasta'
input_data_neg_dir100 = '../data/split_data/random_neg_data/ACP_100_neg_random.fasta'
train_100_pos_dir = '../data/split_data/test_train_data_main/cdhit100/train_100_pos.fasta'
train_100_neg_dir = '../data/split_data/test_train_data_main/cdhit100/train_100_neg.fasta'
test_100_pos_dir = '../data/split_data/test_train_data_main/cdhit100/test_100_pos.fasta'
test_100_neg_dir = '../data/split_data/test_train_data_main/cdhit100/test_100_neg.fasta'

count_pos_seq = count_seq_samples(input_data_pos_dir100)
print("count_seqs cdhit100: ", count_pos_seq)
train_count, test_count = calc_test_train_data_count(count_pos_seq * 2, 0.8)
print('train_count:  {}, test_count: {}'.format(train_count, test_count))
pos_train_count = int(train_count / 2)

split_train_test_data(input_data_pos_dir100, train_100_pos_dir, test_100_pos_dir, pos_train_count)
split_train_test_data(input_data_neg_dir100, train_100_neg_dir, test_100_neg_dir, pos_train_count)
## --------------------------------------------------------------------------

input_data_pos_dir90 = '../data/split_data/preprocess_level1_length_filter/ACP_90_pos_preprocess_level1.fasta'
input_data_neg_dir90 = '../data/split_data/random_neg_data/ACP_90_neg_random.fasta'
train_90_pos_dir = '../data/split_data/test_train_data_main/cdhit90/train_90_pos.fasta'
train_90_neg_dir = '../data/split_data/test_train_data_main/cdhit90/train_90_neg.fasta'
test_90_pos_dir = '../data/split_data/test_train_data_main/cdhit90/test_90_pos.fasta'
test_90_neg_dir = '../data/split_data/test_train_data_main/cdhit90/test_90_neg.fasta'

count_pos_seq = count_seq_samples(input_data_pos_dir90)
print("count_seqs cdhit90: ", count_pos_seq)
train_count, test_count = calc_test_train_data_count(count_pos_seq * 2, 0.8)
print('train_count:  {}, test_count: {}'.format(train_count, test_count))
pos_train_count = int(train_count / 2)

split_train_test_data(input_data_pos_dir90, train_90_pos_dir, test_90_pos_dir, pos_train_count)
split_train_test_data(input_data_neg_dir90, train_90_neg_dir, test_90_neg_dir, pos_train_count)
## --------------------------------------------------------------------------
input_data_pos_dir80 = '../data/split_data/preprocess_level1_length_filter/ACP_80_pos_preprocess_level1.fasta'
input_data_neg_dir80 = '../data/split_data/random_neg_data/ACP_80_neg_random.fasta'
train_80_pos_dir = '../data/split_data/test_train_data_main/cdhit80/train_80_pos.fasta'
train_80_neg_dir = '../data/split_data/test_train_data_main/cdhit80/train_80_neg.fasta'
test_80_pos_dir = '../data/split_data/test_train_data_main/cdhit80/test_80_pos.fasta'
test_80_neg_dir = '../data/split_data/test_train_data_main/cdhit80/test_80_neg.fasta'

count_pos_seq = count_seq_samples(input_data_pos_dir80)
print("count_seqs cdhit80: ", count_pos_seq)
train_count, test_count = calc_test_train_data_count(count_pos_seq * 2, 0.8)
print('train_count:  {}, test_count: {}'.format(train_count, test_count))
pos_train_count = int(train_count / 2)

split_train_test_data(input_data_pos_dir80, train_80_pos_dir, test_80_pos_dir, pos_train_count)
split_train_test_data(input_data_neg_dir80, train_80_neg_dir, test_80_neg_dir, pos_train_count)

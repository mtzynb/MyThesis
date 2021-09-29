from preprocess_data import combine_pos_neg_data_in_a_single_file

train_100_pos_dir = '../data/split_data/test_train_data_main/cdhit100/train_100_pos.fasta'
train_100_neg_dir = '../data/split_data/test_train_data_main/cdhit100/train_100_neg.fasta'
test_100_pos_dir = '../data/split_data/test_train_data_main/cdhit100/test_100_pos.fasta'
test_100_neg_dir = '../data/split_data/test_train_data_main/cdhit100/test_100_neg.fasta'

train_100_mixed_dir = '../data/split_data/test_train_data_main/cdhit100/train_100_mixed.fasta'
test_100_mixed_dir = '../data/split_data/test_train_data_main/cdhit100/test_100_mixed.fasta'

print("start combining TRAIN cdhit 100% data...")
combine_pos_neg_data_in_a_single_file(train_100_pos_dir, train_100_neg_dir, train_100_mixed_dir)

print("start combining TEST cdhit 100% data...")
combine_pos_neg_data_in_a_single_file(test_100_pos_dir, test_100_neg_dir, test_100_mixed_dir)

print("End combining cdhit 100% data...")

## --------------------------------------------------------------------------
#
# train_90_pos_dir = '../data/split_data/test_train_data_main/cdhit90/train_90_pos.fasta'
# train_90_neg_dir = '../data/split_data/test_train_data_main/cdhit90/train_90_neg.fasta'
# test_90_pos_dir = '../data/split_data/test_train_data_main/cdhit90/test_90_pos.fasta'
# test_90_neg_dir = '../data/split_data/test_train_data_main/cdhit90/test_90_neg.fasta'
#
# print("start calculating cdhit 90% data...")
# train_90_pos_count = count_seq_samples(train_90_pos_dir)
# print("train_90_pos_dir: ", train_90_pos_count)
#
# train_90_neg_count = count_seq_samples(train_90_neg_dir)
# print("train_90_neg_dir: ", train_90_neg_count)
#
# test_90_pos_count = count_seq_samples(test_90_pos_dir)
# print("test_90_pos_dir: ", test_90_pos_count)
#
# test_90_neg_count = count_seq_samples(test_90_neg_dir)
# print("test_90_neg_dir: ", test_90_neg_count)
# ## --------------------------------------------------------------------------
#
# train_80_pos_dir = '../data/split_data/test_train_data_main/cdhit80/train_80_pos.fasta'
# train_80_neg_dir = '../data/split_data/test_train_data_main/cdhit80/train_80_neg.fasta'
# test_80_pos_dir = '../data/split_data/test_train_data_main/cdhit80/test_80_pos.fasta'
# test_80_neg_dir = '../data/split_data/test_train_data_main/cdhit80/test_80_neg.fasta'
#
# print("start calculating cdhit 80% data...")
# train_80_pos_count = count_seq_samples(train_80_pos_dir)
# print("train_80_pos_dir: ", train_80_pos_count)
#
# train_80_neg_count = count_seq_samples(train_80_neg_dir)
# print("train_80_neg_dir: ", train_80_neg_count)
#
# test_80_pos_count = count_seq_samples(test_80_pos_dir)
# print("test_80_pos_dir: ", test_80_pos_count)
#
# test_80_neg_count = count_seq_samples(test_80_neg_dir)
# print("test_80_neg_dir: ", test_80_neg_count)
# ## --------------------------------------------------------------------------

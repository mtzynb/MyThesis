from preprocess_dataaa import count_seq_samples

train_mixed_100_dir = '../data/split_data/round2/test_train_data_main/mixed_data/train_mixed_100.fasta'
test_mixed_100_dir = '../data/split_data/round2/test_train_data_main/mixed_data/test_mixed_100.fasta'

print("start counting cdhit 100% data...")
train_100_mixed_count = count_seq_samples(train_mixed_100_dir)
print("train_100_mixed_count: ", train_100_mixed_count)

test_100_mixed_count = count_seq_samples(test_mixed_100_dir)
print("test_100_mixed_count: ", test_100_mixed_count)
## --------------------------------------------------------------------------
train_mixed_90_dir = '../data/split_data/round2/test_train_data_main/mixed_data/train_mixed_90.fasta'
test_mixed_90_dir = '../data/split_data/round2/test_train_data_main/mixed_data/test_mixed_90.fasta'

print("start counting cdhit 90% data...")
train_90_mixed_count = count_seq_samples(train_mixed_90_dir)
print("train_90_mixed_count: ", train_90_mixed_count)

test_90_mixed_count = count_seq_samples(test_mixed_90_dir)
print("test_90_mixed_count: ", test_90_mixed_count)
## --------------------------------------------------------------------------
train_mixed_80_dir = '../data/split_data/round2/test_train_data_main/mixed_data/train_mixed_80.fasta'
test_mixed_80_dir = '../data/split_data/round2/test_train_data_main/mixed_data/test_mixed_80.fasta'

print("start counting cdhit 80% data...")
train_80_mixed_count = count_seq_samples(train_mixed_80_dir)
print("train_80_mixed_count: ", train_80_mixed_count)

test_80_mixed_count = count_seq_samples(test_mixed_80_dir)
print("test_80_mixed_count: ", test_80_mixed_count)
## --------------------------------------------------------------------------

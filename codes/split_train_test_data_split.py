import math
import random

from Bio import SeqIO


def calc_test_train_data_count(no_of_whole_data, percentage_of_data_to_use_for_train):
    train_data_count = math.ceil(no_of_whole_data * percentage_of_data_to_use_for_train)
    test_data_count = no_of_whole_data - train_data_count

    return train_data_count, test_data_count


def split_train_test_data(input_data, output_train_file, output_test_file, train_split_count):
    records = list(SeqIO.parse(input_data, "fasta"))

    random.seed(25)
    train_data = random.sample(records, train_split_count)
    train_data_id = [train_data[i].id for i in range(len(train_data))]
    records_id = [records[i].id for i in range(len(records))]

    print("records_id len", len(records_id))
    print("train_data_id len", len(train_data_id))

    test_data_id = list(set(records_id) - set(train_data_id))
    print("test_data_id len", len(test_data_id))

    test_data = []

    for i in range(len(records)):
        for j in range(len(test_data_id)):
            if records[i].id == test_data_id[j]:
                test_data.append(records[i])

    print("train_data : ", len(train_data))
    print("test_data : ", len(test_data))

    SeqIO.write(train_data, output_train_file, "fasta")
    SeqIO.write(test_data, output_test_file, "fasta")

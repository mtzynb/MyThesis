from fasta_file_utils import correct_fasta_file
from preprocess_dataaa import count_seq_samples_by_class_label


# ------------ correct cdhit 90 fasta file --------------
input_fasta_cdhit90 = '../data/new_cdhit/new-ACP-Mixed-90.fasta'
output_fasta_cdhit90 = '../data/new_cdhit/corrected_files/new-corrected-ACP-Mixed-90.fasta'

# correct_fasta_file(input_fasta_cdhit90, output_fasta_cdhit90)

before_correct_count = count_seq_samples_by_class_label(input_fasta_cdhit90, "0")
after_correct_count = count_seq_samples_by_class_label(output_fasta_cdhit90, "0")
print("before correct cdhit90 file, seq count is : ", before_correct_count)
print("after correct cdhit90 file, seq count is : ", after_correct_count)


# ------------ correct cdhit 80 fasta file --------------
input_fasta_cdhit80 = '../data/new_cdhit/new-ACP-Mixed-80.fasta'
output_fasta_cdhit80 = '../data/new_cdhit/corrected_files/new-corrected-ACP-Mixed-80.fasta'

# correct_fasta_file(input_fasta_cdhit80, output_fasta_cdhit80)

before_correct_count = count_seq_samples_by_class_label(input_fasta_cdhit80, "0")
after_correct_count = count_seq_samples_by_class_label(output_fasta_cdhit80, "0")
print("before correct cdhit80 file, seq count is : ", before_correct_count)
print("after correct cdhit80 file, seq count is : ", after_correct_count)

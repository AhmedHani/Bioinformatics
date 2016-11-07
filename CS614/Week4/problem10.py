___author__ = 'Ahmed Hani Ibrahim'

from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from strings_algorithms import StringsAlgorithms
import os

#A_ACCT_TGG
#ACAC_TGTGA
#AACTTG

def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem10')
    solution_dir = os.path.join("Problems", "Problem10Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()

    for train_i in range(0, len(output)):
        alpha_dna, beta_dna = test_cases[train_i]
        case_output = output[train_i]
        strings_algorithms = StringsAlgorithms(alpha_dna, beta_dna)
        lcs = strings_algorithms.lcs('dp')
        print(len(lcs))

        if len(case_output) != len(lcs):
            raise Exception("Output not matched!\nExpecting: " + str(case_output) + "\nFound: " + str(lcs))

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output), len(test_cases)):
        usage.start()
        alpha_dna, beta_dna = test_cases[test_i]
        strings_algorithms = StringsAlgorithms(alpha_dna, beta_dna)
        lcs = strings_algorithms.lcs('dp')
        print(len(lcs))
        usage.end()

        #writer.write_data(test_i + 1, lcs, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + alpha_dna + "\n" + beta_dna + "\n")

        print("\n\nOutput")
        print("=====")

        print(lcs)

        print("\n")
        print("======")
        print("Execution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Used: " + str(usage.get_memory_usage()) + " MB")


if __name__ == '__main__':
    main()

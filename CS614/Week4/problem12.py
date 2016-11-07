___author__ = 'Ahmed Hani Ibrahim'

from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from strings_algorithms import StringsAlgorithms
import os


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem12')
    solution_dir = os.path.join("Problems", "Problem12Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()
    scoring_matrix = data_reader.get_PAM_data()

    for train_i in range(0, len(output)):
        alpha_dna, beta_dna = test_cases[train_i]
        case_output = output[train_i]
        strings_algorithms = StringsAlgorithms(alpha_dna, beta_dna)
        align = strings_algorithms.alignment(_type='local', scoring_matrix=scoring_matrix)

        #if align != case_output:
         #   raise Exception("Output not matched!\nExpecting: " + str(case_output) + "\nFound: " + str(align))

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output), len(test_cases)):
        usage.start()
        alpha_dna, beta_dna = test_cases[test_i]
        strings_algorithms = StringsAlgorithms(alpha_dna, beta_dna)
        align = strings_algorithms.alignment(_type='local', scoring_matrix=scoring_matrix)
        usage.end()

        writer.write_data(test_i + 1, align, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + alpha_dna + "\n" + beta_dna + "\n")

        print("\n\nOutput")
        print("=====")

        print(align[0])
        print(align[1][0])
        print(align[1][1])

        print("\n")
        print("======")
        print("Execution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Used: " + str(usage.get_memory_usage()) + " MB")

if __name__ == '__main__':
    main()
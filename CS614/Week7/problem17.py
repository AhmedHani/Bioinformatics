___author__ = 'Ahmed Hani Ibrahim'


from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from dna import DNA
import os


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem17')
    solution_dir = os.path.join("Problems", "Problem17Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()

    for train_i in range(0, len(output)):
        dna = test_cases[train_i][0]
        k = test_cases[train_i][1][0]
        score_matrix = test_cases[train_i][1][1]
        case_output = output[train_i]
        most_probable_k_mer = DNA(dna).get_most_probable_k_mer(int(k), score_matrix)

        if most_probable_k_mer != case_output:
            raise Exception("Output not matched!\nExpecting: " + str(case_output) + "\nFound: " + str(most_probable_k_mer))

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output) - 1, len(test_cases)):
        usage.start()
        dna = test_cases[test_i][0]
        k = test_cases[test_i][1][0]
        score_matrix = test_cases[test_i][1][1]
        most_probable_k_mer = DNA(dna).get_most_probable_k_mer(int(k), score_matrix)
        usage.end()

        writer.write_data(test_i + 1, most_probable_k_mer, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + str(dna) + "\n" + str(k) + "\n" + str(score_matrix))

        print("\n\nOutput")
        print("=====")

        print(most_probable_k_mer)

        print("\n")
        print("======")
        print("Execution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Used: " + str(usage.get_memory_usage()) + " MB")

if __name__ == '__main__':
    main()



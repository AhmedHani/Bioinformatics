___author__ = 'Ahmed Hani Ibrahim'


from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from graph_algorithms import Graph
import os


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem15')
    solution_dir = os.path.join("Problems", "Problem15Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()

    for train_i in range(0, len(output)):
        k = test_cases[train_i][0]
        dna = test_cases[train_i][1]
        graph = Graph()
        adj_list = graph.get_debruijn_graph(_type='string', k=int(k), dna_string=dna)
        case_output = output[train_i]

        if sorted(adj_list.items()) != sorted(case_output.items()):
            raise Exception("Output not matched!\nExpecting: " + str(sorted(case_output.items())) + "\nFound: " + str(sorted(adj_list.items())))

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output), len(test_cases)):
        usage.start()
        k = test_cases[test_i][0]
        dna = test_cases[test_i][1]
        adj_list = Graph().get_debruijn_graph(_type='string', k=int(k), dna_string=dna)
        usage.end()

        writer.write_data(test_i + 1, adj_list, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + str(k) + "\n" + dna + "\n")

        print("\n\nOutput")
        print("=====")

        print(adj_list)

        print("\n")
        print("======")
        print("Execution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Used: " + str(usage.get_memory_usage()) + " MB")

if __name__ == '__main__':
    main()
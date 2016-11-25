___author__ = 'Ahmed Hani Ibrahim'


from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from graph_algorithms import Graph
import os


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem16')
    solution_dir = os.path.join("Problems", "Problem16Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()

    for train_i in range(0, len(output)):
        k_mers = test_cases[train_i]
        graph = Graph()
        adj_list = graph.get_debruijn_graph(_type='k_mers', k_mers=k_mers)
        case_output = output[train_i]

        if sorted(adj_list.items()) != sorted(case_output.items()):
            raise Exception("Output not matched!\nExpecting: " + str(sorted(case_output.items())) + "\nFound: " + str(sorted(adj_list.items())))

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output), len(test_cases)):
        usage.start()
        k_mers = test_cases[test_i]
        adj_list = Graph().get_debruijn_graph(_type='k_mers', k_mers=k_mers)
        usage.end()

        writer.write_data(test_i + 1, adj_list, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + str(k_mers) + "\n")

        print("\n\nOutput")
        print("=====")

        print(adj_list)

        print("\n")
        print("======")
        print("Execution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Used: " + str(usage.get_memory_usage()) + " MB")

if __name__ == '__main__':
    main()
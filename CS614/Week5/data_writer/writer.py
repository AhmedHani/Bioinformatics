___author__ = 'Ahmed Hani Ibrahim'

import os


class DataWriter(object):
    def __init__(self, solution_dir):
        self.__solution_dir = solution_dir

    def write_data(self, file_index, output_, running_time, memory_used):
        if "Problem13" in self.__solution_dir:
            with open(os.path.join(self.__solution_dir, "output" + str(file_index) + ".txt"), 'w') as writer:
                output_.sort()
                writer.write('\n'.join(map(lambda v: str(v), output_)))

                writer.write("\n\n\n")
                writer.write("======")
                writer.write("\n")
                writer.write("Execution Time: " + str(running_time) + " s")
                writer.write("\n")
                writer.write("Memory Used: " + str(memory_used) + " MB")

        if "Problem14" in self.__solution_dir:
            with open(os.path.join(self.__solution_dir, "output" + str(file_index) + ".txt"), 'w') as writer:
                for edge in sorted(output_.items()):
                    writer.write(str(edge[0] + " -> " + str(edge[1])))
                    writer.write("\n")

                writer.write("\n\n\n")
                writer.write("======")
                writer.write("\n")
                writer.write("Execution Time: " + str(running_time) + " s")
                writer.write("\n")
                writer.write("Memory Used: " + str(memory_used) + " MB")

        if "Problem15" in self.__solution_dir:
            with open(os.path.join(self.__solution_dir, "output" + str(file_index) + ".txt"), 'w') as writer:
                for edge in sorted(output_.items()):
                    writer.write(str(edge[0] + " -> "))

                    adj_nodes = ""
                    for string in edge[1]:
                        adj_nodes += string + ","

                    writer.write(adj_nodes[0:len(adj_nodes) - 1])
                    writer.write("\n")

                writer.write("\n\n\n")
                writer.write("======")
                writer.write("\n")
                writer.write("Execution Time: " + str(running_time) + " s")
                writer.write("\n")
                writer.write("Memory Used: " + str(memory_used) + " MB")

        if "Problem16" in self.__solution_dir:
            with open(os.path.join(self.__solution_dir, "output" + str(file_index) + ".txt"), 'w') as writer:
                for edge in sorted(output_.items()):
                    writer.write(str(edge[0] + " -> "))

                    adj_nodes = ""
                    for string in edge[1]:
                        adj_nodes += string + ","

                    writer.write(adj_nodes[0:len(adj_nodes) - 1])
                    writer.write("\n")

                writer.write("\n\n\n")
                writer.write("======")
                writer.write("\n")
                writer.write("Execution Time: " + str(running_time) + " s")
                writer.write("\n")
                writer.write("Memory Used: " + str(memory_used) + " MB")
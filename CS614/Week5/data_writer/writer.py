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

        if "Problem11" in self.__solution_dir:
            with open(os.path.join(self.__solution_dir, "output" + str(file_index) + ".txt"), 'w') as writer:
                s = output_[0]
                writer.write(str(output_[0]))
                writer.write("\n")
                writer.write(output_[1][0])
                writer.write("\n")
                writer.write(output_[1][1])
                writer.write("\n")

                writer.write("\n\n\n")
                writer.write("======")
                writer.write("\n")
                writer.write("Execution Time: " + str(running_time) + " s")
                writer.write("\n")
                writer.write("Memory Used: " + str(memory_used) + " MB")

        if "Problem12" in self.__solution_dir:
            with open(os.path.join(self.__solution_dir, "output" + str(file_index) + ".txt"), 'w') as writer:
                writer.write(str(output_[0]))
                writer.write("\n")
                writer.write(output_[1][0])
                writer.write("\n")
                writer.write(output_[1][1])
                writer.write("\n")

                writer.write("\n\n\n")
                writer.write("======")
                writer.write("\n")
                writer.write("Execution Time: " + str(running_time) + " s")
                writer.write("\n")
                writer.write("Memory Used: " + str(memory_used) + " MB")
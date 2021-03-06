___author__ = 'Ahmed Hani Ibrahim'

import os


class DataWriter(object):
    def __init__(self, solution_dir):
        self.__solution_dir = solution_dir

    def write_data(self, file_index, output_, running_time, memory_used):
        if "Problem7" in self.__solution_dir:
            with open(os.path.join(self.__solution_dir, "output" + str(file_index) + ".txt"), 'w') as writer:
                writer.write(' '.join(map(lambda v: str(v), output_)))

                writer.write("\n\n\n")
                writer.write("======")
                writer.write("\n")
                writer.write("Execution Time: " + str(running_time) + " s")
                writer.write("\n")
                writer.write("Memory Used: " + str(memory_used) + " MB")

        if "Problem8" in self.__solution_dir:
            with open(os.path.join(self.__solution_dir, "output" + str(file_index) + ".txt"), 'w') as writer:
                writer.write(' '.join(map(lambda v: str(v), output_)))

                writer.write("\n\n\n")
                writer.write("======")
                writer.write("\n")
                writer.write("Execution Time: " + str(running_time) + " s")
                writer.write("\n")
                writer.write("Memory Used: " + str(memory_used) + " MB")

        if "Problem9" in self.__solution_dir:
            with open(os.path.join(self.__solution_dir, "output" + str(file_index) + ".txt"), 'w') as writer:
                for k_mer in output_:
                    writer.write(k_mer)
                    writer.write("\n")

                writer.write("\n\n\n")
                writer.write("======")
                writer.write("\n")
                writer.write("Execution Time: " + str(running_time) + " s")
                writer.write("\n")
                writer.write("Memory Used: " + str(memory_used) + " MB")
___author__ = 'Ahmed Hani Ibrahim'
import os


class DataWriter(object):
    def __init__(self, solution_dir):
        self.__solution_dir = solution_dir
        self.__file_index = 1

    def write_data(self, input_, output_, running_time, memory_used):
        if "Problem1" in self.__solution_dir:
            with open(os.path.join(self.__solution_dir, str(self.__file_index) + ".txt"), 'w') as writer:
                writer.write(input_)
                writer.write("\n\n\n")
                writer.write("Output")
                writer.write("\n")
                writer.write(output_)

                writer.write("\n\n\n")
                writer.write("======")
                writer.write("\n")
                writer.write("Execution Time: " + str(running_time) + " s")
                writer.write("\n")
                writer.write("Memory Used: " + str(memory_used) + " MB")

        if "Problem2" in self.__solution_dir:
            with open(os.path.join(self.__solution_dir, str(self.__file_index) + ".txt"), 'w') as writer:
                writer.write(input_[0])
                writer.write("\n")
                writer.write(input_[1])
                writer.write("\n\n")
                writer.write("Output")
                writer.write("\n")
                writer.write("======")
                writer.write("\n")

                writer.write(str(len(output_)) + "\n")

                for substring in output_:
                    writer.write(substring)
                    writer.write("\n")

                writer.write("\n\n\n")
                writer.write("======")
                writer.write("\n")
                writer.write("Execution Time: " + str(running_time) + " s")
                writer.write("\n")
                writer.write("Memory Used: " + str(memory_used) + " MB")

        self.__file_index += 1


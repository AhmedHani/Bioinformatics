___author__ = 'Ahmed Hani Ibrahim'
import glob


class DataReader(object):
    def __init__(self, problem_dataset_dir):
        self.__problem_dataset_dir = problem_dataset_dir
        self.__test_cases = []
        self.__output = []

        self.__blosum = {}
        self.__pam = {}

    def get_data(self):
        files_list = glob.glob(self.__problem_dataset_dir + "\\*.txt")
        files_list.sort()

        if "Problem17" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        data = r.readlines()
                        dna = data[0].strip()
                        k = data[1].strip()
                        score_matrix = {}
                        data = data[3:]

                        for i in range(0, len(data)):
                            row = data[i].strip().split()

                            if 'A' in score_matrix:
                                current = score_matrix['A']
                                current.append(float(row[0]))
                                score_matrix['A'] = current

                            else:
                                score_matrix['A'] = [float(row[0])]

                            if 'C' in score_matrix:
                                current = score_matrix['C']
                                current.append(float(row[1]))
                                score_matrix['C'] = current

                            else:
                                score_matrix['C'] = [float(row[1])]

                            if 'G' in score_matrix:
                                current = score_matrix['G']
                                current.append(float(row[2]))
                                score_matrix['G'] = current

                            else:
                                score_matrix['G'] = [float(row[2])]

                            if 'T' in score_matrix:
                                current = score_matrix['T']
                                current.append(float(row[3]))
                                score_matrix['T'] = current

                            else:
                                score_matrix['T'] = [float(row[3])]

                        self.__test_cases.append((dna, (k, score_matrix)))

                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        k_mer = r.readline().strip()

                        self.__output.append(k_mer)

        return self.__test_cases, self.__output
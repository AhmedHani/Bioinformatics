___author__ = 'Ahmed Hani Ibrahim'
import os
import glob


class DataReader(object):
    def __init__(self, problem_dataset_dir):
        self.__problem_dataset_dir = problem_dataset_dir
        self.__rna_codons = {}
        self.__training_data = []
        self.__testing_data = []

    def get_rna_codon_table(self, rna_codon_file_name="RNA_codon_table.txt"):
        files_list = glob.glob(self.__problem_dataset_dir + "\\*.txt")

        for file_ in files_list:
            if file_.endswith("RNA_codon_table.txt"):
                with open(file_, "rb") as r:
                    for line in r:
                        codon, amino_acid = line.split(" ")
                        self.__rna_codons[codon] = amino_acid.strip()
                break

        return self.__rna_codons

    def get_data(self):
        files_list = glob.glob(self.__problem_dataset_dir + "\\*.txt")

        if "Problem1" in self.__problem_dataset_dir:
            for file_ in files_list:
                if not file_.endswith("RNA_codon_table.txt"):
                    with open(file_, "rb") as r:
                        index = 1
                        rna, output_protein = "", ""
                        prev = ""
                        for line in r:
                            if line.isspace():
                                continue
                            if index is 1:
                                rna = line
                            if "Output" in prev:
                                output_protein = line
                            prev = line
                            index += 1

                        if output_protein is "":
                            self.__testing_data.append((rna.strip(), None))
                        else:
                            self.__training_data.append((rna.strip(), output_protein.strip()))

        if "Problem2" in self.__problem_dataset_dir:
            for file_ in files_list:
                if not file_.endswith("RNA_codon_table.txt"):
                    with open(file_, "rb") as r:
                        index = 1
                        dna, amino_acid = "", ""
                        prev = ""
                        output_substrings = []

                        for line in r:
                            if line.isspace():
                                continue
                            if index is 1:
                                dna = line
                            if index is 2:
                                amino_acid = line
                            if "=" in prev or output_substrings.__len__() is not 0:
                                output_substrings.append(line.strip())
                            index += 1
                            prev = line

                        if output_substrings.__len__() is not 0:
                            self.__training_data.append(((dna.strip(), amino_acid.strip()), output_substrings))
                        else:
                            self.__testing_data.append(((dna.strip(), amino_acid.strip()), None))

        return self.__training_data, self.__testing_data
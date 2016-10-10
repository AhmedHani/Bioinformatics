___author__ = 'Ahmed Hani Ibrahim'


class RNA(object):
    def __init__(self, rna_string=""):
        self.__rna_string = rna_string
        self.__amino_acid = ""
        self.__codons_table = {}

    def set_codons_table(self, codons_table):
        self.__codons_table = codons_table

    def get_codons_table(self):
        return self.__codons_table

    def set_rna_string(self, rna_string):
        self.__rna_string = rna_string
        self.__amino_acid = ""

    def get_rna_string(self):
        return self.__rna_string

    def get_amino_acid(self):
        return self.__amino_acid

    def to_amino_acid(self):
        for i in range(0, len(self.__rna_string), 3):
            codon = self.__rna_string[i] + self.__rna_string[i + 1] + self.__rna_string[i + 2] \
                if i + 1 <= len(self.__rna_string) - 1 and i + 2 <= len(self.__rna_string) - 1 else ""
            self.__amino_acid += self.__codons_table[codon] if codon in self.__codons_table else ""

        return self.__amino_acid

    def to_dna_string(self):
        return self.__rna_to_dna_string(self.__rna_string)

    @staticmethod
    def __rna_to_dna_string(rna_string):
        return rna_string.replace('U', 'T')
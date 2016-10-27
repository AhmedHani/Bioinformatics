___author__ = 'Ahmed Hani Ibrahim'
from rna import RNA
import numpy as np


class DNA(object):
    def __init__(self, dna_string=""):
        self.__dna_string = dna_string
        self.__codon_table = {}

    def set_codon_table(self, codon_table):
        self.__codon_table = codon_table

    def get_codon_table(self):
        return self.__codon_table

    def set_dna_string(self, dna_string):
        self.__dna_string = dna_string

    def get_dna_string(self):
        return self.__dna_string

    def get_dna_to_amino_acid_candidates(self, amino_acid):
        substring_length = len(amino_acid) * 3
        rna = RNA()
        rna.set_codons_table(self.__codon_table)
        candidates = []
        for i in range(0, len(self.__dna_string)):
            if i + substring_length > len(self.__dna_string):
                break

            candidate_substring = self.__dna_string[i:(i + substring_length)]
            rna_string = self.__dna_to_rna_string(candidate_substring)
            rna.set_rna_string(rna_string)
            current_amino_acid = rna.to_amino_acid()

            if current_amino_acid == amino_acid:
                candidates.append(candidate_substring)
            else:
                reversed_dna = self.__reverse_dna(candidate_substring)
                reversed_rna = self.__dna_to_rna_string(reversed_dna)
                rna.set_rna_string(reversed_rna)
                current_amino_acid = rna.to_amino_acid()

                if current_amino_acid == amino_acid:
                    candidates.append(candidate_substring)
                    continue

                complement_dna = self.__complement_dna(candidate_substring)
                complement_rna = self.__dna_to_rna_string(complement_dna)
                rna.set_rna_string(complement_rna)
                current_amino_acid = rna.to_amino_acid()

                if current_amino_acid == amino_acid:
                    candidates.append(candidate_substring)
                    continue

                reversed_complement_dna = self.__complement_dna(self.__reverse_dna(candidate_substring))
                reversed_complement_rna = self.__dna_to_rna_string(reversed_complement_dna)
                rna.set_rna_string(reversed_complement_rna)
                current_amino_acid = rna.to_amino_acid()

                if current_amino_acid == amino_acid:
                    candidates.append(candidate_substring)
                    continue

                complement_reversed_dna = self.__reverse_dna(self.__complement_dna(candidate_substring))
                complement_reversed_rna = self.__dna_to_rna_string(complement_reversed_dna)
                rna.set_rna_string(complement_reversed_rna)
                current_amino_acid = rna.to_amino_acid()

                if current_amino_acid == amino_acid:
                    candidates.append(candidate_substring)
                    continue

        return candidates

    def to_rna_string(self):
        return self.__dna_to_rna_string(self.__dna_string)

    def reverse_dna(self):
        return self.__reverse_dna(self.__dna_string)

    def complement_dna(self):
        return self.__complement_dna(self.__dna_string)

    def reverse_complement(self):
        return self.__reverse_complement(self.__dna_string)

    def most_frequent_k_mer(self, k):
        frequent_k_mers = {}
        k_mers = []

        for i in range(0, len(self.__dna_string) - k):
            substring = self.__dna_string[i:(i + k)]

            if substring in frequent_k_mers:
                frequent_k_mers[substring] += 1
            else:
                frequent_k_mers[substring] = 1

        max_freq = max(frequent_k_mers.values())

        for item in frequent_k_mers.items():
            if item[1] == max_freq:
                k_mers.append(item[0])

        return k_mers

    def get_pattern_indices(self, pattern):
        pattern_indices = []
        pattern_length = len(pattern)

        for i in range(0, len(self.__dna_string) - pattern_length):
            substring = self.__dna_string[i:(i + pattern_length)]

            if substring == pattern:
                pattern_indices.append(i)

        return ' '.join(map(lambda v: str(v), pattern_indices))

    def get_clumps_patterns(self, k, t, l):
        clumps_patterns = []

        for i in range(0, len(self.__dna_string)):
            k_mers = {}
            for j in range(i, i + l):
                if j + k < len(self.__dna_string):
                    k_mer = self.__dna_string[j:(j + k)]

                    if k_mer in k_mers:
                        k_mers[k_mer] += 1
                    else:
                        k_mers[k_mer] = 1
                else:
                    break

            for k_mer in k_mers:
                if k_mers[k_mer] >= t:
                    clumps_patterns.append(k_mer)

        return list(set(clumps_patterns))

    def get_min_skew(self):
        indices_list = [1000]
        g_c_diff_count = 0

        for i in range(0, len(self.__dna_string)):
            if self.__dna_string[i] == 'C':
                g_c_diff_count -= 1
            if self.__dna_string[i] == 'G':
                g_c_diff_count += 1

            indices_list.append(g_c_diff_count)

        return np.array(np.where(np.array(indices_list) == np.array(indices_list).min()))[0]

    def get_mismatched_pattern_indices(self, pattern, d):
        pattern_indices = []
        pattern_length = len(pattern)
        matched = []

        for i in range(0, len(self.__dna_string) - pattern_length):
            substring = self.__dna_string[i:(i + pattern_length)]

            if substring == pattern:
                pattern_indices.append(i)
            elif self.__missmatches(substring, pattern) <= d:
                matched.append(substring)
                pattern_indices.append(i)

        return pattern_indices

    def most_frequent_missmatched_k_mer(self, k, d):
        def most_frequent_missmatched_small_k():
            missmatched_k_mers = []

            def get_all_possible_k_mer():
                import itertools

                alpha = "AGCT"
                k_mers = map(''.join, itertools.product(alpha, repeat=k))

                return k_mers

            all_k_mers = get_all_possible_k_mer()
            k_mers_freq = {}

            for k_mer in all_k_mers:
                for i in range(0, len(self.__dna_string) - k):
                    substring = self.__dna_string[i:(i + k)]

                    if substring == k_mer:
                        if k_mer not in k_mers_freq:
                            k_mers_freq[k_mer] = 1
                        else:
                            k_mers_freq[k_mer] += 1

                    elif self.__missmatches(substring, k_mer) <= d:
                        if k_mer not in k_mers_freq:
                            k_mers_freq[k_mer] = 1
                        else:
                            k_mers_freq[k_mer] += 1

            max_freq = max(k_mers_freq.values())

            for item in k_mers_freq.items():
                if item[1] == max_freq:
                    missmatched_k_mers.append(item[0])

            return missmatched_k_mers
        def most_frequent_missmatched_large_k():
            pass

        return most_frequent_missmatched_small_k() if k <= 4 else most_frequent_missmatched_small_k()

    @staticmethod
    def __reverse_dna(dna_string):
        return dna_string[::-1]

    @staticmethod
    def __complement_dna(dna_string):
        reversed_dna = ""

        for i in range(0, len(dna_string)):
            if dna_string[i] == 'A':
                reversed_dna += 'T'
            elif dna_string[i] == 'G':
                reversed_dna += 'C'
            elif dna_string[i] == 'T':
                reversed_dna += 'A'
            elif dna_string[i] == 'C':
                reversed_dna += 'G'
            elif dna_string[i] == 'G':
                reversed_dna += 'C'

        return reversed_dna

    @staticmethod
    def __reverse_complement(dna_string):
        reversed_dna = dna_string[::-1]
        reversed_complement = ""

        for i in range(0, len(reversed_dna)):
            if reversed_dna[i] == 'A':
                reversed_complement += 'T'
            elif reversed_dna[i] == 'G':
                reversed_complement += 'C'
            elif reversed_dna[i] == 'T':
                reversed_complement += 'A'
            elif reversed_dna[i] == 'C':
                reversed_complement += 'G'
            elif reversed_dna[i] == 'G':
                reversed_complement += 'C'

        return reversed_complement

    @staticmethod
    def __dna_to_rna_string(dna_string):
        return dna_string.replace('T', 'U')

    @staticmethod
    def __edit_distance(substring1, substring2):
        dp_table = [[-1 for i in range(0, len(substring1) + 1)] for j in range(0, len(substring2) + 1)]

        for j in range(0, len(substring1)):
            dp_table[0][j] = j

        for i in range(0, len(substring1)):
            dp_table[i][0] = i

        for i in range(0, len(substring1) + 1):
            for j in range(0, len(substring1) + 1):
                if substring1[i - 1] == substring2[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1]
                else:
                    dp_table[i][j] = 1 + min(dp_table[i][j - 1], min(dp_table[i - 1][j], dp_table[i - 1][j - 1]))

        return dp_table[len(substring1)][len(substring1)]

    @staticmethod
    def __missmatches(substring1, substring2):
        count = 0

        for i in range(0, len(substring1)):
            if substring1[i] != substring2[i]:
                count += 1

        return count



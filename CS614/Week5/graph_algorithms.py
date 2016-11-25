___author__ = 'Ahmed Hani Ibrahim'

from dna import DNA


class Graph(object):
    def __init__(self, nodes=None):
        self.__nodes = nodes

        self.__adj_list = {}

    def get_overlap_graph(self):
        self.__build_overlap_graph()

        return self.__adj_list

    def get_debruijn_graph(self, _type='string', k=None, dna_string=None, k_mers=None):
        if _type == 'string':
            self.__build_debruijn_graph_by_dna(k, dna_string)
        else:
            self.__build_debruijn_graph_by_k_mers(k_mers)

        return self.__adj_list

    def __build_overlap_graph(self):
        self.__nodes.sort()

        visited = set()

        for i in range(0, len(self.__nodes)):
            suffix = self.__nodes[i][1:]

            for j in range(0, len(self.__nodes)):
                if self.__nodes[j] not in visited:
                    prefix = self.__nodes[j][0:len(self.__nodes[j]) - 1]

                    if prefix == suffix:
                        visited.add(self.__nodes[j])
                        self.__adj_list[self.__nodes[i]] = self.__nodes[j]

    def __build_debruijn_graph_by_dna(self, k, dna_string):
        k_mers = sorted(DNA(dna_string).get_k_mers(k))
        suffix_k_mers = sorted(map(lambda v: v[1:], k_mers))
        prefix_k_mers = sorted(map(lambda v: v[0:len(v) - 1], k_mers))

        for i in range(0, len(prefix_k_mers)):
            prefix_suffix = prefix_k_mers[i][1:]
            k_mer_suffix = k_mers[i][1:]
            k_mer_prefix = k_mers[i][0:len(k_mers[i]) - 1]

            for j in range(0, len(suffix_k_mers)):
                suffix_prefix = suffix_k_mers[j][0:len(suffix_k_mers[j]) - 1]

                if prefix_suffix == suffix_prefix and k_mer_suffix == suffix_k_mers[j] and k_mer_prefix == prefix_k_mers[i]:
                    if prefix_k_mers[i] in self.__adj_list:
                        current = self.__adj_list[prefix_k_mers[i]]
                        current.append(suffix_k_mers[j])
                        self.__adj_list[prefix_k_mers[i]] = list(set(sorted(current)))
                    else:
                        self.__adj_list[prefix_k_mers[i]] = [suffix_k_mers[j]]

    def __build_debruijn_graph_by_k_mers(self, k_mers):
        k_mers = sorted(k_mers)
        suffix_k_mers = sorted(map(lambda v: v[1:], k_mers))
        prefix_k_mers = sorted(map(lambda v: v[0:len(v) - 1], k_mers))

        for i in range(0, len(prefix_k_mers)):
            prefix_suffix = prefix_k_mers[i][1:]
            k_mer_suffix = k_mers[i][1:]
            k_mer_prefix = k_mers[i][0:len(k_mers[i]) - 1]

            for j in range(0, len(suffix_k_mers)):
                suffix_prefix = suffix_k_mers[j][0:len(suffix_k_mers[j]) - 1]

                if prefix_suffix == suffix_prefix and k_mer_suffix == suffix_k_mers[j] and k_mer_prefix == prefix_k_mers[i]:
                    if prefix_k_mers[i] in self.__adj_list:
                        current = self.__adj_list[prefix_k_mers[i]]
                        current.append(suffix_k_mers[j])
                        self.__adj_list[prefix_k_mers[i]] = list(set(sorted(current)))
                    else:
                        self.__adj_list[prefix_k_mers[i]] = [suffix_k_mers[j]]
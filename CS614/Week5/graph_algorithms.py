___author__ = 'Ahmed Hani Ibrahim'


class Graph(object):
    def __init__(self, nodes):
        self.__nodes = nodes

        self.__adj_list = {}

    def get_overlap_graph(self):
        self.__build_overlap_graph()

        return self.__adj_list

    def __build_overlap_graph(self):
        self.__nodes.sort()

        visited = set()

        for i in range(0, len(self.__nodes)):
            prefix = self.__nodes[i][1:]

            for j in range(0, len(self.__nodes)):
                if self.__nodes[j] not in visited:
                    suffix = self.__nodes[j][0:len(self.__nodes[j]) - 1]

                    if suffix == prefix:
                        visited.add(self.__nodes[j])
                        self.__adj_list[self.__nodes[i]] = self.__nodes[j]






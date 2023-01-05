import sys


class Vertice:

    def __init__(self, edges):
        self.adjacent = [(id, value) for id, value in enumerate(edges) if value]


class DijkstraAlgorithm:

    def __init__(self, matrix, source_id):
        self.vertices = [Vertice(edge) for edge in matrix]
        self.visited_nodes = [False] * len(self.vertices)
        self.distance_set = [None] * len(self.vertices)
        self.distance_set[source_id] = 0
        self.source_id = source_id

    def run(self):
        for index, _ in enumerate(self.vertices):
            min_distance_vertice_id = self.__find_min_distance()
            self.visited_nodes[min_distance_vertice_id] = True
            for id, distance in self.vertices[min_distance_vertice_id].adjacent:
                if not self.distance_set[id] or self.distance_set[id] > distance + self.distance_set[
                    min_distance_vertice_id]:
                    self.distance_set[id] = distance + self.distance_set[min_distance_vertice_id]
        print(self.distance_set)

    def __find_min_distance(self):
        min_value = sys.maxsize
        min_value_index = None

        for index, _ in enumerate(self.vertices):

            if index == self.source_id and not self.visited_nodes[index]:
                min_value_index = index
                break

            if not self.visited_nodes[index] and self.distance_set[index] and self.distance_set[index] < min_value:
                min_value = self.distance_set[index]
                min_value_index = index

        return min_value_index


matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ]

graph = DijkstraAlgorithm(matrix, 0)

graph.run()

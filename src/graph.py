from random import choice


class Graph():
    """
        The graph itself. Contains the basic operations, as vertices and edges
        insertion, vertices and edges removal, among others.
    """
    def __init__(self):
        self.__vertices = {}

    def add_vertex(self, v):
        """
            Adds a new vertex on the graph. Initially, without any edge
            connected to it.
        """
        self.__vertices[v] = set()

    def remove_vertex(self, v):
        """
            Removes a vertex from the graph
        """
        if (v in self.__vertices):
            vertex = self.__vertices.pop(v)
            for edge in vertex:
                self.remove_edge(v, edge)
        else:
            raise NameError("Vertex doesn't exists")

    def add_edge(self, v1, v2, weight=0):
        """
            Creates an edge between vertex v1 and vertex v2. Notice that
            we can't add more than 1 edge between the same vertices.
        """
        if (v1 in self.__vertices and v2 in self.__vertices):
            self.__vertices[v1].add(v2)
            self.__vertices[v2].add(v1)
        else:
            raise NameError("At least one of the vertices doesn't exist")

    def remove_edge(self, v1, v2):
        """
            Removes an edge between vertex v1 and vertex v2
        """
        try:
            self.__vertices[v1].remove(v2)
            self.__vertices[v2].remove(v1)
        except:
            raise NameError("The edge doesn't exist")

    def order(self):
        """
            Returns the number of vertices of the graph
        """
        return len(self.__vertices)

    def vertices(self):
        """
            Returns all the vertices of the graph
        """
        return self.__vertices

    def single_vertex(self):
        """
            Returns a random vertex of the graph
        """
        return choice(list(self.__vertices.keys()))

    def adjacent_vertices(self, v):
        """
            Given a vertex v, yield all the adjacent vertices of it
        """
        try:
            return self.__vertices[v]
        except:
            raise NameError("The vertex doesn't exist")

    def degree(self, v):
        """
            Given a vertex v, returns the degree of it, i.e. the number of
            adjacent vertices of v
        """
        try:
            return len(self.__vertices[v])
        except:
            raise NameError("The vertex doesn't exist")

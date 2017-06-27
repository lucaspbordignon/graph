from random import choice


class Graph():
    """
        A directed graph (digraph). Contains the basic operations, as vertices
        and edges insertion, vertices and edges removal, among others.

        It maintains a dict (__vertices) that maps each vertex to the set of
        its adjacent vertices.
    """

    def __init__(self):
        self.__vertices = {}

    def add_vertex(self, v):
        """
            Adds a new vertex on the graph. Initially, without any edge
            connected to it.
        """
        if v not in self.__vertices:
            self.__vertices[v] = set()

    def remove_vertex(self, v):
        """
            Removes a vertex from the graph
        """
        if v in self.__vertices:
            for vertex in self.__vertices:
                self.__vertices[vertex].discard(v)
            del self.__vertices[v]
        else:
            raise RuntimeError("Vertex doesn't exists")

    def add_edge(self, v1, v2):
        """
            Creates an edge between vertex v1 and vertex v2. Notice that
            we can't add more than 1 edge between the same vertices.
        """
        if v1 in self.__vertices and v2 in self.__vertices:
            self.__vertices[v1].add(v2)
        else:
            raise RuntimeError("At least one of the vertices doesn't exist")

    def remove_edge(self, v1, v2):
        """
            Removes an edge between vertex v1 and vertex v2
        """
        try:
            self.__vertices[v1].remove(v2)
        except KeyError:
            raise RuntimeError("The edge doesn't exist")

    def order(self):
        """
            Returns the number of vertices of the graph
        """
        return len(self.__vertices)

    def vertices(self):
        """
            Returns all the vertices of the graph
        """
        return set(self.__vertices.keys())

    def single_vertex(self):
        """
            Returns a random vertex of the graph
        """
        return choice(self.__vertices.keys())

    def adjacent_vertices(self, v):
        """
            Given a vertex v, yield all the adjacent vertices of it
        """
        try:
            return self.__vertices[v]
        except KeyError:
            raise RuntimeError("The vertex doesn't exist")

    def degree(self, v):
        """
            Given a vertex v, returns the degree of it, i.e. the number of
            adjacent vertices of v
        """
        try:
            return len(self.__vertices[v])
        except KeyError:
            raise RuntimeError("The vertex doesn't exist")

    def source_vertices(self):
        """
            Returns all the source vertices of the graph, i.e. vertices that
            have an indegree of zero.
        """
        not_sources = set()
        for adjacents in self.__vertices.values():
            # add to 'not_sources' all vertices that have incoming edges
            not_sources.update(adjacents)
        return self.vertices() - not_sources

    def topological_order(self):
        """
            Returns a topological order of the graph.
        """
        try:
            order = []
            visited = set()
            for v in self.source_vertices():
                self.__visit(v, order, visited)
            # return a reverse of 'order'
            return order[::-1]
        except RecursionError:
            raise RuntimeError("Graph is not a DAG")

    def depth_first_search(self, vertex, visited=[]):
        """
            Executes a depth-first search on a single connected component of 
            the graph. Returns a list with the vertices in order of visit.
        """
        for adj in list(self.__vertices[vertex]):
            if adj not in visited:
                visited.append(adj)
                visited = self.depth_first_search(adj, visited)
        return visited

    def __visit(self, v, order, visited):
        """
            Visits a vertex while topologically ordering the graph. After
            visiting all of the unvisited successors of 'v', adds 'v' to the
            end of 'order'. After visiting all vertices, 'order' should hold an
            inverse of a topological order.
        """
        for adj in self.__vertices[v]:
            if adj not in visited:
                self.__visit(adj, order, visited)
        visited.add(v)
        order.append(v)

from graph import Graph


class Course():
    """
        The course object, it contains its name, how many classes/week,
        semester and the courses that are prerequisites for taking it.
    """

    def __init__(self, name, hours, semester, prereqs):
        self.name = name
        self.hours = hours
        self.semester = semester
        self.prereqs = prereqs

    def __lt__(self, other):
        if self.semester == other.semester:
            return self.name < other.name
        return self.semester < other.semester


class Curriculum():
    """
       The representation of the computer science curriculum. An internal
       graph is created, with the following definition:

       G(V, A) such that:
            V = {C | C is a computer science course}
            A = {(C1, C2) | C1 is a prerequisite of C2}
    """
    def __init__(self):
        self.__curriculum = Graph()
        self.__courses = {
            # 1st semester
            "eel5105": Course("eel5105", 5, 1, []),
            "ine5401": Course("ine5401", 2, 1, []),
            "ine5402": Course("ine5402", 6, 1, []),
            "ine5403": Course("ine5403", 6, 1, []),
            "mtm3101": Course("mtm3101", 4, 1, []),
            # 2nd semester
            "ine5404": Course("ine5404", 6, 2, ["ine5402"]),
            "ine5405": Course("ine5405", 5, 2, ["mtm3101"]),
            "ine5406": Course("ine5406", 5, 2, ["eel5105"]),
            "ine5407": Course("ine5407", 3, 2, []),
            "mtm5512": Course("mtm5512", 4, 2, []),
            "mtm7174": Course("mtm7174", 4, 2, ["mtm3101"]),
            # 3rd semester
            "ine5408": Course("ine5408", 6, 3, ["ine5404"]),
            "ine5409": Course("ine5409", 4, 3, ["mtm5512", "mtm7174"]),
            "ine5410": Course("ine5410", 4, 3, ["ine5404"]),
            "ine5411": Course("ine5411", 6, 3, ["ine5406"]),
            "mtm5245": Course("mtm5245", 4, 3, ["mtm5512"]),
            # 4th semester
            "ine5412": Course("ine5412", 4, 4, ["ine5410", "ine5411"]),
            "ine5413": Course("ine5413", 4, 4, ["ine5403", "ine5408"]),
            "ine5414": Course("ine5414", 4, 4, ["ine5404"]),
            "ine5415": Course("ine5415", 4, 4, ["ine5403", "ine5408"]),
            "ine5416": Course("ine5416", 5, 4, ["ine5408"]),
            "ine5417": Course("ine5417", 5, 4, ["ine5408"]),
            # 5th semester
            "ine5418": Course("ine5418", 4, 5, ["ine5412", "ine5414"]),
            "ine5419": Course("ine5419", 4, 5, ["ine5417"]),
            "ine5420": Course("ine5420", 4, 5, ["ine5408", "mtm5245", "mtm7174"]),
            "ine5421": Course("ine5421", 4, 5, ["ine5415"]),
            "ine5422": Course("ine5422", 4, 5, ["ine5414"]),
            "ine5423": Course("ine5423", 4, 5, ["ine5408"]),
            # 6th semester
            "ine5424": Course("ine5424", 4, 6, ["ine5412"]),
            "ine5425": Course("ine5425", 4, 6, ["ine5405"]),
            "ine5426": Course("ine5426", 4, 6, ["ine5421"]),
            "ine5427": Course("ine5427", 4, 6, ["ine5421"]),
            "ine5430": Course("ine5430", 4, 6, ["ine5405", "ine5413", "ine5416"]),
            "ine5453": Course("ine5453", 1, 6, ["ine5417"]),
            # 7th semester
            "ine5428": Course("ine5428", 4, 7, ["ine5407"]),
            "ine5429": Course("ine5429", 4, 7, ["ine5403", "ine5414"]),
            "ine5431": Course("ine5431", 4, 7, ["ine5414"]),
            "ine5432": Course("ine5432", 4, 7, ["ine5423"]),
            "ine5433": Course("ine5433", 6, 7, ["ine5427", "ine5453"]),
            # 8th semester
            "ine5434": Course("ine5434", 9, 8, ["ine5433"])
        }
        self.initialize_curriculum()

    @property
    def courses(self):
        return self.__courses

    @property
    def graph(self):
        return self.__curriculum

    def add_course(self, graph, course):
        """
            Adds a Course to a given Graph, creating the edges from the course
            prerequisites to the course itself.
        """
        graph.add_vertex(course.name)
        for prereq in course.prereqs:
            graph.add_vertex(prereq)
            graph.add_edge(prereq, course.name)

    def initialize_curriculum(self):
        """
            Adds all the subjects of the curriculum to the graph.
        """
        for course in self.__courses.values():
            self.add_course(self.__curriculum, course)

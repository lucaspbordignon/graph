from curriculum import Curriculum


class Main():
    def __init__(self):
        curriculum_object = Curriculum()
        self.curriculum = curriculum_object.graph
        self.courses = curriculum_object.courses
        self.show()

    def show(self):
        """
            Shows the menus and interacts with the user.
        """
        print("Ordem topológica do currículo de Ciência da Computação:\n")
        print(self.curriculum.topological_order())

        print("----------------------------------------------------------------------")

        semester = int(input("Em qual semestre você está? "))

        print("\nDigite o código das disciplinas que você já foi aprovado:")
        print("(Deixe vazio para finalizar a inserção de disciplinas)")
        course = input("")
        completed = []
        while course != "":
            completed.append(course)
            course = input("")

        for course in completed:
            self.curriculum.remove_vertex(course)

        print("----------------------------------------------------------------------")
        print("Sugestão de matérias para o(s) próximo(s) semestre(s):\n")
        while self.curriculum.order() > 0:
            # order possible courses (source vertices) by semester
            possible_courses = sorted(self.curriculum.source_vertices(),
                                      key=lambda c: self.courses[c])

            total_hours = 0
            recommended_courses = []

            for course in possible_courses:
                if total_hours + self.courses[course].hours <= 28:
                    recommended_courses.append(course)
                    total_hours += self.courses[course].hours

            semester += 1
            print("Faça no {}o semestre:".format(semester))
            for course in recommended_courses:
                print("{} ".format(course), end='')
            print("\n")

            for course in recommended_courses:
                self.curriculum.remove_vertex(course)


if (__name__ == '__main__'):
    Main()

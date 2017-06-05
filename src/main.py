from curriculum import Curriculum


if __name__ == "__main__":

    curriculum = Curriculum()

    print("Ordem topológica do currículo de Ciência da Computação:\n")
    print(curriculum.graph.topological_order())

    print("-"*80)

    semester = int(input("Quantos semestres completos você já cursou? "))

    print("\nDigite o código das disciplinas que você já foi aprovado " +
          "(e.g. ine5413):")
    print("(Deixe vazio para finalizar a inserção de disciplinas)")

    course = input("")
    completed = []
    while course != "":
        completed.append(course)
        course = input("")

    for course in completed:
        curriculum.graph.remove_vertex(course)

    print("-"*80)
    print("Sugestão de matérias para o(s) próximo(s) semestre(s):\n")

    while curriculum.graph.order() > 0:
        # order possible courses (source vertices) by semester
        possible_courses = sorted(curriculum.graph.source_vertices(),
                                  key=lambda c: curriculum.courses[c])

        total_hours = 0
        recommended_courses = []

        for course in possible_courses:
            if total_hours + curriculum.courses[course].hours <= 28:
                recommended_courses.append(course)
                total_hours += curriculum.courses[course].hours

        semester += 1
        print("Faça no {}o semestre:".format(semester))
        for course in recommended_courses:
            print("{} ".format(course), end='')
        print("\n")

        for course in recommended_courses:
            curriculum.graph.remove_vertex(course)

from curriculum import curriculum, courses

semester = int(input("Em qual semestre você está? "))
print("")

print("Digite o código das disciplinas que você já foi aprovado:")
course = input("")
completed = []
while course != "":
    completed.append(course)
    course = input("")

for course in completed:
    curriculum.remove_vertex(course)

while curriculum.order() > 0:
    # order possible courses (source vertices) by semester
    possible_courses = sorted(curriculum.source_vertices(),
            key=lambda c: courses[c])

    total_hours = 0
    recommended_courses = []

    for course in possible_courses:
        if total_hours + courses[course].hours <= 28:
            recommended_courses.append(course)
            total_hours += courses[course].hours

    semester += 1
    print("Faça no {}o semestre:".format(semester))
    for course in recommended_courses:
        print("{} ".format(course), end='')
    print("\n")

    for course in recommended_courses:
        curriculum.remove_vertex(course)

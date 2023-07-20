# 1st solution
def divide_students(students):
        even_list = []
        odd_list = []
        all = []
        for i, student in enumerate(students):
            if i % 2 == 0:
                even_list.append(student)
            else:
                odd_list.append(student)

        all.append(even_list)
        all.append(odd_list)
        return all

# 2nd solution
def divide_students2(students):
    groups = [[], []]
    for i, student in enumerate(students):
        if i % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    return groups


students = ["John", "Mark", "Venessa", "Mariam"]
print(divide_students(students))
print(divide_students2(students))

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_of_students = sorted(list(students))
median_grades_dict = {}
number_of_students = (len(grades))
for i in range(0, number_of_students):
    sum_of_grades = sum(grades[i])
    count_of_grades = len(grades[i])
    median_grade = (sum_of_grades / count_of_grades)
    median_grades_dict.update({list_of_students[i]: median_grade})
print(median_grades_dict)
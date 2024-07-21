grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sum_of_grades_0 = sum(grades[0])
count_of_grades_0 = len(grades[0])
median_grade_0 = (sum_of_grades_0 / count_of_grades_0)  # Aaron
sum_of_grades_1 = sum(grades[1])
count_of_grades_1 = len(grades[1])
median_grade_1 = (sum_of_grades_1 / count_of_grades_1)  # Bilbo
sum_of_grades_2 = sum(grades[2])
count_of_grades_2 = len(grades[2])
median_grade_2 = (sum_of_grades_2 / count_of_grades_2)  # Johnny
sum_of_grades_3 = sum(grades[3])
count_of_grades_3 = len(grades[3])
median_grade_3 = (sum_of_grades_3 / count_of_grades_3)  # Khendrik
sum_of_grades_4 = sum(grades[4])
count_of_grades_4 = len(grades[4])
median_grade_4 = (sum_of_grades_4 / count_of_grades_4)  # Steve

list_of_students = list(students)
list_of_students = sorted(list_of_students)
median_grades_dict = {list_of_students[0]:median_grade_0,
                      list_of_students[1]:median_grade_1,
                      list_of_students[2]:median_grade_2,
                      list_of_students[3]:median_grade_3,
                      list_of_students[4]:median_grade_4}
print(median_grades_dict)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3],
          [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(students) # сортируем по порядку список студентов
average_grades = {} # создаём словарь
for student, student_grades in zip(students_list, grades): #создаём переменные student=students_list и др, объединяем списки
    average_grade = sum(student_grades) / len(student_grades) # находим средние через заданную переменную
    average_grades[student] = average_grade #ключ student, средний балл - значение
print(average_grades)
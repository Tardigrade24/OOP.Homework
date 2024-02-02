class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade_for_student(self):
        total_grades = 0
        total_count = 0
        for grades_list in self.grades.values():
            total_grades += sum(grades_list)
            total_count += len(grades_list)

        if total_count == 0:
            return 0
        else:
            return total_grades / total_count

    def __lt__(self, other):
        return self._average_grade_for_student() < other._average_grade_for_student()

    def __le__(self, other):
        return self._average_grade_for_student() <= other._average_grade_for_student()

    def __eq__(self, other):
        return self._average_grade_for_student() == other._average_grade_for_student()

    def __ne__(self, other):
        return self._average_grade_for_student() != other._average_grade_for_student()

    def __gt__(self, other):
        return self._average_grade_for_student() > other._average_grade_for_student()

    def __ge__(self, other):
        return self._average_grade_for_student() >= other._average_grade_for_student()

    def __str__(self):
        finished_courses_str = ", ".join(self.finished_courses)
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        avg_grade = self._average_grade_for_student()
        return (f"Имя: {self.name}"
                f"\nФамилия: {self.surname}"
                f"\nСредняя оценка за домашние задания:{avg_grade}"
                f"\nКурсы в процессе изучения: {courses_in_progress_str}"
                f"\nЗавершенные крусы:{finished_courses_str}")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        total_grades = 0
        total_count = 0
        for grades_list in self.grades.values():
            total_grades += sum(grades_list)
            total_count += len(grades_list)

        if total_count == 0:
            return 0
        else:
            return total_grades / total_count

    def __lt__(self, other):
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        return self._average_grade() <= other._average_grade()

    def __eq__(self, other):
        return self._average_grade() == other._average_grade()

    def __ne__(self, other):
        return self._average_grade() != other._average_grade()

    def __gt__(self, other):
        return self._average_grade() > other._average_grade()

    def __ge__(self, other):
        return self._average_grade() >= other._average_grade()

    def __str__(self, ):
        avg_grade = self._average_grade()
        return super().__str__() + f"\nСредняя оценка за лекции:{avg_grade}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def _rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__()

def average_grade_for_homework(students, course_name):
    total_grades = 0
    total_count = 0

    for student in students:
        if course_name in student.grades:
            total_grades += sum(student.grades[course_name])
            total_count += len(student.grades[course_name])

    if total_count == 0:
        return 0
    else:
        return total_grades / total_count

def average_grade_for_lectures(lecturers, course_name):
    total_grades = 0
    total_count = 0

    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grades += sum(lecturer.grades[course_name])
            total_count += len(lecturer.grades[course_name])

    if total_count == 0:
        return 0
    else:
        return total_grades / total_count


student1 = Student("John ", "Smith ", "Male ")
student2 = Student("Jane ", "Smith ", "Female ")

lecturer1 = Lecturer("James", "Bond")
lecturer2 = Lecturer("Jason", "Bourne")

reviewer1 = Reviewer("John", "Wick")
reviewer2 = Reviewer("Johnny", "Silverhand")

# Добавляем курсы
student1.courses_in_progress = ["математика", "физика "]
student1.finished_courses = ["история"]

student2.courses_in_progress = ["химия", "биология "]
student2.finished_courses = ["литература"]

lecturer1.courses_attached = ["математика", "физика"]
lecturer2.courses_attached = ["химия", "биология"]

reviewer1.courses_attached = ["математика", "физика"]
reviewer2.courses_attached = ["химия", "биология"]

# Проверка дз
reviewer1._rate_hw(student1, "математика", 90)
reviewer1._rate_hw(student1, "физика", 85)
reviewer2._rate_hw(student2, "химия", 92)
reviewer2._rate_hw(student2, "биология", 88)

# Оценки лекторов
student1._rate_lecturer(lecturer1, "математика", 5)
student1._rate_lecturer(lecturer1, "физика", 4)
student2._rate_lecturer(lecturer2, "химия", 4)
student2._rate_lecturer(lecturer2, "биология", 5)

# Пример использования функций
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]
course_name = "математика"
average_hw_grade = average_grade_for_homework(students_list, course_name)
average_lecture_grade = average_grade_for_lectures(lecturers_list, course_name)

print("Student 1:")
print(student1)

print("\nStudent 2:")
print(student2)

print("\nLecturer 1:")
print(lecturer1)

print("\nLecturer 2:")
print(lecturer2)

print("\nReviewer 1:")
print(reviewer1)

print("\nReviewer 2:")
print(reviewer2)

print(f"Средняя оценка за домашние задания по курсу {course_name}: {average_hw_grade}")
print(f"Средняя оценка за лекции по курсу {course_name}: {average_lecture_grade}")
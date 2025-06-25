class Student:
    student_year = 2027 # its a class variable
    num_students = 0  # class variable

    def __init__(self, name, age,):
        self.name = name
        self.age = age
        Student.num_students += 1
        #you can't put Student.student_year here
#print(Student.student_year) you can only print
student1 = Student("Aditya", 20)
student2 = Student("Adhi", 19)
student3 = Student("john", 21)
print(f"The number of students in the calss is {Student.num_students} and they will gradute on the year {Student.student_year}")
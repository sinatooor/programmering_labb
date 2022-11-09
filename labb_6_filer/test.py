class School:
    def __init__(self, student):
        pass

class Student:
    # student is a object with 3 parameters
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.id_number}"




def main():
    """Main function of program"""

    id_number = 2
    file = open("students.txt", "r")
    students = []
    amount_of_students = 0
    while id_number != "":
        id_number = file.readline().strip()
        last_name = file.readline().strip()
        first_name = file.readline().strip()
        student = Student(first_name,last_name, id_number)
        students.append(student)
        amount_of_students +=1
    file.close()   


    n = 0
    while n != amount_of_students:
        print(f"{students[n]}")
        n+=1


main()

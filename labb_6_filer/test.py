class School:
    def __init__(self, student):
        pass

class Student:
    # student is a object with 3 parameters
    def __init__(self, id_number, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.id_number}"




def main():
    """Main function of program"""

    file = open("students.txt", "r")
    students = []
    amount_of_students = 0
    while True:
        student = Student(file.readline().strip(),file.readline().strip(),file.readline().strip())
        students.append(student)
        amount_of_students +=1
        if file.readline() == "":
            break

    file.close()   


    n = 0
    while n != amount_of_students:
        print(f"{students[n]}")
        n+=1


main()

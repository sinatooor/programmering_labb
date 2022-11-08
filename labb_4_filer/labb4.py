class Student:
    # student is a object with 3 parameters
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        return str(self.first_name + self.last_name + self.id_number)


def add_student():
    """Adds new student object"""


def edit_student():
    """Edits an existing student object"""


def delete_student():
    """Deletes a student object"""


def main():
    """Main function of program"""
    name_of_file = input("What is the full name of the file? ")
    file = open(name_of_file, "r")

    number_of_student = input(
        "How many student objects do you want to create? ")

    n = 0
    student = [number_of_student]
    while number_of_student != 0:
        full_name = input("Write full name with space: ").title().strip()
        first_name, last_name = full_name.split(" ")
        student[n] = Student(first_name, last_name, input("Id number: "))
        number_of_student = number_of_student-1

    specified = 0
    while number_of_student < specified:
        print(
            f"{student[specified].first_name} {student[specified].last_name}, with id {student[specified].id_number}")
        specified = specified+1


main()

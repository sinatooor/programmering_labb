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
    full_name = input("Name: ").title().strip()
    first_name, last_name = full_name.split(" ")
    id_number = input("Id number: ")

    print(student)


main()

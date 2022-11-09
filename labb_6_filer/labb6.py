class School:
    

class Student:
    # student is a object with 3 parameters
    def __init__(self, first_name, last_name, id_number):

        if not id_number or not first_name or not last_name:
            raise ValueError("Missing value")
        if len(id_number)!=10:
            raise ValueError("Incorrect ID number")
        if isinstance(id_number, int) != True:
            raise ValueError("Incorrect ID number, It should be digits")
        if last_name == first_name:
            raise ValueError("First name and last name can not be the same")


        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        return str(self.first_name + self.last_name + self.id_number)



def searching_file(name_of_file):
    while true:
        try:
            with open(str(name_of_file), r) in file:
        except FileNotFoundError:
            print("This file does not exist try! try agian")
        return file


def main():
    """Main function of program"""
    name_of_file = input("What is the full name of the file? ")

    file = open(name_of_file, "r")

    answer = "a"
    while answer != "x":
        print("Add student = a, Edit student = e, Delete student = d, End program = x")
        answer = input("What would you like to do? ")
        full_name = input("Name: ").title().strip()
        first_name, last_name = full_name.split(" ")
        student1 = Student(first_name,last_name, input("Id number: "))


    print(f"{student1.first_name} {student1.last_name}, with id {student1.id_number}")


main()

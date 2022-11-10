# -*- coding: utf-8 -*-
import typed_input
import colorama


class School:

    students = []

    @classmethod
    def print_students(cls):
        """prints all students, full name and id, in school"""

        for i in School.students:
            print(i)
        print("")

    @classmethod
    def add_student(cls):
        """adds a student to school list"""
        try:
            full_name = (
                input("Write first name and last name with space: ").title().strip()
            )
        except ValueError:
            print("Type only first and last name! ")
        first_name, last_name = full_name.split()
        id_number = typed_input.check_int("What is the id number? ")
        School.students.append(Student(first_name, last_name, int(id_number)))

    @classmethod
    def read_student_list(cls, file):
        """reads all students and add it to the students container
        argument: file name
        Retuns: nothing
        """

        while True:
            id_number = file.readline().strip()
            last_name = str(file.readline().strip())
            first_name = str(file.readline().strip())
            if id_number == "":
                break

            new = Student(first_name, last_name, int(id_number))
            School.students.append(new)
        file.close()

    @classmethod
    def search_students(cls):
        first_name = input("What is the first name of the person? ")
        n = 0
        while n <= len(School.students):
            if School.students[n].first_name == first_name:
                print(School.students[n])
                break
            n += 1


class Student:
    # student is a object with 3 parameters
    def __init__(self, first_name, last_name, id_number):

        if not id_number or not first_name or not last_name:
            raise ValueError("Missing value")
        if len(str(id_number)) != 10:
            raise ValueError("Incorrect ID number")
        if isinstance(id_number, int) != True:
            raise ValueError("Incorrect ID number, It should be digits")

        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        M = colorama.Fore.MAGENTA
        W = colorama.Fore.WHITE
        return f"{M}Name: {W}{self.first_name} {self.last_name} {M}ID number: {W}{self.id_number}"


def check_file_name():
    """checks if given filename exists"""
    while True:
        try:
            file_name = input(
                f"{colorama.Fore.BLUE}What is the name of file? {colorama.Fore.WHITE}"
            )
            file = open(file_name, encoding="utf-8")
        except FileNotFoundError:
            print(
                f"{colorama.Fore.RED}This file does not exist try! try again{colorama.Fore.WHITE}"
            )

        else:
            break

    return file


def main():
    """Main function of program"""
    print(School)
    while True:
        user_answer = menu_choice()
        if user_answer == "a":
            School.add_student()
        elif user_answer == "d":
            School.print_students()
        elif user_answer == "r":
            School.read_student_list(check_file_name())
            School.print_students()
        elif user_answer == "s":
            School.search_students()
        elif user_answer == "x":

            break


def menu_choice():
    """Menu which get users input
    Argument : nothing
    Returns: user's choice
    """

    print(f"{colorama.Fore.GREEN}Press A to add new a student")
    print("Press D to display all students")
    print("Press R to read in a file")
    print("Press S to search for a student")
    print("Press X to exit the program")
    choice = input(
        f"{colorama.Fore.BLUE}What do you want to do? {colorama.Fore.WHITE}"
    ).lower()
    print("")
    return choice


main()

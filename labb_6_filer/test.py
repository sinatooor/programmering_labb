# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-
# -*- coding: latin-1 -*-
import typed_input
import colorama

class School:
    
    students = []

    def add_student(self=None):
        full_name = input("Write full name with space: ").title().strip()
        first_name, last_name = full_name.split(None)
        id_number = typed_input.check_int("What is the id number? ")
        School.students.append(Student(first_name, last_name, int(id_number)))

    def read_student_list(self,file_name):
        """ reads all students and add it to the students container
        argument: file name
        Retuns: nothing
        """
        file = open(str(file_name), "r")

        while True:
            id_number = file.readline().strip()
            last_name = str(file.readline().strip())
            first_name = str(file.readline().strip())
            if id_number == "":
                break

            new = Student(first_name, last_name , int(id_number))
            School.students.append(new)
        file.close()
        
    def print_students(self=None):
        """prints all students, full name and id, in school"""
        number_of_students = len(School.students)-1
        while number_of_students >= 0:
            print(School.students[number_of_students])
            number_of_students-=1
            
        


            
        


class Student:
    # student is a object with 3 parameters
    def __init__(self, first_name, last_name, id_number):
        
        if not id_number or not first_name or not last_name:
            raise ValueError("Missing value")
        if len(str(id_number))!=10:
            raise ValueError("Incorrect ID number")
        if isinstance(id_number, int) != True:
            raise ValueError("Incorrect ID number, It should be digits")
        

        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.id_number}"

def main():

    School.read_student_list(1,"students.txt")
    School.print_students()
    School.add_student()
    School.print_students()


main()
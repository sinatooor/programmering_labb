class School:
    # School is an object meant to store Student objects
    def __init__(self, student):
        print("hello")
    # Search method to find student based on id_number
    def search_for_student(self, id_number):
        searched_id_number = input("What is the id number of the student? ")

class Student:
    # Student is a object with 3 parameters
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} ID: {self.id_number}"


    @classmethod
    def get(cls):
        first_name = input("What is the students fist name? ")
        last_name = input("What is the students last name? ")
        id_number = input("What is the students id number? ")
        return cls(first_name , last_name , id_number)      #will instantiate a object in this classs (the same as Student())




def main():
    a_student = Student(first_name, last_name, id_number)

    print(a_student)




main()

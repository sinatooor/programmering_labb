import typed_input
import colorama

class Student:
    # student is a object with 3 parameters
    def __init__(self, first_name, last_name, id_number):

        if not id_number or not first_name or not last_name: #checks so there is a value
            raise ValueError("Missing value")
        if len(str(id_number)) != 10: #id number needs to be 10 digits
            raise ValueError("Incorrect ID number")
        if isinstance(id_number, int) != True: #checks so id number is an int
            raise ValueError("Incorrect ID number, It should be digits")

        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        M = colorama.Fore.MAGENTA
        W = colorama.Fore.WHITE
        return f"{M}Name: {W}{self.first_name} {self.last_name} {M}ID number: {W}{self.id_number}"
    

def create_student():
    """function that creates a object of type student and returns said object"""
    while True:
        try:
            full_name = (
                input("Write first name and last name with space: ").title().strip()
            )
            first_name, last_name = full_name.split() #splits with empty space
        except ValueError:
            print(f"{colorama.Fore.RED}Type only first and last name! {colorama.Fore.WHITE}")
        else:
            break
    while True:
        try:   
            id_number = typed_input.check_int("What is the id number? ")
            student = Student(first_name, last_name, int(id_number))
        except ValueError:
            print(f"{colorama.Fore.RED}Invalid id number! {colorama.Fore.WHITE}")
        else:
            break
    return student


def main():
    """promts user to create 3 objects of type students and then prints them"""


    object1 = create_student()
    object2 = create_student()
    object3 = create_student() 

    print("Here are all the created students:")
    print(object1)
    print(object2)
    print(object3)


main()
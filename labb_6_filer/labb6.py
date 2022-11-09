class School:
    
    students = []




        def read_students(self):
        """ reads all students and add it to the students container
        argument: self
        Retuns: nothing
        """
        fil = open("students.txt", "r")
        first_name = fil.readline().strip()
        while first_name:
            first_name = int(fil.readline().strip())
            last_name = int(fil.readline().strip())
            id_number = float(fil.readline().strip())
            new = Student(first_name, last_name , id_number)
            students.append(new)
            first_name = fil.readline().strip()
        fil.close()





class Student:
    # student is a object with 3 parameters
    def __init__(self, first_name, last_name, id_number):
        
        if not id_number or not first_name or not last_name:
            raise ValueError("Missing value")
        if len(id_number)!=10:
            raise ValueError("Incorrect ID number")
        if isinstance(id_number, int) != True:
            raise ValueError("Incorrect ID number, It should be digits")
        

        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def __str__(self):
        return str(self.first_name + self.last_name + self.id_number)



def searching_file(name_of_file):
    while true:
        try:
            with open(str(name_of_file), r) in file:
                pass
        except FileNotFoundError:
            print("This file does not exist try! try agian")
        return file


def main():
    """Main function of program"""

    id_number = 2
    file = open("students.txt", "r")
    students = []
    
    amount_of_students = 0
    while id_number != "":
        id_number = 
        last_name = file.readline()
        first_name = file.readline()
        student = Student(first_name,last_name, id_number)
        students.append(student)
        amount_of_students +=1
    file.close()   


    n = 0
    while n != amount_of_students:
        print(f"{students[n].first_name} {students[n].last_name}, with id {students[n].id_number}")
        n+=1


main()


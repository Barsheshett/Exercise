from Student import Student
from Employee import Employee
from WorkingStudent import WorkingStudent
from Person import Person

def arrayBuilder():
    arr = []
    i = int(input("enter how many people do you want to enter"))
    for index in range(i):
        chose = int(input("enter 1 for person 2 for student 3 for employee and 4 for working student"))
        if chose == 1:
            arr.append(Person(input("enter name"), input("enter id"), int(input("enter age"))))
        elif chose == 2:
            arr.append(Student(input("enter name"), input("enter id"), int(input("enter age")), float(input("enter average")), input("enter institute")))
        elif chose == 3:
            arr.append(Employee(input("enter name"), input("enter id"), int(input("enter age")), float(input("enter salary"))))
        else:
            arr.append(WorkingStudent(input("enter name"), input("enter id"), int(input("enter age")), float(input("enter average")), input("enter institute"), bool(input("enter same_institute"))))
    return arr

def typeArr(arr):
    for i in arr:
        print(type(i))


def main():
    arr = arrayBuilder()
    for i in arr:
        print(i, end="\n\n")
    typeArr(arr)



if __name__ == "__main__":
    main()
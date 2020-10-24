from Student import Student
from Employee import Employee

class WorkingStudent(Student, Employee):
    def __init__(self, name="Ivgenia", id="123456789", age=30, average=100, institute="Queen", salary=100000, same_institute=True):
        Student.__init__(self, name, id, age, average, institute)
        Employee.init(self, salary)
        self.same_institute = same_institute

    def __str__(self):
        print(Student.__str__(self))
        print(Employee.Print(self))
        return "same_institute: %s" % (self.same_institute)
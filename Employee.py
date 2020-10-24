from Person import Person

class Employee(Person):

    def __init__(self, name="Ivgenia", id="123456789", age=30, salary=100000.0):
        Person.__init__(self, name, id, age)
        self.salary = salary

    def init(self, salary=100000):
        self.salary = salary

    def __str__(self):
        print(Person.__str__(self))
        return"salary:%.2f" % self.salary

    def Print (self):
        return "salary: %.2f" % (self.salary)

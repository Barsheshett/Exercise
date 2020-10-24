from Person import Person

class Student (Person):
    def __init__(self, name="Ivgenia", id="123456789", age=30, average=100, institute="Queen"):
        Person.__init__(self, name, id, age)
        self.average = average
        self.institute = institute

    def __str__(self):
        print(Person.__str__(self))
        return "average: %d\ninstitute:%s" % (self.average, self.institute)
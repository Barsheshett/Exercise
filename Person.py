class Person:
    def __init__(self, name="Ivgenia", id="123456789", age=30):
        self.name = name
        self.id = id
        self.age = age

    def __str__(self):
        return "name: %s\nid: %s\nage: %d" % (self.name, self.id, self.age)
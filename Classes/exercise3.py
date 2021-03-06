# Explain the differences between the attributes name, surname and profession, and what values they can have in different instances of this class:

class Smith:
    surname = "Smith"
    profession = "smith"

    def __init__(self, name, profession=None):
        self.name = name
        if profession is not None:
            self.profession = profession


#name here is a variable used to initialise the self.name instance level attribute of the class. It's value will be whatever is given when the instance is created.
#surname here is a class attribute and is the same value for all instances of the class at all times.
#profesion here is an instance level attribut and if given, the value will be set to whatever is specified when the object is created. If not specified though, it will use the class instance attribute which in this case will be "smith"

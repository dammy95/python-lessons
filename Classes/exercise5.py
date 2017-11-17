import datetime

from exercise2 import Person

"""
1. What happens if you call the __str__ method on the instance? 

person.__str__() gives '<exercise2.Person object at 0x1011f45c0>' 
which indeed is the same as using str(person)

2. What is the type of the instance?

using the type() function. type(person) gives <class 'exercise2.Person'>

3. What is the type of the class?

usign the type function again on Person, i.e type(Person), this gives <class 'type'>

4. Write a function which prints out the names and values of all the 
   custom attributes of any object that is passed in as a parameter.

see function below

"""

def print_custom_attributes(any_object):
    for att, val in any_object.__dict__.items():
        print("%s: %s" % (att, val))


if __name__ == '__main__':
    person = Person(
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12), # year, month, day
        "No. 12 Short Street, Greenville",
        "555 456 0987",
        "jane.doe@example.com"
    )

    print_custom_attributes(person)

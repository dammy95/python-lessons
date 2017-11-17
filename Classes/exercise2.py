import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

        self._today = datetime.date.today()
        self._age = self.age()
        

    def age(self):
        today = datetime.date.today()
        if today > self._today:
            return self._age

        self._today = today
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        self._age = age
        return age

if __name__ == '__main__':

    person = Person(
        "Jane",
        "Doe",
        datetime.date(1992, 3, 12), # year, month, day
        "No. 12 Short Street, Greenville",
        "555 456 0987",
        "jane.doe@example.com"
    )

    print(person.name)
    print(person.email)
    print(person.age())

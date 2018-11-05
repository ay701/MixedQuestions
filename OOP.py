class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.mouth = "closed"

    def open_mouth(self):
        if self.mouth == "closed":
            self.mouth = "opened"
            print("Mouth opened")

    def close_mouth(self):
        if self.mouth == "opened":
            self.mouth = "closed"
            print("Mouth closed")

    def request_open_mouth(self):
        print("Request to open mouth")

        if Person.confirm_identity(self):
            self.patient.open_mouth()
        else:
            print("Patent rejected to open mouth")
            exit()

    @staticmethod
    def confirm_identity(person):
        return hasattr(person, "patient")


class Doctor(Person):

    def __init__(self, first, last):
        Person.__init__(self, first, last)
        self.patient = None

    def add(self, person):
        self.patient = person
        print("Patent: " + self.patient.first + " " + self.patient.last + " added")

    def examine_mouth(self):
        if self.patient.mouth == "opened":
            print("Examining mouth ...")
            self.patient.close_mouth()
            self.examine_done()
        else:
            print("Mouth is closed, can't examine")
            exit()

    @staticmethod
    def examine_done():
        print("Examine done.")


person = Person("David", "Beckham")
doctor = Doctor("Michael", "Berryln")
doctor.add(person)
doctor.request_open_mouth()
doctor.examine_mouth()

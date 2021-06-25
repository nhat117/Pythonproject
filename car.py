class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.000

    def description(self):
        return "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)

car1 = Vehicle()
car1.name = "Merc"
car1.color = "Red"
car1.value = 100000
car2 = Vehicle()
car2.name = "BMW"
car2.color = "Beige"
car2.value = 200000
print(car1.description())
print(car2.description())
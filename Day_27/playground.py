
def add(*num):
    total = 0
    for n in num:
        total += n
    return total

print(add(2, 3, 7))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=5, multiply=7)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Dodge", model="Viper", color="Red W/ White Stripes")
print(my_car.model)
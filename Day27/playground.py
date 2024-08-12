def add(*args):
    total = 0
    for n in args:
        total += n
    return total


#print(add(5, 3, 4, 5, 3, 2, 4))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Nissan", model="ALtima")
print(my_car.make)

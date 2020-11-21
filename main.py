import showroom


class Car2:
    def __init__(self, identification, name, brand, price, active):
        self.identification = int(identification)
        self.name = str(name)
        self.brand = str(brand)
        self.price = int(price)
        self.active = bool(active)


array = [
    Car2(1, "MyLambo", "lambo", 150, True),
    Car2(2, "MyFerrari", "ferrari", 200, True),
    Car2(3, "MySkoda", "skoda", 50, True),
    Car2(4, "MyAudi", "audi", 170, False),
    Car2(5, "MyVw", "VW", 50, True),
    Car2(6, "MyOpel", "Opel", 120, True)
]


def main():

    showroom.add(Car2(7, "MyBMW", "BMW", 160, False))
    showroom.add(Car2(23, "Felicia", "Skoda", 50, True))
    showroom.add(Car2(1, "Octavia", "Skoda", 80, False))
    showroom.add(Car2(11, "Superb", "Skoda", 60, True))
    showroom.add(Car2(13, "GT", "Alfa Romeo", 200, True))
    showroom.updateName(23, "Octavia2")
    showroom.updateName(1, "Octavia 2015")
    showroom.getDatabase()


main()

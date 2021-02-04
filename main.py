#example for a simple class
class car:
    #constructor and member variables
    def __init__(self, color, brand):
        self.color=color
        self.brand=brand

    def accelerate(self):
        print(f"The {self.color} {self.brand} accelerates")

    def crash(self, object):
        print(f"The {self.color} {self.brand} crashed against a {object}!")


if __name__ == '__main__':
    first_car=car("red","audi")
    first_car.accelerate()
    first_car.crash("Wall")



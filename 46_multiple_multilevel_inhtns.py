class Animal:  # MULTI-LEVEL INHERITANCE

    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):  # MULTIPLE INHERITANCE
    pass


rabbit1 = Rabbit("Rabbit")
hawk1 = Hawk("Hawk")
fish1 = Fish("Fish")

rabbit1.flee()
hawk1.hunt()
fish1.flee()
fish1.hunt()
hawk1.sleep()
fish1.sleep()

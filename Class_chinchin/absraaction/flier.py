class Flyer:
    def fly(self, bird):
        bird.fly()


class Bird:
    def fly(self):
        print("flying")


class Chicken:
    def fly(self):
        print("chicken flying")


flyer1 = Flyer()
bird1 = Bird()
chicken1 = Chicken()

flyer1.fly(bird1)
flyer1.fly(chicken1)

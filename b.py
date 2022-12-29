class cat():
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name + " is eating")

my_cat = cat('juju'.title())
my_cat.eat()

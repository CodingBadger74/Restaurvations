class Dog():
    hungry = False
    breed = ''
    dirty = False
    friends = 0

    def play(self):
        self.hungry = True
        self.dirty = True
        self.friends += 1

    def eat(self):
        self.hungry = False

    def bathe(self):
        self.dirty = False

    def walk(self):
        self.hungry = True

def stats(name, object):
    print()
    print(name + ':')
    print('Hungry?', object.hungry)
    print('Breed:', object.breed)
    print('Dirty?', object.dirty)
    print('Friends:', object.friends)
    print()

# Ginger Bob Ross
ginger_bob_ross = Dog()

ginger_bob_ross.breed = 'Husky'
ginger_bob_ross.play()
ginger_bob_ross.eat()
ginger_bob_ross.bathe()
ginger_bob_ross.walk()

stats('Ginger Bob Ross', ginger_bob_ross)

# Mike
mike = Dog()

mike.breed = 'Pomeranian'
mike.play()
mike.bathe()
mike.eat()

stats('Mike', mike)

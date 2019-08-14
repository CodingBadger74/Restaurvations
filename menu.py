from random import *

sideList = ['kimchi', 'fruit salad', 'sauerkraut', 'escargot']
entréeList = ['pizza', 'haggis', 'pelmeni', 'sour cream porridge', 'squid tacos']
dessertList = ['chocolate cake', 'unicorn tears', 'a banana split', 'astronaut ice cream']
drinkList = ['Coca-Cola', 'sugar water', 'almond milk', 'raw eggs', 'mercury']

side = sideList[randint(0,len(sideList)-1)]
entrée = entréeList[randint(0,len(entréeList)-1)]
dessert = dessertList[randint(0,len(dessertList)-1)]
drink = drinkList[randint(0,len(drinkList)-1)]

input('''
Welcome to Chez Bronwen! Can I take your order?
''')
input('''What's that? You want me to pick the best items from our menu for you?
What a great idea! Let's see...
''')
input('''What do you think of this?
Your side is %s,
your entrée is %s,
your dessert is %s,
and your drink is %s!

How does that sound?
''' %(side, entrée, dessert, drink))
print('I\'m so happy to hear that! Enjoy your meal.')

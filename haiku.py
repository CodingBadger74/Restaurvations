#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
syl5 = ['An old silent pond...', 'splash! Silence again.', 'In the twilight rain', 'A lovely sunset.', 'A mountain village', 'the sound of water.', 'Over the wintry', 'with no leaves to blow.', 'when they strike the bell', 'Temple Kencho-ji', 'Temple bells die out.', 'A perfect evening!', 'Black cloudbank broken', 'Moon-lighted mountains!', 'April\'s air stirs in', 'Floats and balances']
syl7 = ['A frog jumps into the pond,', 'these brilliant-hued hibiscus-', 'under the piled-up snow', 'forest, winds howl in rage', 'these gingko leaves are falling-', 'The fragrant blossoms remain.', 'scatters in the night ... Now see', 'willow-leaves ... a butterfly']

#Generates a random integer.
random5 = randint(0, len(syl5)-1)
random7 = randint(0, len(syl7)-1)
newRandom5 = randint(0, len(syl5)-2)

for i in range(3):
    print()
print(syl5[random5])
syl5.remove(syl5[random5])
print(syl7[random7])
print(syl5[newRandom5])
for i in range(3):
    print()

'On a strange planet'
'Sunrise is irregular'
'Each day several dawns'

'Robin chick peeks out'
'Sees the world for the first time'
'Cheeps and ducks back in.'

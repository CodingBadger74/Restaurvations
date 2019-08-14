hairColors = ['Brown', 'Blue', 'Red', 'Blonde', 'Black', 'Purple']

#print(hairColors[2])

people = ['Bob Ross', 'Kendra', 'Liv', 'Taylor Swift', 'Lil Nas X', 'Kat']

#print(people[1] + ' has: ' + hairColors[1] + ' hair.')

peopleAndColors = {'Bob Ross' : 'Brown', 'Kendra' : 'Blue', 'Liv' : 'Red',
        'Taylor Swift' : 'Blonde', 'Lil Nas X' : 'Black', 'Kat' : 'Purple'}
# Key : Value

#print('Bob Ross has: ' + peopleAndColors['Bob Ross'] + ' hair.')

#name = 'Lil Nas X'

for i in range(0, len(people)):
    name = people[i]
    print(name + ' has: ' + peopleAndColors[name] + ' hair.')

print(list(peopleAndColors.keys())[1])
print('Brown' in peopleAndColors.values())

peopleAndColors.update({'Ed Sheeran' : 'Red'})
print(peopleAndColors)
peopleAndColors.pop('Ed Sheeran')
print(peopleAndColors)

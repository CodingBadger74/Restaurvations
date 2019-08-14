'''list = ['This', 'list', 'is', 'used', 'for', 'the', 'list.index()', 'demo.']

# Find the index of an item in the list
print(list.index('is'))
# output is 2

# This doesn't work if it is not in the list
#list.index('giraffe')

listList = [['This', 'contains'], ['lists', 'in', 'a', 'list!']]
print(listList.index(['This', 'contains']))

list[6] = 'blue'
print(list)

print(list[slice(1,4)])

print(list)
list.remove('This')
print(list)'''
x = [0, 1, 2, 3, 4]
y = ['a','b','c','d','e']
print(x, y)
x[4] = y[4]
print(x,y)

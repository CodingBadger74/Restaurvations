womenInTechList = ['Dorothy Vaughan', 'Jess Lee', 'Dr. Aprille Joy Ericsson', 'Cindy Alvarez', 'Amanda Randles', 'Ada Lovelace']
print(womenInTechList)
print(womenInTechList[1])
print(len(womenInTechList))
print('Dorothy Vaughan' in womenInTechList)

# These iterate over the list and print the same thing.
# This one creates a variable for an item in the list.
for woman in womenInTechList:
    print(woman)
for i in range(len(womenInTechList)):
    print(womenInTechList[i])

print(len(womenInTechList[3]))
print('da' in womenInTechList[5])
print(womenInTechList[5][6])
print(womenInTechList[5][4] + womenInTechList[5][7])
for letter in womenInTechList[1]:
    print(letter, end = '/')
print()

for woman in womenInTechList:
    if woman == 'Dr. Aprille Joy Ericsson':
        print(womenInTechList.index(woman))

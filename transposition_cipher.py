import math

def cipher_text():
    first_cipher_text = input('\nInput your ciphertext here:\n')
    # enable letters for key
    # check if valid key

    key = get_key_number()
    ciphertext = []

    for i in first_cipher_text:
        if i != ' ':
            ciphertext.append(i)

    columns = []

    for i in range(len(key)):
        columns.append([])

    # assuming padded - edit later
    column_length = int(len(ciphertext) / len(key))

    # sort into columns
    for i in range(len(key)):
        for j in range(column_length * i, column_length * (i + 1)):
                columns[i].append(ciphertext[j])

    print()
    # arrange columns
    for j in range(column_length):
        for num in key:
            print(columns[int(num) - 1][j], end='')
    print()

# dont want it to loop -- tons of issues here!
def get_key_number():
    key = input('\nInput your key here (numbers or keyword):\n')
    # need to check for wildcard characters
    nums = 0
    strs = 0
    for unit in key:
        if unit in '0123456789':
            nums += 1
        elif unit in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            strs += 1
    if (nums != 0 and strs != 0) or (nums == 0 and strs == 0):
        get_key_number()
    elif strs == 0:
        return key
    elif nums == 0:
        key_list = []
        sorted_list = []

        for letter in key:
            key_list.append(letter)
            sorted_list.append(letter)

        sorted_list.sort()

        for part in sorted_list:
#            print(part, key_list[key_list.index(part)], sorted_list.index(part))
            key_list[key_list.index(part)] = str(sorted_list.index(part) + 1)
            sorted_list[sorted_list.index(part)] = str(sorted_list.index(part) + 1)
    #        key_list[part] = sorted_list.index(key_list[part]) + 1

        new_key = ''
        for bit in key_list:
            new_key += bit

        return new_key

def plain_text():
    first_plain_text  = input('\nWhat would you like encrypted?\n')
    #key = input("\nWhat is your key (numbers or keyword)?\n")
    key = get_key_number()
    plaintext = []

    for i in first_plain_text:
        plaintext.append(i)

    columns = []
    
    for i in range(len(key)):
        columns.append([])

    # assuming padded - edit later
    column_length = int(len(plaintext) / len(key))

    # sort into columns
    for i in range(len(key)):
        for j in range(column_length * i, column_length * (i + 1)):
            columns[i].append(plaintext[j])

    print()
    # arrange columns
    for j in range(column_length):
        for num in key:
            print(columns[int(num) - 1][j], end='')
    print()

type_of_text = ''
while type_of_text.lower() != 'ciphertext' and type_of_text.lower() != 'plaintext':
    type_of_text = input('Would you like to input ciphertext or plaintext?\n')
if type_of_text.lower() == 'ciphertext':
    cipher_text()
else:
    plain_text()

'''
# must consider:
    not padded with x's
    word as key instead of #

DECRYPTING
1. Get ciphertext
2. Get key
3. Make dict with [key] # of keys
4. Break ciphertext into [key] groups
5. Assign groups to dict keys
6. Print first val in order, 2nd val in order, etc.

ENCRYPTING
1. Get plaintext
2. Get key
3. Make dict with [key] # of keys
4. Assign 1st val of plaintextto 1st key, etc.
5. Pad with X's
6. Print dict lists in number order
'''

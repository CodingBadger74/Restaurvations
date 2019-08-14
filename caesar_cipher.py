letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

input = input('What text to you want to decrypt/encrypt?\n')

cipher_text = []

for letter in input:
    cipher_text.append(letter.upper())

for i in range(26):
    print('Key =', 26 - i, end = ' ')
    plain_text = []
    for unit in range(len(cipher_text)):
        if cipher_text[unit] in letters:
            if i + letters.index(cipher_text[unit]) < 26:
                plain_text.append(letters[letters.index(cipher_text[unit]) + i])
            else:
                plain_text.append(letters[letters.index(cipher_text[unit]) + i - 26])
        else:
            plain_text.append(cipher_text[unit])
    for part in plain_text:
        print(part, end='')
    print()
    print()

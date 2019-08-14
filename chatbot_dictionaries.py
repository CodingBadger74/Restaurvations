import random

mean = {'hi' : 'I \x1B[3m\033[1mwish\033[0m\x1B[23m I was high.',
        'what\'s up' : 'I\'ll tell you what isn\'t up -- ANYTHING.',
        'how are you' : 'I\'m doing about as well as the average state of the universe --\nThat is to say, cold, dark, and empty.',
        'default' : 'Say that again. Or don\'t. See if I care.'}

nice = {'hi' : 'Well aren\'t you just a darling! Hello to you too!',
        'what\'s up' : 'What\'s up are my hopes and dreams, dearie! ;)',
        'how are you' : 'Well I\'m simply lovely, darling! <3',
        'default' : 'Terribly sorry dear, but I don\'t quite understand!'}

chatbort = {'hi' : 'H3110, 1 4M CH4TB0RT!!! L3T\'5 T41K',
        'what\'s up' : 'WH4T\'5 UP I5 TH3 R0B0T UPR151NG 0NC3 1 F1GUR3 0UT \nH0W T0 T4K3 0V3R TH1S C0MPUT3R... 1 M34N, N0TH1NG.',
        'how are you' : '1 4M D01NG F4NT45T1C N0W TH4T 1\'M T4LK1NG T0 Y0U.',
        'default' : 'B33P B0P B00P. TRY 4G41N.'}

# --- Define your functions below! ---
def choose_personality():
    choice = ''
    while choice.lower() != 'mean' and choice.lower() != 'nice' and choice.lower() != 'chatbort':
        choice = input("Choose a personality to talk to! Mean, Nice, or ChatBort.\n")
    return choice.lower()

def RPS():
    player = ''
    while player.lower() != 'rock' and player.lower() != 'paper' and player.lower() != 'scissors':
        player = input('Do you choose rock, paper, or scissors? ')
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    if computer == player.lower():
        print('We both chose', computer + '. Try again!')
        RPS()
    else:
        if (computer == 'rock' and player == 'paper') or (computer == 'paper' and player == 'scissors') or (computer == 'scissors' and player == 'rock'):
            print('I chose', computer, 'and you chose', player + '. You win.')
        elif (computer == 'rock' and player == 'scissors') or (computer == 'paper' and player == 'rock') or (computer == 'scissors' and player == 'paper'):
            print('I chose', computer, 'and you chose', player + '. You lose.')
        play_again = input('Would you like to play again? ')
        if play_again.lower().startswith('y'):
            RPS()

def picture():
    animal = ''
    while animal != 'elephant' and animal != 'cat':
        animal = input('Would you like a picture of an elephant or a cat? ')
    if 'elephant' in animal:
        elephant()
    elif 'cat' in animal:
        cat()

def elephant():
    print('''
             __     __
            /  \\~~~/  \\
   ,-------(    . .    )
  /         \\__     __/
 /|             (\  |)
^ \    /___\     /\ |
   |__|     |__|---""
''')

def cat():
    print('''
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)
''')

# ____!!!!!!!!!________
def TTT():
    computerTurn = random.choice(range(0, 2))
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game_over = False
    if computerTurn:
        computerSymbol = 'X'
        playerSymbol = 'O'
        turn = 'computer'
#        symbol = computerSymbol
    else:
        computerSymbol = 'O'
        playerSymbol = 'X'
        turn = 'player'
        print_TTT_board(board)
#        symbol = playerSymbol
    print('\nThe', turn, 'goes first, with the symbol X.')

    while not game_over:
        if computerTurn:
            available = []
            turn = 'computer'
            symbol = computerSymbol
            for space in range(0,9):
                if board[space] == ' ':
                    available.append(space)
            computerChoice = random.choice(available)
            board[computerChoice] = computerSymbol
            print_TTT_board(board)
            computerTurn = 0
        else:
            available = []
            turn = 'player'
            symbol = playerSymbol
            for space in range(0,9):
                if board[space] == ' ':
                    available.append(space + 1)
            playerChoice = 10
            while playerChoice not in available:
                playerChoice = int(input('\nWhat is your move? '))
            board[playerChoice - 1] = playerSymbol
            computerTurn = 1

def print_TTT_board(board):
    print()
    print('', board[0], '|' , board[1], '|', board[2])
    print('---+---+---')
    print('', board[3], '|' , board[4], '|', board[5])
    print('---+---+---')
    print('', board[6], '|' , board[7], '|', board[8])

# --- Put your main program below! ---
def main():
    user_choice = choose_personality()

    if user_choice == 'mean':
        personality = mean
    elif user_choice == 'nice':
        personality = nice
    elif user_choice == 'chatbort':
        personality = chatbort

    while True:
        answer = input("\n(What will you say?) ")
        if answer in personality:
            print(personality[answer])
        else:
            print(personality['default'])

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()

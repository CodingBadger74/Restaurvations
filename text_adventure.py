# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":
    print('You decide to go left and you see a giant monster blocking your path. Would you rather sneak past or fight the monster?') # Update to match your story.
    answer = input()
    if answer == "sneak past":
        print("Since you weren't quick enough, you get eaten by the monster. THE END")
    elif answer == "fight":
        print('Would you rather fight with a magical sword or a bow and arrow?')
        weapon = input()
        if weapon == "sword":
            print('''You draw your sword and impale the monster as it charges towards you.
As it lays dying, it whispers that it can help you escape the maze.
Do you listen?''')
            answer = input()
            if answer == 'yes':
                print('The monster whispers that a map of the maze can be found at northernmost point of the labyrinth.')
            elif answer == 'no':
                print('The monster dies XD. You have lost your chance of escaping the maze. You wander for eternity. THE END')
        elif weapon == 'bow and arrow':
            print('''As you grab your bow and arrow, your hands begin to burn.
You realize that they are covered in a dendrotoxin and your body has already begun to shut down.
As you collapse, you briefly see the monster barrelling towards you. THE END''')
elif user_input == "right":
    print("You choose to go right and you meet another person escaping the maze as well. Would you rather talk to the person or ignore them?") # Update to match your story.
    answer = input()
    if answer == 'talk':
        print("Let's help each other since 2 heads are better than one.")
        print("I see a drawing on the wall, it might be helpful for us to use to escape the maze")
        print('Would you rather inspect the drawing and use it or had walked past without knowing?')
        answer = input()
        if answer == 'inspect':
            print('You walk up to the drawing, inspecting it to find out that it is a part of a map.')
    if answer == 'ignore':
        print("You see a person, then you walk past them and go on your way to escape the maze.")
        

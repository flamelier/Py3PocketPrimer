'''
MIT License

Copyright (c) 2020 Flamelier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Imports time
import time 

# Imports Random
import random

# Defines main function
def main():
    print('Inside Main') # Debug

    inputChoice = playerInput()
    choicePlayer = playerChoice(inputChoice)
    choiceComputer = computerChoice()

    throwHands(choicePlayer, choiceComputer)

def playerInput():
    inputChoice = str.lower(input('Enter [r]ock, [p]aper, [s]cissor:\n'))
    inputConfirm = str.lower(input('You selected ' + inputChoice + ' are you sure? [y]es or [n]o.\n'))
    if inputConfirm == ('y'):
        return inputChoice
    elif inputConfirm == ('n'):
        playerInput()
    else:
        print('You didn\'t give a valid answer, please try again')
        playerInput()

def playerChoice(inputChoice):
    # Sets rock to 1
    if inputChoice == str('r'):
        choicePlayer = 1
        return choicePlayer
    # Sets paper to 2
    elif inputChoice == str('p'):
        choicePlayer = 2
        return choicePlayer
    # Sets scissor to 3
    elif inputChoice == str('s'):
        choicePlayer = 3
        return choicePlayer

def computerChoice():
    choiceComputer = random.randint(1,3)
    return choiceComputer

def throwHands(choicePlayer, choiceComputer):
    if choicePlayer == choiceComputer:
        tie()
        return
    elif choicePlayer > choiceComputer:
        playerWins()
        return
    elif choicePlayer < choiceComputer:
        computerWins()
        return

def computerWins():
    print('''
   _____ ____  __  __ _____  _    _ _______ ______ _____   __          _______ _   _  _____ 
  / ____/ __ \|  \/  |  __ \| |  | |__   __|  ____|  __ \  \ \        / /_   _| \ | |/ ____|
 | |   | |  | | \  / | |__) | |  | |  | |  | |__  | |__) |  \ \  /\  / /  | | |  \| | (___  
 | |   | |  | | |\/| |  ___/| |  | |  | |  |  __| |  _  /    \ \/  \/ /   | | | . ` |\___ \ 
 | |___| |__| | |  | | |    | |__| |  | |  | |____| | \ \     \  /\  /   _| |_| |\  |____) |
  \_____\____/|_|  |_|_|     \____/   |_|  |______|_|  \_\     \/  \/   |_____|_| \_|_____/ 
''')

def playerWins():
    print('''
  _____  _           __     ________ _____   __          _______ _   _  _____ 
 |  __ \| |        /\\\\ \   / /  ____|  __ \  \ \        / /_   _| \ | |/ ____|
 | |__) | |       /  \\\\ \_/ /| |__  | |__) |  \ \  /\  / /  | | |  \| | (___  
 |  ___/| |      / /\ \\\\   / |  __| |  _  /    \ \/  \/ /   | | | . ` |\___ \ 
 | |    | |____ / ____ \| |  | |____| | \ \     \  /\  /   _| |_| |\  |____) |
 |_|    |______/_/    \_\_|  |______|_|  \_\     \/  \/   |_____|_| \_|_____/ 
''')

def tie():
    print('''
  _______ _____ ______ 
 |__   __|_   _|  ____|
    | |    | | | |__   
    | |    | | |  __|  
    | |   _| |_| |____ 
    |_|  |_____|______|
''')

# Calls main function
main()
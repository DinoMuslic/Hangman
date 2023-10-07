import os
import sys
import random
import pandas as pd

os.system('cls');

def drawHangman(wrongAnswer):
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
========= \n''', '''
  +---+
  |   |
  O   |
      |
      |
      |
========= \n''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========= \n''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========= \n''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= \n''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= \n''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= \n''']
    
    if wrongAnswer == 0:
        print(HANGMANPICS[0])
    if wrongAnswer == 1:
        print(HANGMANPICS[1])
    if wrongAnswer == 2:
        print(HANGMANPICS[2])
    if wrongAnswer == 3:
        print(HANGMANPICS[3])
    if wrongAnswer == 4:
        print(HANGMANPICS[4])
    if wrongAnswer == 5:
        print(HANGMANPICS[5])
    if wrongAnswer == 6:
        print(HANGMANPICS[6])
    
def printLetters(wordLength):
    for i in range(len(letters)):
        print(letters[i], end="")

# fl = open("words.txt", "r")
# WORDS = fl.read()
# WORDS_LIST = WORDS.replace("\n", ' ').split(" ")
# WORDS_LIST_LENGTH = len(WORDS_LIST)
# fl.close()

df = pd.read_csv('hr_HR.csv')
wrds = df['abak'].tolist()
WORDS = []

for word in wrds:
    if word[0].isupper() == False:
        WORDS.append(word)

WORDS_LIST_LENGTH = len(WORDS)         

randomWord = random.choice(WORDS)
randomWordLength = len(randomWord)

RIGHT_ANSWER = randomWord

wrongAnswers = 0
rightAnswers = 0
guessedLetters = []
guessedRightLetters = []
letters = ["_ "] * randomWordLength
drawHangman(wrongAnswers)
printLetters(randomWordLength)

index = None
right = 0

while wrongAnswers < 6:
    print("\n")
    guess = str(input("Unesite slovo: "))
    if guess == "stop":
        sys.exit()

    if guess not in randomWord and guess not in guessedLetters and guess not in guessedRightLetters:
        wrongAnswers += 1
        guessedLetters.append(guess)
    else:
        for i in range(len(randomWord)):
            if guess == randomWord[i]:
                guessedRightLetters.append(guess)
                index = i
                right += 1
                randomWord = randomWord.replace(guess, " ", 1)
                letters[index] = f"{guess} "
                rightAnswers += right
                right = 0

    os.system('cls');
    drawHangman(wrongAnswers)
    printLetters(randomWordLength)
    print(f" ~~~  {guessedLetters}")
    if rightAnswers == randomWordLength:
            print("\nPOBIJEDILI STE!\n")
            break
    
if wrongAnswers == 6:
    print("\nIZGUBILI STE!\n")
    print("Trazena rijec:", RIGHT_ANSWER)
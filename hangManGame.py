import random, time, os

#Features I would like to add later
#keeps track of letters used and doesn't allow duplicates and will prompt user again.
#maybe creating a module for user input simplicity
#add an exit program command, ability to activte it at any time. s

listofAnswers = [
    'ambulance', 'butterfly', 'chocolate', 'elephant', 'firefighter',
    'guitarist', 'kangaroo', 'moonlight', 'parachute', 'watermelon'
]

HangManPics = [
    '''
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

while True:
    correctAnswer = random.choice(listofAnswers)

    blankSpaces = []
    for blank in range(len(correctAnswer)):
        blankSpaces.append("_")

    letterList = []
    for letter in correctAnswer:
        letterList.append(letter)

    wrongGuess = 0

    while wrongGuess <= 5:
        print("Welcome to the Hangman Game".center(40))
        print()
        print(HangManPics[wrongGuess])
        print(f"You have {6 - wrongGuess} guesses left.")

        for count in range(len(blankSpaces)):
            print(blankSpaces[count], end="")


        if letterList == blankSpaces:
            print(f"\nCongrats! The answer was {correctAnswer} You won!")
            time.sleep(1)
            print("🎉🎊🎉")
            time.sleep(1)
            break

        while True:  # User input
            try:
                userGuess = input("\nGuess" + " a letter.\n>").lower()
                if len(userGuess) != 1:
                    print("\Please enter only 1 character.")
                    time.sleep(1)
                    os.system("clear")
                    continue
                if not userGuess.isalpha():
                    print("Only letters of the alphabet, please.")
                    time.sleep(1)
                    os.system("clear")
                    continue
                break
            except TypeError:
                print("\rIncorrect input try again.")

        if userGuess in letterList:  # WIP
            print("Correct!")
            for number in range(len(letterList)):
                if letterList[number] == userGuess:
                    blankSpaces[number] = userGuess
            time.sleep(1)
        else:
            print("Wrong answer, Try again.")
            wrongGuess += 1
            time.sleep(1)
            continue

    if wrongGuess == 6:
        print("You loose!")
    print()

    again = input("Try again? (Y/N)").lower()
    if again == "y":
        print("Loading....")
        time.sleep(1)
        os.system("clear")
        continue
    elif again == "n":
        print("Thanks for playing.")
        break
    else:
        print("Invalid answer. Program will now end.")
        break

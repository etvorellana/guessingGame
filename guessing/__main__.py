from . guessingGame import GuessingGame

def main():
    print("Welcome to the guessing game!")
    print("First you will guess a number between 1 and 100.")
    game = GuessingGame()
    game.play()
    game.changeGameKind()
    game.play()
    print("Thanks for playing!")

if __name__ == '__main__':
    main()

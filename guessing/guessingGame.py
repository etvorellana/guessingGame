import random

class GuessingGame:
    def __init__(self, player = True, gap = 100, max_guesses = 8):
        self.__player = player
        self.__gap = gap
        self.__name = input("What is your name? ")
        if self.__player:
            self.__number = random.randint(1, gap+1)
        self.__maxGuesses = max_guesses
        self.__guesses = 0
        self.__guess = 0

    def playerGuess(self):
        print("Hi " + self.__name + ", I'm thinking of a number!!!")
        while self.__guess != self.__number:
            self.__guess = int(input("Guess a number between 1 and " + str(self.__gap) + ": "))
            self.__guesses += 1
            if self.__guess > self.__number:
                print("Too high!")
            elif self.__guess < self.__number:
                print("Too low!")
            else:
                print( "Congratulations {}, you got it!".format(self.__name))
                print("It took you {} guesses.".format(self.__guesses))
                break
            if self.__guesses == self.__maxGuesses:
                print("You ran out of guesses!")
                break
                

    def __computerAsk(self, low, high,):
        print("Hi {}, is your number {}?".format(self.__name, self.__guess))
        answer = input("Enter 'h' if your number is higher, 'l' if your number is lower, or 'c' if I guessed correctly: ")
        answer = answer.lower()
        if answer == 'l':
            high = self.__guess
            self.__payerAnswers.append(answer)
            return low, high, False
        elif answer == 'h':
            low = self.__guess
            self.__payerAnswers.append(answer)
            return low, high, False
        elif answer == 'c':
            print("I guessed it in {} guesses!".format(self.__guesses))
            return low, high, True
        else:
            print("I don't understand your input.")
            return self.__computerAsk(low, high)
    
    
    def __verify(self, number):
        low = 1
        high = self.__gap
        for answer in self.__payerAnswers:
            self.__guess = (low + high) // 2
            if answer == 'h':
                if self.__guess >= number:
                    print("You lied to me!")
                    print("I guessed it in {} guesses!".format(self.__guesses))
                    #print("Your number was {}.".format(number))
                    print("{} is not higher than {}.".format(number, self.__guess))
                    break
                else:
                    low = self.__guess
            elif answer == 'l':
                if self.__guess <= number:
                    print("You lied to me!")
                    #print("I guessed it in {} guesses!".format(self.__guesses))
                    print("Your number was {}.".format(number))
                    print("{} is not lower than {}.".format(number, self.__guess))
                    break
                else:
                    high = self.__guess
        
    def changeGameKind(self):
        self.__player = not self.__player
        self.__guesses = 0
        self.__guess = 0
    
    def resetGame(self, player = True, gap = 100, max_guesses = 8):
        self.__guesses = 0
        self.__guess = 0
        self.__player = player
        self.__gap = gap
        self.__maxGuesses = max_guesses
        
    def computerGuess(self):
        self.__payerAnswers = []
        print("Hi {}!!! Pick a number between 1 and {}: ".format(self.__name, self.__gap))
        #self.__number = int(input("Pick a number between 1 and {}: ".format(self.__gap)))
        low = 1
        high = self.__gap
        while True:
            self.__guess = (low + high) // 2
            self.__guesses += 1
            low, high, correct = self.__computerAsk(low, high)
            if correct:
                break
            if self.__guesses == self.__maxGuesses:
                print("I ran out of guesses!")
                number = int(input("What was your number? "))
                self.__verify(number)
                break
    
    def play(self):
        if self.__player:
            self.playerGuess()
        else:
            self.computerGuess()
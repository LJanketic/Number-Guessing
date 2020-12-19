import random

class numberGuesser:
    def __init__(self, rangeMin = 0, rangeMax = 100):
        self.solution = random.randint(rangeMin, rangeMax)
        self.rangeMin = rangeMin
        self.rangeMax = rangeMax
        self.counter = 0

    def isCorrect(self):
        print("Guess the number in range from "+ str(self.rangeMin) + " and " + str(self.rangeMax) +"\n") 
        while True:
            guess = int(input())
            if guess == self.solution:
                print("\nThat is the correct number!\n")
                print("You guessed the number in "+ str(self.counter)+ " attempts")
                break
            elif (guess <= self.solution) and (guess >= self.rangeMin):
                self.counter += 1
                print("Incorrect! The number you are looking for is greater than your guess.\n")
            elif (guess >= self.solution) and (guess <= self.rangeMax):
                self.counter += 1
                print("Incorrect! The number you are looking for is lesser than your guess.\n")
            else: 
                print("The number you have entered is out of the designated scope!\n")

game = numberGuesser()
game.isCorrect()

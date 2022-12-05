from random import randint
from time import sleep
import sys
from colorama import Fore


#TODO Game end system

class Mastermind():
    def __init__(self):
        self.code = []
        self.connected = []
        self.current_round = 0
        self.t_results = []
        self.t_guesses = []
        self.txt_time = 0.05


        print(Fore.LIGHTBLACK_EX + "Welcome to Mastermind")
        sleep(self.txt_time)
        print("The computer will randomley select a code")
        sleep(self.txt_time)
        print("The code is made up of colors: red, yellow, green, blue, purple, and white")
        sleep(self.txt_time)
        print("These colors are represented by their first letter")
        sleep(self.txt_time)
        print("After every guess, the computer will tell you how many were in the right place and right spot")
        sleep(self.txt_time)
        print("And how many were in the right place wrong spot")
        sleep(self.txt_time)
        print("You have 10 tries")
        sleep(self.txt_time)
        print("At any time, press end to end the game")
        sleep(self.txt_time)
        print("From there, you can start a new game or quit the program")
        sleep(self.txt_time)
        print("Good luck!")
        sleep(self.txt_time)

    
    def guess(self, guess):
        if self.playing == True:
            guess = [int(self.convert_to_in(guess[0])),int(self.convert_to_in(guess[1])),int(self.convert_to_in(guess[2])),int(self.convert_to_in(guess[3])),]
            self.connected = [[],[]]
            self.results = []
            for i in range(4):

                if guess[i] == self.code[i]:
                    self.results.append(2)
                    self.connected[0].append(i)
                    self.connected[1].append(i)


            for i in range(4):
                for j in range(4):
                    if guess[i] == self.code[j]:
                        if self.connected[0].count(i) == 0 and self.connected[1].count(j) == 0:
                            self.results.append(1)
                            self.connected[0].append(i)
                            self.connected[1].append(j)


            

            self.update(self.results, guess)
            return self.results

    def update(self, result, guess):
        self.t_results.append(result)
        self.t_guesses.append(guess)
        self.current_round += 1



    def convert_to_out(self, input):
        
        if input == 0:
            return "r"
        elif input == 1:
            return "y"
        elif input == 2:
            return "g"
        elif input == 3:
            return "b"
        elif input == 4:
            return "p"
        elif input == 5:
            return "w"


    def convert_to_in(self, input):
        if input == 'r':
            return 0
        elif input == 'y':
            return 1
        elif input == 'g':
            return 2
        elif input == 'b':
            return 3
        elif input == 'p':
            return 4
        elif input == 'w':
            return 5


    def display(self):
        if self.playing:
            print('-------------')
            for i in range(self.current_round):
                print(f'{i} - ',end='')
                self.color(self.t_guesses[i][0])
                print(f'|{self.convert_to_out(self.t_guesses[i][0])}|',end='')
                self.color(self.t_guesses[i][1])
                print(f'|{self.convert_to_out(self.t_guesses[i][1])}|',end='')
                self.color(self.t_guesses[i][2])
                print(f'|{self.convert_to_out(self.t_guesses[i][2])}|',end='')
                self.color(self.t_guesses[i][3])
                print(f'|{self.convert_to_out(self.t_guesses[i][3])}|',end='')
                self.color(11)

                print(f' |Right color right place: {self.t_results[i].count(2)}|',end='')
                print(f' |Right color wrong place: {self.t_results[i].count(1)}|')


                #print(f'{i} - |{self.convert_to_out(self.t_guesses[i][0])}|{self.convert_to_out(self.t_guesses[i][1])}|{self.convert_to_out(self.t_guesses[i][2])}|{self.convert_to_out(self.t_guesses[i][3])}| |Right color right plade: {self.t_results[i].count(2)}| |Right color wrong place: {self.t_results[i].count(1)}|')
            print('-------------')

    def usr_input(self):
        print("-------------")
        print("Enter guess")
        print("-------------")
        guess = input()
        if guess == 'end':
            self.end_game(0)
        
        
        return guess


    def round(self):
        self.guess(self.usr_input())
        self.display()
    
    def start_game(self):
        self.code = [randint(0,5), randint(0,5), randint(0,5), randint(0,5)]
        #self.code = [1,0,5,0]
        self.connected = []
        self.current_round = 0
        self.t_results = []
        self.t_guesses = []
        self.playing = True


        for i in range(10):
            self.round()
            if i == 10:
                self.end_game(1)
            if not self.playing:
                break
        
    def color(self, input):
        if input == 0:
            print(Fore.RED,end='')
        elif input == 1:
            print(Fore.YELLOW,end='')
        elif input == 2:
            print(Fore.GREEN,end='')
        elif input == 3:
            print(Fore.BLUE,end='')
        elif input == 4:
            print(Fore.MAGENTA,end='')
        elif input == 5:
            print(Fore.WHITE,end='')
        elif input == 11:
            print(Fore.LIGHTBLACK_EX,end='')


    def end_game(self, code):
        self.playing = False
        if code == 0:
            print("------------------------")
            print("Game ended by user input")
            self.end_code = str(f'|{self.convert_to_out(self.code[0])}|{self.convert_to_out(self.code[1])}|{self.convert_to_out(self.code[2])}|{self.convert_to_out(self.code[3])}|')
            print(f"The code was: {self.end_code}")
            print("------------------------")
            print("Type 'play' to play again OR type quit to 'quit' the program")
            inp = input()
            if inp == 'play':
                self.start_game()
            elif inp == 'quit':
                print("------------------------")
                print("Program ended by user input")
                print("------------------------")
                sys.exit(0)
        if code == 1:
            print("------------------------")
            print("Game Over")
            print("You win!!!")
            print()
                














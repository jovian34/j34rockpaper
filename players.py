import random


class Player(object):

    def __init__(self):
        self.score = 0
        self.choice = 'START'

    def add_to_score(self):
        self.score += 1


class Human(Player):

    def get_user_input(self):
        options = ['r', 'p', 's']
        print('choose (r)ock, (p)aper, or (s)cissors: ', end='')
        self.choice = input()
        if self.choice[0].lower() in options:
            self.choice = self.choice[0].lower()
        else:
            print('Invalid choice... please try again.')
            return self.get_user_input()

    def process_choice(self):
        if self.choice == 'r':
            print('You chose rock!')
            self.choice = 'rock'
        if self.choice == 'p':
            print('You chose paper!')
            self.choice = 'paper'
        if self.choice == 's':
            print('You chose scissors!')
            self.choice = 'scissors'

    def set_user_choice(self):
        self.get_user_input()
        self.process_choice()


class Computer(Player):

    def set_random_choice(self):
        self.choice = random.randint(1, 3)

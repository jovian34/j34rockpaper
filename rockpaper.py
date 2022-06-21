from re import I
from players import Human, Computer
from showdown import Showdown
from os import environ, system, name
from time import sleep


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    environ['TERM'] = 'xterm'
    human = Human()
    computer = Computer()
    showdown = Showdown()
    while human.score < 10 and computer.score < 10:
        print(f'Human: {human.score} ... '
              f'Computer: {computer.score}')
        print('====================================================')
        human.set_user_choice()
        computer.set_random_choice()
        showdown.showdown_map[(human.choice, computer.choice)](human, computer)
        sleep(3)
        clear_screen()
    if human.score > computer.score:
        print('Human wins by score '
              f'of {human.score} to {computer.score}')
    else:
        print('Computer wins by score '
              f'of {computer.score} to {human.score}')


if __name__ == '__main__':
    main()
    
        



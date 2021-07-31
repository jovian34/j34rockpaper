import players
from os import environ, system, name
from time import sleep


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def rock_crushes_scissors(h_obj, c_obj):
    print('Rock crushes scissors. Human Wins!')
    print('-------------------------------------')
    h_obj.add_to_score()
    

def rock_smothered_by_paper(h_obj, c_obj):
    print('Paper smothers rock. Computer Wins!')
    print('-------------------------------------')
    c_obj.add_to_score()
    

def paper_smothers_rock(h_obj, c_obj):
    print('Paper smothers rock. Human Wins!')
    print('-------------------------------------')
    h_obj.add_to_score()
    

def paper_cut_by_scissors(h_obj, c_obj):
    print('Scissors cut paper. Computer Wins!')
    print('-------------------------------------')
    c_obj.add_to_score()
    

def scissors_cut_paper(h_obj, c_obj):
    print('Scissors cut paper. Human Wins!')
    print('-------------------------------------')
    h_obj.add_to_score()
    

def scissors_crushed_by_rock(h_obj, c_obj):
    print('Rock crushes scissors. Computer Wins!')
    print('-------------------------------------')
    c_obj.add_to_score()
    

def rock_push(h_obj, c_obj):
    print("Computer also chose Dwayne Johnson. We're all getting our Rocks on today!")
    print('------------------------------------')


def paper_push(h_obj, c_obj):
    print('Computer chose Paper too. Paper is on sale by the case at Office Depot!!!!')
    print('------------------------------------')
    

def scissor_push(h_obj, c_obj):
    print('Computer also chose Scissors. Dead Again is a great movie BTW!')
    print('--------------------------------------')
    

showdown_map = {
    ('rock', 3): rock_crushes_scissors,
    ('rock', 2): rock_smothered_by_paper,
    ('paper', 1): paper_smothers_rock,
    ('paper', 3): paper_cut_by_scissors,
    ('scissors', 2): scissors_cut_paper,
    ('scissors', 1): scissors_crushed_by_rock,
    ('rock', 1): rock_push,
    ('paper', 2): paper_push,
    ('scissors', 3): scissor_push,
}


def main():
    environ['TERM'] = 'xterm'
    human = players.Human()
    computer = players.Computer()
    while human.score < 10 and computer.score < 10:
        print(f'Human: {human.score} ... '
              f'Computer: {computer.score}')
        print('====================================================')
        human.set_user_choice()
        computer.set_random_choice()
        showdown_map[(human.choice, computer.choice)](human, computer)
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
    
        



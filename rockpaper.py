import players


def one_three(h_obj, c_obj):
    print('Rock crushes scissors. Human Wins!')
    print('-------------------------------------')
    h_obj.add_to_score()
    

def one_two(h_obj, c_obj):
    print('Paper smothers rock. Computer Wins!')
    print('-------------------------------------')
    c_obj.add_to_score()
    

def two_one(h_obj, c_obj):
    print('Paper smothers rock. Human Wins!')
    print('-------------------------------------')
    h_obj.add_to_score()
    

def two_three(h_obj, c_obj):
    print('Scissors cut paper. Computer Wins!')
    print('-------------------------------------')
    c_obj.add_to_score()
    

def three_two(h_obj, c_obj):
    print('Scissors cut paper. Human Wins!')
    print('-------------------------------------')
    h_obj.add_to_score()
    

def three_one(h_obj, c_obj):
    print('Rock crushes scissors. Computer Wins!')
    print('-------------------------------------')
    c_obj.add_to_score()
    

def one_one(h_obj, c_obj):
    print('Were all getting our Rocks on today!')
    print('------------------------------------')


def two_two(h_obj, c_obj):
    print('Paper is on sale by the case at Office Depot!!!!')
    print('------------------------------------')
    

def three_three(h_obj, c_obj):
    print('Scissors! Dead Again is a great movie!')
    print('--------------------------------------')
    
showdown_map = { 
    (1, 3): one_three,
    (1, 2): one_two,
    (2, 1): two_one,
    (2, 3): two_three,
    (3, 2): three_two,
    (3, 1): three_one,
    (1, 1): one_one,
    (2, 2): two_two,
    (3, 3): three_three,
}


def main():
    human = players.Human()
    computer = players.Computer()
    while human.score < 10 and computer.score < 10:
        print(f'Human: {human.score} ... '
              f'Computer: {computer.score}')
        print('====================================================')
        showdown_map[(human.user_output(), computer.get_random())](human, computer)
    if human.score > computer.score:
        print('Human wins by score '
              f'of {human.score} to {computer.score}')
    else:
        print('Computer wins by score '
              f'of {computer.score} to {human.score}')


if __name__ == '__main__':
    main()
    
        



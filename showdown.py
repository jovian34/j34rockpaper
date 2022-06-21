

class Showdown:

    def __init__(self) -> None:
        self.showdown_map = {
            ('rock', 3): self.rock_crushes_scissors,
            ('rock', 2): self.rock_smothered_by_paper,
            ('paper', 1): self.paper_smothers_rock,
            ('paper', 3): self.paper_cut_by_scissors,
            ('scissors', 2): self.scissors_cut_paper,
            ('scissors', 1): self.scissors_crushed_by_rock,
            ('rock', 1): self.rock_push,
            ('paper', 2): self.paper_push,
            ('scissors', 3): self.scissor_push,
        }

    def rock_crushes_scissors(self, h_obj, c_obj):
        print('Rock crushes scissors. Human Wins!')
        print('-------------------------------------')
        h_obj.add_to_score()
        

    def rock_smothered_by_paper(self, h_obj, c_obj):
        print('Paper smothers rock. Computer Wins!')
        print('-------------------------------------')
        c_obj.add_to_score()
        

    def paper_smothers_rock(self, h_obj, c_obj):
        print('Paper smothers rock. Human Wins!')
        print('-------------------------------------')
        h_obj.add_to_score()
        

    def paper_cut_by_scissors(self, h_obj, c_obj):
        print('Scissors cut paper. Computer Wins!')
        print('-------------------------------------')
        c_obj.add_to_score()
        

    def scissors_cut_paper(self, h_obj, c_obj):
        print('Scissors cut paper. Human Wins!')
        print('-------------------------------------')
        h_obj.add_to_score()
        

    def scissors_crushed_by_rock(self, h_obj, c_obj):
        print('Rock crushes scissors. Computer Wins!')
        print('-------------------------------------')
        c_obj.add_to_score()
        

    def rock_push(self, h_obj, c_obj):
        print("Computer also chose Dwayne Johnson. We're all getting our Rocks on today!")
        print('------------------------------------')


    def paper_push(self, h_obj, c_obj):
        print('Computer chose Paper too. Paper is on sale by the case at Office Depot!!!!')
        print('------------------------------------')
        

    def scissor_push(self, h_obj, c_obj):
        print('Computer also chose Scissors. Dead Again is a great movie BTW!')
        print('--------------------------------------')
        

    
import random

class RockPaperScissors:

    def __init__(self,name,):
        self.choices =['rock','paper','scissors']
        self.player_name=name
    
  
    def get_user_choice(self):
        user_choice= input(f"enter your choice({self.choices}):")
        if user_choice.lower() in self.choices:
            return user_choice.lower()

        print(f'invalidchoice you must select from  {self.choices}.')
        return self.get_user_choice()
    
    def get_computter_choice(self):
            return random.choice(self.choices)

    def decide_winner(self,user_choice,computter_choice):
         if user_choice==computter_choice:
             return"it is tie"

         win_combinations =[('rock','scissors'),('paper','rock'),('scissors','paper')]
         for win_comp in win_combinations:
            if (user_choice==win_comp[0])&(computter_choice==win_comp[1]):
                 return "congraguations!you won!"
        
        
         return "oh no computter won"

    def play(self):
        user_choice= self.get_user_choice()
        computter_choice= self.get_computter_choice()
        winner_msg=self.decide_winner(user_choice,computter_choice)
        print(f'computterChoice:{computter_choice}')
        print(winner_msg)




if __name__== '__main__':
     game=RockPaperScissors("Negar")

while True:
    game.play()

    continue_game=input('do you want to play again (enter any key  to play again,enter q/Q toexit)')
    if continue_game.lower()=='q':
        break

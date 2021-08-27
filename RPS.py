import math   ## Completely useless need for math class
from random import randrange


User_Choice = ""  


## Global Variable
Rock = 'rock'
Paper = 'paper'
Sissors = 'sissors'



## I can't spell.
def RNP():

    print( "ROCK PAPER SISSORS SHOOT!....... \n")

    
    
    
def Basic_Function():
    User_Choice = ""
    ## Makes sure the user's answers are in line or makes sure the user actually answers 

    while(len(User_Choice)) == 0 or (Paper not in User_Choice) or (Rock not in User_Choice) or (Sissors not in User_Choice):
        User_Choice = input("Please pick betweeen Rock , Paper, Sissors")

        if Rock in User_Choice:

            return User_Choice

        elif Paper in User_Choice:

            return User_Choice

        elif Sissors in User_Choice:

            return User_Choice

          
          
 # If statements for each choice         
def Logic_of_Game():

   Answer = Basic_Function()
   RPS_List = ['rock', 'paper', 'sissors']
   Decider = randrange(0, 3)    # Will pick through the different index of the  RPS_list 

   print(Answer.capitalize(), "VS ",RPS_List[Decider].capitalize() )
  
  
  #A BUNCH OF IF STATEMENTS 

   if( Rock in RPS_List[Decider]):

        if( Rock in Answer):
            print(" It is a tie!")

        if (Sissors in Answer):
            print("Sorry you lose :(")

        if(Paper in Answer ):
            print( " Winner winner chicken dinner!")

   if (Paper in RPS_List[Decider]):

       if (Paper in Answer):
           print(" It is a tie!")

       if (Sissors in Answer):
           print("Sorry you lose :(")

       if (Rock in Answer):
           print(" Winner winner chicken dinner!")

   if (Sissors in RPS_List[Decider]):

       if (Sissors in Answer):
           print(" It is a tie!")

       if (Paper in Answer):
           print("Sorry you lose :(")

       if (Rock in Answer):
           print(" Winner winner chicken dinner!")


RNP()

Logic_of_Game()


Question = ""

while(len(Question)==0):
    Question = input("Would you like to continue?")

    if('y'in Question.lower()):
        RNP()
        Logic_of_Game()

        continue

    else:

      print("Thanks for playing")

from random import randrange


User_Choice = ""

Rock = 'rock'
Paper = 'paper'
Sissors = 'sissors'

def RNP():

    print( "ROCK PAPER SISSORS SHOOT!....... \n")

def Basic_Function():
    User_Choice = ""
    Final_Choice = User_Choice

    while(len(User_Choice)) == 0 or (Paper not in User_Choice) or (Rock not in User_Choice) or (Sissors not in User_Choice):
        User_Choice = input("Please pick betweeen Rock , Paper, Sissors")

        if Rock in User_Choice:

            return User_Choice

        elif Paper in User_Choice:

            return User_Choice

        elif Sissors in User_Choice:

            return User_Choice

def Logic_of_Game():

   Answer = Basic_Function()
   RPS_List = ['rock', 'paper', 'sissors']
   Decider = randrange(0, 3)

   print(Answer.capitalize(), "VS ",RPS_List[Decider].capitalize() )

   if( Rock in RPS_List[Decider]):

        if( Rock in Answer):
            print(" It is a tie!")

        if (Paper in Answer):
            print("Sorry you lose :(")

        if(Sissors in Answer ):
            print( " Winner winner chicken dinner!")

   if (Paper in RPS_List[Decider]):

       if (Paper in Answer):
           print(" It is a tie!")

       if (Rock in Answer):
           print("Sorry you lose :(")

       if (Sissors in Answer):
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

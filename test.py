#Instructions
#ROCK PAPER SCISSORS
#The Game Instructions to USer/Player
import random
print("Winning rule for the Rock paper Scissors Game as follows: \n"
      +"\tRock vs paper -> paper wins \n"
      +"\tRock vs scissors -> Rock wins \n"
      +"\tPaper vs scissors -> scissors wins \n")
while True:
#Tell the User to enter either Rock, Paper, Scissors
    print("Enter choice\n 1.rock\n 2.paper\n 3.scissors\n")
    while True:
#Get the response from the user
        user_choice = input("User turn:>")
        user_choice = user_choice.lower()
        
        if user_choice not in ['rock','paper','scissors']:
            print("Wrong input, please enter again")
        else:
            break
#Print the response from the user
    print("User choice is: "+user_choice+"\n")

#Computer chooses randomly between Rock, Paper, Scissors
    comp_choice = random.choice(['rock','paper','scissors'])
#Print computer choice
    print("Computer choice is: "+comp_choice+"\n")

#Print User choice and Computer choice
    print("\t" +user_choice+ "\n V/s \n"+"\t"+comp_choice)

#Decide the condition of winning according to the Game Instructions
    result = None

    if((user_choice == "rock" and comp_choice =="paper") or
           (user_choice == "paper" and comp_choice == "paper")):
            result = "paper"
    elif((user_choice == "rock" and comp_choice == "scissors") or
             (user_choice == "scissors" and comp_choice == "rock")):
             result = "rock"
    else:
            result = "scissors"
         
#Compare the result with the user and computer
#Printing either user or computer wins
    
    if(user_choice == comp_choice):
            print("<==Draw==>")
    elif(result == user_choice):
            print("<==User Wins==>")
    else:
            print("<==Computer Wins==>")
    
#Get the response from User to play Again
    while(True):
        ans = input("<Do you want to play again? (Y/N)>")
        if ans not in ['n','N','y','Y']:
                print("Wrong input, please enter again")
        else:
                break
#Check the response from User and continue the loop
#Otherwise break the loop to close the game
    if(ans == 'n' or ans =='N'):
        break

#Print a Thanks Message to the user
print("\n<<<<<Thanks for playing Rock Paper Scissors Game :)>>>>>\n")
        
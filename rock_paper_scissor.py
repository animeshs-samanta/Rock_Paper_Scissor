import random

print("-----------------Rules of the game----------------------")
print("Rock vs Paper => Paper Wins")
print("Rock vs Scissor => Rock Wins")
print("Paper vs Scissor => Scissor Wins")

while True:
    print("\n1. Rock \n2. Paper \n3. Sciissor \n\nEnter your choice: ")
    user=int(input())
    
    while user > 3 or user < 1:
        print("\nWrong Choice!,\nEnter new choice: ")
        user=int(input())
        
    if (user==1):
        user_choice = "Rock"
    elif (user == 2):
        user_choice = "Paper"
    else:
        user_choice = "Scissor"

    print("\nThe user's choice is: ", user_choice)
    print("\nNow Computer's Turn: ")
    
    computer = random.randint(1,3)
    while(computer==user):
        computer=random.randint(1,3)
        
    if (computer==1):
        computer_choice = "Rock"
    elif (computer == 2):
       computer_choice = "Paper"
    else:
       computer_choice = "Scissor"

    print("\nThe computer's choice is: ", computer_choice)
        
    
    print("\n------------USER    VS     COMPUTER---------")
    
    if(user==computer):
        print("\nThe Game Is Draw")
        
    if(user==1 and computer==2):
        print("\nComputer Win ", end=" ")
        print("\nRock vs Paper => Paper Wins")

    elif(user==1 and computer==3):
        print("\nUser Win ", end=" ")
        print("\nRock vs Scissor => Rock Wins")
        
    elif(user==2 and computer==1):
        print("\nUser Win ", end=" ")
        print("\nRock vs Paper => Paper Wins")
        
    elif(user==2 and computer==3):
        print("\nComputer Win ", end=" ")
        print("\nPaper vs Scissor => Scissor Wins")
        
    elif(user==3 and computer==1):
        print("\nComputer Win ", end=" ")
        print("\nRock vs Scissor => Rock Wins")
        
    elif(user==3 and computer==2):
        print("\nUser Win ", end=" ")
        print("\nPaper vs Scissor => Scissor Wins")

    
    print("\nDo you want to play again? (Y/N)")
    ans=input().lower()
    if ans=='n':
        break
    
print("\n-----Thanks For Playing-----")

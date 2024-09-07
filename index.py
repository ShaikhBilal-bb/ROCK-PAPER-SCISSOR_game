import random

userpoint=0
comppoint=0
def user_choice():
    words=["rock","paper","scissor"]
    choice=input("Enter your selction among Rock, Paper, Scissor: ").lower()
    if choice in words:
        return choice
    else:
        print("Invalid choice , You lost a turn!")
        return 0

def comp_choice():
    return random.choice(["rock","paper","scissor"])

def check_round(userchoice,compchoice):
    global userpoint,comppoint
    if userchoice==compchoice:
        return "Tie"
    elif  (userchoice=="rock"and compchoice=="scissor") or (userchoice=="paper" and compchoice=="rock")or(user_choice=="scissor" and compchoice=="paper"):
        userpoint+=1
        return "user wins this round"
    else:
        comppoint+=1
        return "computer wins this round"

def overallwinner(userpoint,comppoint):
    if userpoint>comppoint:
        return "user wins the game"
    elif userpoint<comppoint:
        return "computer wins the game"
    else:
        return "it's a tie"
def main():
    
    print("Welcome to Rock,Paper,Scissor game\n Its made by Soumodeep Das\n")
    n=int(input("Enter how many Rounds of game you want to play:"))
    for i in range(0,n):
        userchoice=user_choice()
        if userchoice:
            compchoice=comp_choice()
            print("Computer chose: ",compchoice)
            print("You chose: ",userchoice)
            print(check_round(userchoice,compchoice))
        else:
            continue
        print("Score - You: ",userpoint," Computer: ",comppoint)
    print(overallwinner(userpoint,comppoint))
    return 0
main()
    
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
#Write your code below this line 👇
decisionUser = -1
while decisionUser > 2 or decisionUser < 0:
    decisionUser = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    decisionCPU = random.randint(0,2)
    movement = ""

    if(decisionUser == 0):
        movement = "User chose Rock:\n"+rps[0]
        if(decisionCPU == 1):
            movement += "\nCPU chose Paper:\n"+rps[1]+"\n ***CPU Wins***"
        elif(decisionCPU == 2):
            movement += "\nCPU chose Scissors:\n"+rps[2]+"\n ***User Wins***"
        elif(decisionCPU == 0):
            movement += "\nCPU chose Rock:\n"+rps[0]+"\n ***It's a tie***"
    elif(decisionUser == 1):
        movement = "User chose Paper:\n"+rps[1]
        if(decisionCPU == 0):
            movement += "\nCPU chose Rock:\n"+rps[0]+"\n ***User Wins***"
        elif(decisionCPU == 1):
            movement += "\nCPU chose Paper:\n"+rps[1]+"\n ***It's a tie***"
        elif(decisionCPU == 2):
            movement += "\nCPU chose Scissors:\n"+rps[2]+"\n ***CPU Wins***"
    elif(decisionUser == 2):
        movement = "User chose Scissors:\n"+rps[2]
        if(decisionCPU == 0):
            movement += "\nCPU chose Rock:\n"+rps[0]+"\n ***CPU Wins***"
        elif(decisionCPU == 1):
            movement += "\nCPU chose Paper:\n"+rps[1]+"\n ***User Wins***"
        elif(decisionCPU == 2):
            movement += "\nCPU chose Scissors:\n"+rps[2]+"\n ***It's a tie***"
    else:
        print("Incorrect Number, please try again with (0-2)")

print(movement)




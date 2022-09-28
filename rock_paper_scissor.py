


print("\n\n\n\t\t\t\t\t\t\t\t\t ***** ROCK PAPER SCISSOR GAME ***** ")

import random

nam=' '
name=input("\n\n\n\t ENTER YOUR NAME ::: ")
nam=name.upper()
print("\n\n\t\t\t\t\t\t\t\t_____________________________________________________")
print("\n\t\t\t\t\t\t\t\t\t     WELCOME {} TO OUR GAME ".format(nam))
print("\n\t\t\t\t\t\t\t\t_____________________________________________________")

flag=0
flag2=0
flag3=0
for i in range(3):
    value=random.randint(1,3)
    

    choice=input("\n\n\n\n\t\t CHOOSE WHAT YOU WANT:- \n\n\t\t 1.ROCK \n\n\t\t 2.PAPER \n\n\t\t 3.SCISSOR \n\n\t\t ENTER :::")

    if value==1 and choice=="paper" or choice=="PAPER":
        print("\n\n\t\t YOU WON BECAUSE COMPUTER CHOOSE ROCK AND YOU CHOOSE PAPER")
        flag+=1
        
    elif value==1 and choice=="scissor" or choice=="SCISSOR":
        print("\n\n\t\t YOU LOSE BECAUSE COMPUTER CHOOSE ROCK AND YOU CHOOSE SCISSOR")
        flag3+=1

    elif value==1 and choice=="rock" or choice=="ROCK":
        print("\n\n\t\t DRAW! NO RESULT")
        flag2+=1



    elif value==2 and choice=="scissor":
        print("\n\n\t\t YOU WON BECAUSE COMPUTER CHOOSE PAPER AND YOU CHOOSE SCISSOR ")
        flag+=1

    elif value==2 and choice=="rock":
        print("\n\n\t\t YOU LOSE BECAUSE COMPUTER CHOOSE PAPER AND YOU CHOOSE ROCK")
        flag3+=1


    elif value==2 and choice=="paper":
        print("\n\n\t\t DRAW! NO RESULT")
        flag2+=1




    elif value==3 and choice=="rock":
        print("\n\n\t\t YOU WON BECAUSE COMPUTER CHOOSE SCISSOR AND YOU CHOOSE ROCK")
        flag+=1

    elif value==3 and choice=="paper":
        print("\n\n\t\t YOU LOSE BECAUSE COMPUTER CHOOSE SCISSOR AND YOU CHOOSE PAPER")
        flag3+=1

    elif value==3 and choice=="scissor":
        print("\n\n\t\t DRAW! NO RESULT")
        flag2+=1



    else:
        print("\n\n\t\t INVALID CHOICE")

if flag==1 and flag2==1 and flag3==1:
    print("\n\n\t\t\t\t\t\t\t\t\t\t     OVERALL DRAW ")

elif flag==2 and flag3==1:
    print("\n\n\t\t\t\t\t\t\t\t\t\t    OVERALL YOU WON ")

elif flag==2 and flag2==1:
    print("\n\n\t\t\t\t\t\t\t\t\t\t    OVERALL YOU WON ")

elif flag==1 and flag3==2:
    print("\n\n\t\t\t\t\t\t\t\t\t\t    OVERALL YOU LOSE ")

elif flag==1 and flag2==2:
    print("\n\n\t\t\t\t\t\t\t\t\t\t    OVERALL YOU WON ")

elif flag==0 and flag3==3:
    print("\n\n\t\t\t\t\t\t\t\t\t\t    OVERALL YOU LOSE ")

elif flag==0 and flag2==3:
    print("\n\n\t\t\t\t\t\t\t\t\t\t    OVERALL YOU DRAW ")

elif flag3==1 and flag2==2:
    print("\n\n\t\t\t\t\t\t\t\t\t\t    OVERALL YOU LOSE ")

elif flag3==2 and flag2==1:
    print("\n\n\t\t\t\t\t\t\t\t\t\t    OVERALL YOU LOSE ")

else:
    print("\n\n\t\t\t\t\t\t\t\t\t\t    OVERALL YOU WON ")


print("\n\n\t\t\t\t\t\t\t\t\t\t **THANKS FOR PLAYING** ")


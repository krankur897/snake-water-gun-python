import random
''' 
1 for Snake
-1 for Water
0 for Gun
'''
computer=random.choice([-1,0,1])
UserChoice=input("Enter the choice:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[UserChoice]

# We have two member, You And Computer
print(f"You Choosen {reverseDict[you]}\nComputer chooses {reverseDict[computer]}")

if(computer==you):
    print("Its a Draw")

# nested if else
else:   
    if(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Lose!")
    else:
        print("Something went wrong!")
    
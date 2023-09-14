import random

Again =1 
p1 = 0
p2 = 0

while Again > 0:
    
    # print("Your Are Player -1 ")
    print("choose your option\n")
    print( " Rock     .... (1)")
    print( " Paper    .... (2)")
    print( " Scissors .... (3)\n")

    playStack = ["Error ","Rock", "Paper" , "Scissors"]

    player1 = int(input("choose your move : "))
    print("You selected .......: " ,playStack[player1])
    stack = [1,2,3]
    player2 = int((random.choice(stack)))
    # print( " P1 : ", player1)
    # print( " P2 : ", player2)

    print("Computer selected ...: ",playStack[player2], "\n")

    if player1 == 1 : #Rock

        if player2 == 2 : #paper
            print("!! You Lost !!") 
            p2+=1 
        elif player2 == 3: # Scissors
            print( "!!  You Win  !!")
            p1+=1 
        else :
            print("!! Draw !!")

    elif player1 == 2 : #Paper

        if player2 == 1 :
            print("!! You Win !!")
            p1+=1 
        elif player2 == 3:
            print( "!! You Lost  !!")
            p2+=1 
        else :
            print("!! Draw !!")

    else : #Scissors

        if player2 == 2 :
            print("!! You lost !!")
            p2+=1 
        elif player2 == 1:
            print( "!!  You Win !!")
            p1+=1 
        else :
            print("!! Draw !!")
    
    print(" \n------Score----!!!")
    print("You...", p1 * 100)
    print("Computer...", p2 * 100)

    print("\n Do You Want to play again")
    Again = int(input("Yes...(1) || NO...(0) : "))





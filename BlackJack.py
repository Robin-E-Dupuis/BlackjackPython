import random


playerScore = 0
CompScore = 0


def playerCards():
  player = random.randint(1,13)
  global playerScore
  if player==1:
    playerScore +=11
    print("Player pulled an Ace!")
    print("Player Score is ", playerScore)
  elif player== 2:
    playerScore +=2
    print("Player pulled a Two!!")
    print("Player Score is ", playerScore)
  elif player==3:
    playerScore +=3
    print("Player pulled a Three!")
    print("Player Score is ", playerScore)
  elif player==4:
    playerScore +=4
    print("Player pulled a Four!")
    print("Player Score is ", playerScore)
  elif player==5:
    playerScore +=5
    print("Player pulled a Five!")
    print("Player Score is ", playerScore)
  elif player==6:
    playerScore +=6
    print("Player pulled a Six!")
    print("Player Score is ", playerScore)
  elif player==7:
    playerScore +=7
    print("Player pulled a Seven!")
    print("Player Score is ", playerScore)
  elif player == 8:
    playerScore +=8
    print("Player pulled an Eight!")
    print("Player Score is ", playerScore)
  elif player==9:
    playerScore +=9
    print("Player pulled a Nine!")
    print("Player Score is ", playerScore)
  elif player==10:
    playerScore +=10
    print("Player pulled a Ten!")
    print("Player Score is ", playerScore)
  elif player==11:
    playerScore +=10
    print("Player pulled a Jack!")
    print("Player Score is ", playerScore)
  elif player==12:
    playerScore +=10
    print("Player pulled a Queen!")
    print("Player Score is ", playerScore)
  elif player==13:
    playerScore +=10
    print("Player pulled a King!")
    print("Player Score is ", playerScore)


def computerCards():
    computer = random.randint(1, 13)
    global CompScore
    if computer == 1:
        CompScore +=11
        print("Computer pulled an Ace!")
        print("Computer Score is ", CompScore)
    elif computer == 2:
        CompScore +=2
        print("Computer pulled a Two!!")
        print("Computer Score is ", CompScore)
    elif computer == 3:
        CompScore +=3
        print("Computer pulled a Three!")
        print("Computer Score is ", CompScore)
    elif computer == 4:
        CompScore +=4
        print("Computer pulled a Four!")
        print("Computer Score is ", CompScore)
    elif computer == 5:
        CompScore +=5
        print("Computer pulled a Five!")
        print("Computer Score is ", CompScore)
    elif computer == 6:
        CompScore +=6
        print("Computer pulled a Six!")
        print("Computer Score is ", CompScore)
    elif computer == 7:
        CompScore +=7
        print("Computer pulled a Seven!")
        print("Computer Score is ", CompScore)
    elif computer == 8:
        CompScore +=8
        print("Computer pulled an Eight!")
        print("Computer Score is ", CompScore)
    elif computer == 9:
        CompScore +=9
        print("Computer pulled a Nine!")
        print("Computer Score is ", CompScore)
    elif computer == 10:
        CompScore +=10
        print("Computer pulled a Ten!")
        print("Computer Score is ", CompScore)
    elif computer == 11:
        CompScore +=10
        print("Computer pulled a Jack!")
        print("Computer Score is ", CompScore)
    elif computer == 12:
        CompScore +=10
        print("Computer pulled a Queen!")
        print("Computer Score is ", CompScore)
    elif computer == 13:
        CompScore +=10
        print("Computer pulled a King!")
        print("Computer Score is ", CompScore)

def winner():
    global playerScore, CompScore
    if CompScore<=21 and CompScore>playerScore:
        print("The Computer Wins this BlackJack!")
    elif CompScore>21 and CompScore>playerScore:
        print("The Computer Lost and the Player Wins this BlackJack!")
    elif playerScore<=21 and playerScore>CompScore:
        print("The Player Wins this BlackJack!")
    elif playerScore>21 and playerScore>CompScore:
        print("The Player Lost and the Computer Wins this Blackjack!")
    elif playerScore==CompScore:
        print("Draw! No one Wins this BlackJack!")
    else :
        print("Both the Computer and the Player Lose this BlackJack!")



choice = input("Enter Hit or Stay :").lower()

while True:
    if choice == "hit" or choice == "h":
        playerCards()
        if playerScore > 21:
            print("Player Busted!")
            winner()
            break
        choice = input("Enter Hit or Stay :").lower()
    elif choice == "stay" or choice == "s":
        print("Your current score is ",playerScore)
        while CompScore < 21:
           computerCards()
        winner()
        break
    else:
        print("Invalid input. Please enter 'Hit' or 'Stay'.")
        choice = input("Enter Hit or Stay :").lower()

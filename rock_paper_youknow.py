import random 

user_wins = 0 
computer_wins = 0 

options= ["rock", "paper", "scissors"]


while True : 
    user_input = input("type ROCK/PAPER/SCISSORS or Q to quit: ").lower()
    if user_input == "q":
        break
        
        #user input ei list e ache naki check kora hocche
    if user_input not in options:
        print("input not correct, try again! ")
        continue 
    
    random_number = random.randint(0,2)
    # rock: 0 , paper: 1 , scissors: 2
    computer_guess = options[random_number]
    print("computer guessed", computer_guess + ".")
    
         
    if user_input =="rock" and computer_guess =="rock":
        print("its a draw, do again")
        continue 
    elif user_input =="paper" and computer_guess =="paper":
        print("its a draw, do again")
        continue 
    elif user_input =="scissors" and computer_guess =="scissors":
        print("its a draw, do again")
        continue 
    elif user_input =="rock" and computer_guess == "scissors":
        print("you won!")
        user_wins += 1
        
    elif user_input =="paper" and computer_guess == "rock":
        print("you won!")
        user_wins += 1
    
    elif user_input =="scissors" and computer_guess == "paper":
        print("you won!")
        user_wins += 1
        
    else: 
        print("you lost")
        computer_wins += 1
        
print("you won", user_wins, "times")
print("computer won", user_wins, "times")
print("goodbye!")
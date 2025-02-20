import random 

# a = random.randrange(-1,10) #does not include 10
# b = random.randint(-1,10) # does include 10 
# print(a)
# print(b)

top_of_range = input("type a number: ") #inputs as str

if top_of_range.isdigit(): # checks if the input is digit/number 
    
    top_of_range = int(top_of_range) #converts it to int
    
    if top_of_range <=0:
        print("please enter bigger number than 0 next time")
        quit()
        
else: 
    print("please enter a number next time ")
    quit()

random_number = random.randint(0,top_of_range)
guess = 0 

while True: 
    guess+=1
    user_guess = input("make a guess: ")
    if user_guess.isdigit(): # checks if the input is digit/number 
    
        user_guess = int(user_guess) #converts it to int
        
    else: 
        print("please enter a number next time ")
        continue  
    
    
    if user_guess == random_number: 
        print("good job")
        break
     
    elif user_guess > random_number:
        print("you are above the number")
        
    else: 
        print("you are below the number")
print(guess , " guesses")
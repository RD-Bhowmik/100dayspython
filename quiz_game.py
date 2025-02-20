print("Welcome to the Quiz Game!") 

playing = input("Do you want to play? ") 
print(playing)
if playing.lower() != "yes":
    quit()

print("okay! let's play :)")

score = 0 

answer = input("what odes gpu stands for? ")

if answer.lower() == "graphics processing unit":
    print("correct!") 
    score += 1 
else: 
    print("incorrect!")
    
answer = input("what does ram stands for? ")    
if answer.lower() == "random access memory":
    print("correct!") 
    score += 1 
else: 
    print("incorrect!")
    
answer = input("what does PSU stands for? ")    
if answer.lower() == "power supply":
    print("correct!") 
    score += 1 
else: 
    print("incorrect!")
    
print("you got " + str(score) + " questions correct !")
print("you got " + str((score/4)*100) + " % ")







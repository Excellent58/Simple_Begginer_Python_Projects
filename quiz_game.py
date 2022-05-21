print("welcome to quiz game!!!")

play = input("Do you want to play: ").lower()

if play != "yes":
    quit()

print("okay let's play :)")
score = 0

answer = input("what does cpu stand for: ").lower()
if answer == "central processing unit": 
    print("right")
    score += 1
else:
    print("wrong")
    
answer = input("what does GPU stand for: ").lower()
if answer == "graphics processing unit": 
    print("right")
    score += 1
else:
    print("wrong")

answer = input("what does RAM stand for: ").lower()
if answer == "random access memory": 
    print("right")
    score += 1
else:
    print("wrong")

answer = input("what does PSU stand for: ").lower()
if answer == "power supply unit": 
    print("right")
    score += 1
else:
    print("wrong")   

print("you got {} questions correct".format(score)) 
print("you got {} %.".format(int((score/4)*100)))

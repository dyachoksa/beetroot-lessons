import random
number = random.randint(1,9)
attempt = 0

while True:
    res = input("Please, guese the number")
    if res.lower() == "exit":
        break
    else:
        gues_Number = int(res)
    attempt +=1
    if gues_Number==number:
        print("You are right!")
        break;
    elif gues_Number<number:
        print("too low :(")
    elif gues_Number>number:
        print("too high :(")
        
if res.lower() != "exit":
    print(f"You’ve gessed after {attempt} attempt")

import random
a = random.randint(0,10)

while(a):
    b = input("Guess the number : ")
    b = int(b)
    if b == a:
        print("Correct!")
        break
    if b !=a:
        print("Wrong, try again!")



        

    
            

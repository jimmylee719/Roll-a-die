import random as r

while True:
    inkey = input("Press any key and then press[ENTER]Roll-a-die,Press [ENTER] directly to end:")
    if len(inkey)>0:
        num = r.randint(1,6)
        print("The number of dice you throw is"+str(num))
    else:
        print("GameOver!")
        break
        

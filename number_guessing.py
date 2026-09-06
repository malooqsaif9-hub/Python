import random
num = random.randint(1,100)
tries = 0
while True:
    guessed = int(input("please give me your number between 1 - 100\n"))
    tries+=1
    if guessed == num:
        print(f"Congratulations you guessed correct number in {tries} \n")
    elif guessed > num :
        print("sorry you have to go for a lower number ")
    elif guessed<num:
        print("sorry you have to go for a little higher ")


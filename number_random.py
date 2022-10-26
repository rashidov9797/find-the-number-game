import random

random_number = random.randint(1, 100)
#randint - select intger number

game_count = 1

while True:
    # try - error chiqmaganda shu qismi ishlaydi
    try:
        number = int(input("Enter a number between 1 and 100 --->>> "))
        if number > random_number:
            print("Enter a smaller number --->>>")
        elif number < random_number:
            print("Enter a larger number --->>>")
        elif number == random_number:
            print(f"Congratulations. You have won in {game_count} tries")
            break
        count = game_count + 1
    # troubleshooting
    except:
        print("Please enter a number only!")



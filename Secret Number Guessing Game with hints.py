#The Secret Number Guessing Game with Hints (Comparing Numbers)
secret_number =int(input('Set your secret number: '))
i=0
for i in range(3):
    a=int(input('Enter the secret Number: '))
    if secret_number==a:
        print('You win! 🎉')
        break
    elif a>secret_number:
        print("Too high! Try again.")
    elif a<secret_number:
        print("Too low! Try again.")
    i+=1
if a!=secret_number:
    print("Game Over! The number was: .",secret_number)

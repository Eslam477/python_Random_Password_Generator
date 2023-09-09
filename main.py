import random
from os import system,name

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '!', '@', '<', '>', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}']



system('cls' if name == 'nt' else 'clear')

print('Welcome to Random Password Generator, the work of Eslam Mohamed Elnemery 🚀🚀🚀')


waiting_correct_answer = True
is_wrong_answer = False
while waiting_correct_answer:

    if is_wrong_answer:
        system('cls' if name == 'nt' else 'clear')
        print('An unexpected value was entered 😐😐, please try again')
    x = input('Choose the number of characters that make up the password:')
    if str.isdigit(x):
        waiting_correct_answer = False
    else:
        is_wrong_answer = True
password = ''
for r in range(int(x)):
    password = password + str(random.choice(alphabets))
print('Your password is: '+password)


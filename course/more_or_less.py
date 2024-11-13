from random import randint

secret = randint(0, 100)
user_input = int(input('Veuillez entrer un nombre entre 0 et 100 :'))
attempts = 1

while secret != user_input:
    if secret > user_input:
        print('C\'est plus grand !')
    else:
        print('C\'est plus petit !')
    

secret = 'redbull'

counter = 0

guess = ''

limit = 3

out_of_guess = False

while guess != secret and not out_of_guess:
    if counter < limit:
        guess = input("Enter your guess: ")
        counter += 1
    else:
        out_of_guess = True



def raise_to_power(base,power):
    return base**power

print(raise_to_power(3,4))

from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:
    i += 1
    print(i)
    number = randint(1,10)
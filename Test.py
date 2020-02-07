import random

# a**2 >= 9 and not a>3
# prediction: false

# a+2 ==5 or a-1 !=3
# 'Prediction: True'
x, y = (325, 325)


def age_limit_output(age):
    age_limit = 13
    if age < age_limit:
        print(age, 'is below age limit')
    else:
        print(age, 'is old enough')
    print('minimum age is', age_limit)


age_limit_output(15)


# Seek extra practice or help

def vowel(letter):
    vowels = "AEIOUaeiou"
    if letter in vowels:
        return True
    else:
        print(False)


# vowel(a)


def letter_in_word():
    letter = "howdyallHOWDYALL"
    if letter in letter_in_word:
        return True
    else:
        return False


def intiger(n):
    if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                print('number is a multiple of 6')
            else:
                print('number is even')
        else:
            print('number is odd')
    else:
        print('number is not an integer')


intiger(12)
print('# -------------------------------------------------------------------------------------------------------------')


print('# -------------------------------------------------------------------------------------------------------------')


def infer_once(low, high):
    secret = random.randint(low, high)
    print('I have a number between', low, 'and', high,)
    infer = int(input('Guess: '))
    if infer != secret:
        print('Wrong, my number is ', secret, '.', sep='')
    else:
        print('Right, my number is', infer, end='!\n')


infer_once(4, 5)


print('# -------------------------------------------------------------------------------------------------------------')


def guess():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4 inclusive')
    if guess != secret:
        print('Right on I was number', secret,)
    else:
        if guess > secret:
            print('too high! my number was', secret,)
        else:
            print('too low! my number was', secret,)


guess()


def quiz_decimal(low, high):
    print('type a number between', low, 'and', high,)
    decimal = float(input('Decimal'))
    if decimal > low:
        if decimal < high:
            print('Correct!', decimal, 'is between', low, 'and', high, )
        else:
            print(decimal, 'too high', decimal, 'is greater than', high,)
    else:
        print(decimal, 'too low,', decimal, 'is smaller than', low,)


quiz_decimal(7, 13)

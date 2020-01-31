
 a=3

a**2 >= 9 and not a>3
# prediction: false

a+2 ==5 or a-1 !=3
#'Prediction: True'
x, y = (325,325)

def age_limit_output(age):
    age_limit = 13
    if age <age_limit:
        print(age, 'is below age limit')
    else:
        print(age, 'is old enough')
    print('minimum age is', age_limit)


age_limit_output(15)


 def report_grade(percent):
    if percent >=80:
        print("a grade of %s")

report_grade(79)
#a grade of 79 does not indicate mastery
#Seek extra practice or help

def vowel(letter):
    vowels="AEIOUaeiou"
    if letter in vowels:
        return True
    else:
        print(False)


vowel(a)



def letter_in_word(letter):
  letter_in_word="howdyallHOWDYALL"
  if  letter in letter_in_word:
    return True
  else:
      return False

letter_in_word(R)

def intiger(n):
    if int(n)==n:
        if n % 2 == 0:
            if n % 3 ==0:
                print('number is a multiple of 6' )
            else:
                print('number is even')
        else:
            print( 'number is odd')
    else:
        print('number is not an integer')


intiger(12)



import random
def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        print('Wrong, my number is ', secret, '.', sep='')
    else:
        print('Right, my number is', guess, end='!\n')





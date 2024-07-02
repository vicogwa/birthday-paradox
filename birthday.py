import datetime
import random

def getBirthday (numOfBirthday):
    # return a list of random date number for birthday
    birthdays = []

    for i in range(numOfBirthday):
        startYear = datetime.date(1998, 1, 1)
        numDay = datetime.timedelta(random.randint(0, 354)) 
        birthday = startYear + numDay
        birthdays.append(birthday)
    return birthdays


    # return list of object date that occurs more than one
def getMatch(birthdays):
    # set is use to get the unique object date, if all obj are unique, return none
    if len(birthdays) == len(set(birthdays)):
        return None


        # comparing the birthday and return the matching birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA 

# display the intro:

print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
(It's not actually a paradox, it's just a surprising result.)
 ''')

 # Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

#  keep asking until user enter a valid amount
while True:
        print("how many number shall i generate? (max 100)")
        response = input("enter num: ")
        if response.isdecimal()and (0 < int(response) <= 100):
            numBDay = int(response)
            break
        print()

# generate and display the birthday
print("here are", numBDay, "birthday")
print()
birthdays = getBirthday(numBDay)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print( "" , end = '')

        monthName = MONTHS[birthday.month]
        dateText = (f"{monthName} , {birthday.day}")
        print(dateText , end = ':')
print()
print()

  
# check if two birthday matches
match = getMatch(birthdays)
#   display the result 
     
print("In this simulation, " , end = '')
if match != None:
    monthName = MONTHS[match.month -1]
    dateText = (f"{monthName}, {match.day} ")
    print(f"multiple people have a birthday on {dateText}")
else:
    print("there are no matching birthdays. ")
print()        
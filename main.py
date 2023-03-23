import time
import random
import datetime
from datetime import datetime
from datetime import date

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

year = date.today().year
def str_time_prop(start, end, time_format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)

def getWeekday(date):
    dateObj = datetime.strptime(date,'%d/%m/%Y')
    n = dateObj.weekday()
    n = int(n)+1
    if n == 7:
        n = 0

    return n

def startCountdown():
    print('\nstarting in:')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('Begin!')

def checkAnswer(a, b):
    if int(a) == int(b):
        print(bcolors.OKGREEN + "Correct!" + bcolors.ENDC)
    else:
        print(bcolors.WARNING + "Wrong! the answer was " + str(b) + bcolors.ENDC)

print(random_date("1/1/2008", "1/1/2009", random.random()))


print('Starting DoomsdayTest')
print('\nthis is a game for guessing the weekday of dates')
print('You write down the weekday as a number between 0 and 6')
print('where 0 is a sunday and 6 is saturday')

print('\n\nWhat difficulty do you want:')

print('\n1. Easy')
print('All the dates are only from this year')

print('\n2. Medium')
print('Dates are only from 2000 to 2099')

print('\n3. Hard')
print('Dates are from 1800 to 2199')

print('\n4. Extreme')
print('Haven\'t decided yet')

print('\n\nwrite the number of the difficulty you want:')
mode = input()

cont = 1

if mode == '1':
    print('\n\nEasymode selected')
    while bool(cont):    
        print('\ngenerating 5 dates')
        date1 = random_date("1/1/" + str(year), "31/12/"+ str(year), random.random())
        week1 = getWeekday(date1)
        date2 = random_date("1/1/" + str(year), "31/12/"+ str(year), random.random())
        week2 = getWeekday(date2)
        date3 = random_date("1/1/" + str(year), "31/12/"+ str(year), random.random())
        week3 = getWeekday(date3)
        date4 = random_date("1/1/" + str(year), "31/12/"+ str(year), random.random())
        week4 = getWeekday(date4)
        date5 = random_date("1/1/" + str(year), "31/12/"+ str(year), random.random())
        week5 = getWeekday(date5)
        print('The days are done, the countdown will start!\n')
        startCountdown()
        startTime = time.time()
        print("\n\n" + date1)
        print('write the day as a number:')
        answer1 = input()
        checkAnswer(answer1, week1)

        print("\n\n" + date2)
        print('write the day as a number:')
        answer2 = input()
        checkAnswer(answer2, week2)
    
        print("\n\n" + date3)
        print('write the day as a number:')
        answer3 = input()
        checkAnswer(answer3, week3)

        print("\n\n" + date4)
        print('write the day as a number:')
        answer4 = input()
        checkAnswer(answer4, week4)

        print("\n\n" + date5)
        print('write the day as a number:')
        answer5 = input()
        checkAnswer(answer5, week5)

        endTime = time.time()
        timer = endTime-startTime
        limit = 500
        score = limit-int(timer)
        if int(answer1) == int(week1):
            score = score*1.5
        if int(answer2) == int(week2):
            score = score*1.5
        if int(answer3) == int(week3):
            score = score*1.5
        if int(answer4) == int(week4):
            score = score*1.5
        if int(answer5) == int(week5):
            score = score*1.5
        if timer > limit:
            score = 0

        print('\n\nDone!!')
        print('your time is: ' + str(timer))
        print('Your score is: ' + str(score))
        print('\nDo you want to continue? y/n')
        i = input()
        if i == 'n':
            cont = 0
if mode == '2':
    print('Medium mode selected!')
    while bool(cont):
        
        print('\ngenerating 10 dates')
        date1 = random_date("1/1/" + '2000', "31/12/"+ '2099', random.random())
        week1 = getWeekday(date1)
        date2 = random_date("1/1/" + '2000', "31/12/"+ '2099', random.random())
        week2 = getWeekday(date2)
        date3 = random_date("1/1/" + '2000', "31/12/"+ '2099', random.random())
        week3 = getWeekday(date3)
        date4 = random_date("1/1/" + '2000', "31/12/"+ '2099', random.random())
        week4 = getWeekday(date4)
        date5 = random_date("1/1/" + '2000', "31/12/"+ '2099', random.random())
        week5 = getWeekday(date5)
        date6 = random_date("1/1/" + '2000', "31/12/"+ '2099', random.random())
        week6 = getWeekday(date6)
        date7 = random_date("1/1/" + '2000', "31/12/"+ '2099', random.random())
        week7 = getWeekday(date7)
        date8 = random_date("1/1/" + '2000', "31/12/"+ '2099', random.random())
        week8 = getWeekday(date8)
        date9 = random_date("1/1/" + '2000', "31/12/"+ '2099', random.random())
        week9 = getWeekday(date9)
        date10 = random_date("1/1/" + '2000', "31/12/"+ '2099', random.random())
        week10 = getWeekday(date10)
        
        print('The days are done, the countdown will start!\n')
        startCountdown()
        startTime = time.time()
        print("\n\n" + date1)
        print('write the day as a number:')
        answer1 = input()
        checkAnswer(answer1, week1)

        print("\n\n" + date2)
        print('write the day as a number:')
        answer2 = input()
        checkAnswer(answer2, week2)
    
        print("\n\n" + date3)
        print('write the day as a number:')
        answer3 = input()
        checkAnswer(answer3, week3)

        print("\n\n" + date4)
        print('write the day as a number:')
        answer4 = input()
        checkAnswer(answer4, week4)

        print("\n\n" + date5)
        print('write the day as a number:')
        answer5 = input()
        checkAnswer(answer5, week5)

        print("\n\n" + date6)
        print('write the day as a number:')
        answer6 = input()
        checkAnswer(answer6, week6)

        print("\n\n" + date7)
        print('write the day as a number:')
        answer7 = input()
        checkAnswer(answer7, week7)

        print("\n\n" + date8)
        print('write the day as a number:')
        answer8 = input()
        checkAnswer(answer8, week8)

        print("\n\n" + date9)
        print('write the day as a number:')
        answer9 = input()
        checkAnswer(answer9, week9)

        print("\n\n" + date10)
        print('write the day as a number:')
        answer10 = input()
        checkAnswer(answer10, week10)
        endTime = time.time()

        timer = endTime-startTime
        limit = 1000
        score = limit-int(timer)
        if int(answer1) == int(week1):
            score = score*1.5
        if int(answer2) == int(week2):
            score = score*1.5
        if int(answer3) == int(week3):
            score = score*1.5
        if int(answer4) == int(week4):
            score = score*1.5
        if int(answer5) == int(week5):
            score = score*1.5
        if int(answer6) == int(week6):
            score = score*1.5
        if int(answer7) == int(week7):
            score = score*1.5
        if int(answer8) == int(week8):
            score = score*1.5
        if int(answer9) == int(week9):
            score = score*1.5
        if int(answer10) == int(week10):
            score = score*1.5
        if timer > limit:
            score = 0

        print('\n\nDone!!')
        print('your time is: ' + str(timer))
        print('Your score is: ' + str(score))
        print('\nDo you want to continue? y/n')
        i = input()
        if i == 'n':
            cont = 0

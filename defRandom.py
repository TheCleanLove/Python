import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Number is 1'
    elif answerNumber == 2:
        return 'Number is 2'
    elif answerNumber == 3:
        return 'Number is 3'
    elif answerNumber == 4:
        return 'Number is 4'
    elif answerNumber == 5:
        return 'Number is 5'
    elif answerNumber == 6:
        return 'Number is 6'
    elif answerNumber == 7:
        return 'Number is 7'
    elif answerNumber == 8:
        return 'Number is 8'
    elif answerNumber == 9:
        return 'Number is 9'

r = random.randint(1,9)
number = getAnswer(r)
print(number)

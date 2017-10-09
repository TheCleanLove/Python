name = ' '
count = 0
while name != 'your name':
    print('Please enter your name.')
    name = input()
    count += 1
    if count >= 10:
        print('Dude, it\'s a joke, you\'re supposed to type \'your name\'')
        break


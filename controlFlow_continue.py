# like a break statement, continue is used inside loops
# when loop reaches continue statement, program execution
# jumps to the start of the loop and reevalutes loop conditions

while True:
    print('What\'s your name?')
    name = input()
    if name != 'Trump':
        continue
    password = ' '
    count = 0
    while password != 'pussy':
        print('Hello POTUS, what\'s the password?')
        password = input()
        continue 
    break
print('Acces granted.')

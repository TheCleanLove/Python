import sys
count = 1
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
    print('Count = ' + str(count) + '.')
    count += 1
    if count == 15:
        print('Last try Brian!!!!!!')
    if count > 15:
        print('Stop wasting your time and go to sleep, Brian.')
        sys.exit()
            

#example of an exit
response = "exit"
import sys
while True:
    print('Type exit to exit.')
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')


from colorama import Fore
import win32api
import time


penis_size = int(input(Fore.WHITE + 'How long is your penis (inches): '))

if penis_size > 32:
    print('Sorry your penis is too long :(')
elif penis_size <= 1:
    print("I am so sorry :'3")
elif penis_size < 3:
    print('Sorry your penis is too small :)')
else:
    print(f'Your penis will be {penis_size} inches long')

penis_color = (input('What color is your penis?:'))

print('\n\n=====PENIS PREVIEW=====\n\n')

color = getattr(Fore, penis_color.upper())
print(color)

print('      _____')
print('     /  |  \\')
print('     \\     /')
for i in range(0, penis_size):
    print(color + '     |     |', end='')
    if i == 0 or i == penis_size - 1:
        print(Fore.WHITE + ' ---+')
    elif i == penis_size // 2:
        print(Fore.WHITE + f'    +--- {penis_size} inches')
    else:
        print(Fore.WHITE + '    |')
print(color, end='')
print('   ____   ____')
print('  /    \\ /    \\  ')
print('  \\____/ \\____/')

last_state = 1
while True:
    if (state := win32api.GetKeyState(1)) != last_state:
        last_state = state
        if state < 0:
            print(f'Left clicked {state}')


from os import system
from colorama import Fore
import win32api
from penis import MeasuredPenis

cum = 0

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


last_state = 1
penis = MeasuredPenis(penis_size)
print(penis)

while True:
    if (state := win32api.GetKeyState(1)) != last_state:
        last_state = state
        if state < 0:
            penis.length += 1
            system('cls')
            print(penis)
            cum = cum + 1

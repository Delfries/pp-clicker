from sys import builtin_module_names
from turtle import pen
from colorama import *

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
if penis_color == "red":
    print(Fore.RED)
elif penis_color == "blue":
    print(Fore.BLUE)
elif penis_color == "green":
    print(Fore.GREEN)
else:
    print(Fore.WHITE + "Too bad, you're getting a white penis")

print('      _____')
print('     /  |  \\')
print('     \\     /')
for i in range(0, penis_size):
    print('     |     |', end='')
    if i == 0 or i == penis_size - 1:
        print(Fore.WHITE + ' ---+')
    elif i == penis_size // 2:
        print(Fore.WHITE + f'    +--- {penis_size} inches')
    else:
        print(Fore.WHITE + '    |')
print('   ____   ____')
print('  /    \\ /    \\  ')
print('  \\____/ \\____/')

penis_size = int(input('How long is your penis (inches): '))

if penis_size > 32:
    print('Sorry your penis is too long :(')
elif penis_size <= 1:
    print("I am so sorry :'3")
elif penis_size < 3:
    print('Sorry your penis is too small :)')
else:
    print(f'Your penis will be {penis_size} long')

print('\n\n=====PENIS PREVIEW=====\n\n')
print('      _____')
print('     /  |  \\')
print('     \\     /')
for i in range(0, penis_size):
    print('     |     |', end='')
    if i == 0 or i == penis_size - 1:
        print(' ---+')
    elif i == penis_size // 2:
        print(f'    +--- {penis_size} inches')
    else:
        print('    |')
print('   ____   ____')
print('  /    \\ /    \\  ')
print('  \\____/ \\____/')
  
penis_size = int(input('How long is your penis (inches): '))

if penis_size > 32:
    print('Sorry your penis is too long :(')
elif penis_size < 3:
    print('Sorry your penis is too small :)')
elif penis_size <= 1:
    print('I am so sorry :()')
else:
    print(f'Your penis will be {penis_size} wide')

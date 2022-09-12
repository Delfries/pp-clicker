print("How many inches long would you like your penis to be?")
penis_size = int(input())

if int(penis_size) > 32:
    print('Sorry your penis is too wide :(')
    exit(0)
else:
    print("Your penis will be " + str(penis_size) + " wide")

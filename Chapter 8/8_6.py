numlist = list()

while True:
    number = input('Enter a number, enter Done when done:')
    if number == 'Done':
        break
    try:
        numbers = float(number)
    except:
        print('Invalid Entry')
        quit()
    numlist.append(numbers)

print('Maximum:', max(numlist))
print('Minimum:', min(numlist))
    

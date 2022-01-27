"""Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average."""

num = 0
minimum = None
maximum = None

while True:
    usernum = input('Enter a number. Enter Done when finished.: ')
    if usernum == 'Done':
        break
    try:
        goodnum = float(usernum)
    except:
        print('Invalid Entry.')
        continue
    if minimum is None:
        minimum = goodnum
    if minimum > goodnum:
        minimum = goodnum
    if maximum is None:
        maximum = goodnum
    if maximum < goodnum:
        maximum = goodnum

print('Smallest number entered was', minimum, '.', 'Largest number entered was', maximum, '.')

"""Exercise 1: Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number."""

#Define the variables to be used in math later
num = 0
total = 0.0

#Start the loop of user number entry
while True:
    usernum = input('Enter a number. Type Done when finished: ')
    if usernum == 'Done':
        break     
    try:
        number = float(usernum) #Ensure the user entered a number and have a value to use for total and average later
    except:
        print("Invalid Entry.")
        continue
    num = num + 1 #Add 1 to the number
    total = total + number
print('Total of numbers is:', total, 'Number of Numbers Entered is:', num, 'Average of the numbers is:', total / num)
 

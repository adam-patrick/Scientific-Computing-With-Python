hours = float(input('Enter Hours Worked:'))
rate = float(input('Enter Pay Rate:'))

if hours <= 40:
    pay = hours *  rate
else:
    pay = ((hours - 40) * (1.5 * rate)) + (40 * rate)
    
print('Your pay is', pay)

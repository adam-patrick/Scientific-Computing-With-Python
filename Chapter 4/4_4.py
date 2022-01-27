try:
        hours = float(input("Enter Hours Worked: "))
except:
        print("Error. Incorrect Format.")
        exit()
try:
        rate = float(input("Enter Pay Rate: "))
except:
        print("Error. Incorrect Format.")
        exit()
def compute_pay(hours, rate):
    if hours <= 40:
        wages = hours * rate
        return wages
    else:
        wages = (((hours - 40) *(1.5 * rate)) + (hours * rate))
        return wages
print(compute_pay(hours, rate))
                    

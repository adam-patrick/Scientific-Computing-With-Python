file = input('Enter a file name:')

try:
    fname = open(file)
except:
    print('Invalid Entry. Quitting...')
    quit()

dicky = dict()
lst = list()

for line in fname:
    line = line.rstrip()
    email = line.split()
    if len(email) < 5 or email[0] != 'From':
        continue
    colon_pos = email[5].find(':')
    hour = email[5][:colon_pos]
    
    if hour not in dicky:
        dicky[hour] = 1
    else:
        dicky[hour] += 1

for key, value in list(dicky.items()):
    lst.append((key, value))

lst.sort()
for key, value in lst:
    print(key, value)

       

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
    if len(email) < 2 or email[0] != 'From':
        continue
    else:
        if email[1] not in dicky:
            dicky[email[1]] = 1
        else:
            dicky[email[1]] += 1

for key, value in list(dicky.items()):
    lst.append((value, key))

lst.sort(reverse=True)
for key, value in lst[:1]:
    print(value,key)

       

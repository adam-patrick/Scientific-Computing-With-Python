file = input('Enter a file name:')

try:
    fname = open(file)
except:
    print('Invalid Entry. Quitting...')
    quit()

dicky = dict()

for line in fname:
    line = line.rstrip()
    sentence = line.split()
    if len(sentence) < 3 or sentence[0] != 'From':
        continue
    else:
        pos = sentence[1].find('@')
        domain = sentence[1][pos+1:]
        if domain not in dicky:
            dicky[domain] = 1
        else:
            dicky[domain] += 1

       
print(dicky)

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
        if sentence[1] not in dicky:
            dicky[sentence[1]] = 1
        else:
            dicky[sentence[1]] += 1
print(dicky)

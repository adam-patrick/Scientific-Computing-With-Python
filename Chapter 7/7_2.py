file_name = input('Enter a file name:')

try:
    file = open(file_name)
except:
    print('File cannot be opened:', file_name)
    quit()

count = 0
spam = 0

for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        confidence = float(line[21:])
        spam = spam + confidence

average_spam = spam / count
print('Average spam confidence:', average_spam)
        

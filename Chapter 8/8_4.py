ogfile = input('Enter file romeo.txt:')

try:
    file = open(ogfile)
except:
    print('Wrong answer, asshole!')
    quit()
    
mylist = list()

for line in file:
    line = line.split(' ')
    for word in line:
        word = word.strip()
        if word not in mylist:
            mylist.append(word)
mylist.sort()
print(mylist)
    
    
        
            
    
    


    

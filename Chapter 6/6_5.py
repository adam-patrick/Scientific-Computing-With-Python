"""Exercise 5: Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number."""

str = 'X-DSPAM-Confidence:0.8475'
print('The String is',str) #first say what the original string is
colonpos = str.find(':')
print('Its numerical position is',colonpos)#tell what position it is in
info = str[colonpos + 1:]
print('The extracted string is now',info)#show what you extracted
data = float(info)
print('The info you looked for is:',data)#show what it is after converting to float

Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print ("You can print shit within IDLE's interface. Cool, eh there guy?")
You can print shit within IDLE's interface. Cool, eh there guy?
if 43 > 42:
    Print "Shit Yeah, Mother Fucker!!!"
    
SyntaxError: invalid syntax
if 43 > 42:
    Print ("Shit Yeah, Mother Fucker!!!")

    
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    Print ("Shit Yeah, Mother Fucker!!!")
NameError: name 'Print' is not defined. Did you mean: 'print'?
if 43 > 42:
    print("Shit Yeah, Mother Fucker!!!")

    
Shit Yeah, Mother Fucker!!!

movies= ("Holy Grail", "Life of Brian", "Meaning of Life")
print(movies[1])
Life of Brian
Life of Brian
SyntaxError: invalid syntax

cast = ["Cleese", 'Palin', 'Jones', "Idle]
        
SyntaxError: unterminated string literal (detected at line 1)
cast = ["Cleese", 'Palin', 'Jones', "Idle"]
        
print(cast)
        
['Cleese', 'Palin', 'Jones', 'Idle']
print(len(cast))
        
4
print(cast[1])
        
Palin
cast.append("Gilliam")
        
print(cast)
        
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.pop()
        
'Gilliam'
print(cast)
        
['Cleese', 'Palin', 'Jones', 'Idle']
cast.extend(["Gilliam", "Chapman"])
        
print(cast)
        
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']
        
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']
cast.remove("Chapman")
        
print(cast)
        
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.insert(0,"Chapman")
        
print(cast)
        
['Chapman', 'Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.insert(1,"1975")
        
cast.insert(3,"1979")
        
cast.insert(5,"1983")
        
print(cast)
        
['Chapman', '1975', 'Cleese', '1979', 'Palin', '1983', 'Jones', 'Idle', 'Gilliam']
cast.remove("1975", "1979", "1983")
        
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    cast.remove("1975", "1979", "1983")
TypeError: list.remove() takes exactly one argument (3 given)
cast.remove("1975)
            
SyntaxError: unterminated string literal (detected at line 1)
cast.remove("1975")
            
cast.remove("1979")
            
cast.remove("1983")
            
movies.insert(1, "1975")
            
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    movies.insert(1, "1975")
AttributeError: 'tuple' object has no attribute 'insert'
print(movies)
            
('Holy Grail', 'Life of Brian', 'Meaning of Life')
movies.insert(1,"1975")
            
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    movies.insert(1,"1975")
AttributeError: 'tuple' object has no attribute 'insert'
movies=["Holy Grail", 1975,
        "The Life of Brian", 1979,
        "The Meaning of Life", 1983]
            
print(movies)
            
['Holy Grail', 1975, 'The Life of Brian', 1979, 'The Meaning of Life', 1983]

for each_item in movies:
            if instance(each_item, list):
                for nested_item in each_item:
                    print(nested_item)
            else:
                print(each_item)
                
SyntaxError: invalid syntax. Perhaps you forgot a comma?
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print ("You can print shit within IDLE's interface. Cool, eh there guy?")
You can print shit within IDLE's interface. Cool, eh there guy?
if 43 > 42:
    Print "Shit Yeah, Mother Fucker!!!"
    
SyntaxError: invalid syntax
if 43 > 42:
    Print ("Shit Yeah, Mother Fucker!!!")

    
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    Print ("Shit Yeah, Mother Fucker!!!")
NameError: name 'Print' is not defined. Did you mean: 'print'?
if 43 > 42:
    print("Shit Yeah, Mother Fucker!!!")

    
Shit Yeah, Mother Fucker!!!

movies= ("Holy Grail", "Life of Brian", "Meaning of Life")
print(movies[1])
Life of Brian
Life of Brian
SyntaxError: invalid syntax

cast = ["Cleese", 'Palin', 'Jones', "Idle]
        
SyntaxError: unterminated string literal (detected at line 1)
cast = ["Cleese", 'Palin', 'Jones', "Idle"]
        
print(cast)
        
['Cleese', 'Palin', 'Jones', 'Idle']
print(len(cast))
        
4
print(cast[1])
        
Palin
cast.append("Gilliam")
        
print(cast)
        
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.pop()
        
'Gilliam'
print(cast)
        
['Cleese', 'Palin', 'Jones', 'Idle']
cast.extend(["Gilliam", "Chapman"])
        
print(cast)
        
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']
        
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']
cast.remove("Chapman")
        
print(cast)
        
['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.insert(0,"Chapman")
        
print(cast)
        
['Chapman', 'Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
cast.insert(1,"1975")
        
cast.insert(3,"1979")
        
cast.insert(5,"1983")
        
print(cast)
        
['Chapman', '1975', 'Cleese', '1979', 'Palin', '1983', 'Jones', 'Idle', 'Gilliam']
cast.remove("1975", "1979", "1983")
        
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    cast.remove("1975", "1979", "1983")
TypeError: list.remove() takes exactly one argument (3 given)
cast.remove("1975)
            
SyntaxError: unterminated string literal (detected at line 1)
cast.remove("1975")
            
cast.remove("1979")
            
cast.remove("1983")
            
movies.insert(1, "1975")
            
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    movies.insert(1, "1975")
AttributeError: 'tuple' object has no attribute 'insert'
print(movies)
            
('Holy Grail', 'Life of Brian', 'Meaning of Life')
movies.insert(1,"1975")
            
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    movies.insert(1,"1975")
AttributeError: 'tuple' object has no attribute 'insert'
movies=["Holy Grail", 1975,
        "The Life of Brian", 1979,
        "The Meaning of Life", 1983]
            
print(movies)
            
['Holy Grail', 1975, 'The Life of Brian', 1979, 'The Meaning of Life', 1983]

for each_item in movies:
            if isinstance(each_item, list):
                for nested_item in each_item:
                    print(nested_item)
            else:
                print(each_item)
                
SyntaxError: invalid syntax. Perhaps you forgot a comma?
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)

            
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    for each_item in movies:
NameError: name 'movies' is not defined
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
            else:
                
SyntaxError: invalid syntax
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
        else:
            print(each_item)

            
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for each_item in movies:
NameError: name 'movies' is not defined
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies)
['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
        else:
            print(each_item)

Graham Chapman
['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
            print(each_item)

            
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Graham Chapman
['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            for deeper_item in nested_items:
                print(deeper_item)
    else:
            print(each_item)

            
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Traceback (most recent call last):
  File "<pyshell#19>", line 4, in <module>
    for deeper_item in nested_items:
NameError: name 'nested_items' is not defined. Did you mean: 'nested_item'?
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_items:
                    print(deeper_item)
    else:
            print(each_item)

            
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Traceback (most recent call last):
  File "<pyshell#21>", line 5, in <module>
    for deeper_item in nested_items:
NameError: name 'nested_items' is not defined. Did you mean: 'nested_item'?
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_items:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)

        
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Graham Chapman
Traceback (most recent call last):
  File "<pyshell#25>", line 5, in <module>
    for deeper_item in nested_items:
NameError: name 'nested_items' is not defined. Did you mean: 'nested_item'?
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)

        
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Graham Chapman
Michael Palin
John Cleese
Terry Gilliam
Eric Idle
Terry Jones


def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

            
print_lol(movies)
The Holy Grail
1975
Terry Jones & Terry Gilliam
91
Graham Chapman
Michael Palin
John Cleese
Terry Gilliam
Eric Idle
Terry Jones

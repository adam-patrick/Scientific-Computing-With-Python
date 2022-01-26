Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
names = ['Michael', 'Terry']
isinstance(names, list)
True
num_names = lens(names)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    num_names = lens(names)
NameError: name 'lens' is not defined. Did you mean: 'len'?
num_names = len(names)
isinstance(num_names, list)
False

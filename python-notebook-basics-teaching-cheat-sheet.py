#Python Notebook¶
#In this notebook, I will be demonstrating python code segments that you can use as a cheat sheet for your studies

#Python Basics - Creating and Printing Basic Variable Sets
#In this section, I will demonstrate a short section of how to use basic numeric variables.
#In computer programming, a variable is a storage location paired with an associated name.

#This section will cover:

#variable assignment
#printing
#operations (addition, subtraction, division, multiplication)
#changing format
#checking type
#overcoming basic errors related to variables

#Integers - Create, Format, Change

x = 7 #we have assigned our first variable
y = 6
z = '3'
xxx = 7.777
yyy = 6.666

print(x, y) #display
print(x + y) #add
print(x / y) #divide
print(x * y) #multiply
print(x ** y) #expontential
print(x // y) #floor division
print(int(xxx)) #turn 7.777 into integer
print(float(y)) #turn integer 6 into float
print(type(x)) #check type
print(type(yyy)) #check type

#Lesson 1.1 - COMMON ERRORS AND HOW TO FIX THEM
#print(x + q) #NameError: name 'q' is not defined - Check if you have defined this variable earlier as something else
#print(x + z) #TypeError: unsupported operand type(s) for +: 'int' and 'str'' - Change both to a consistent type
#print(x + y #SyntaxError: unexpected EOF while parsing - You might be missing part of your code to complete the action
#print[x + y] #TypeError: 'builtin_function_or_method' object is not subscriptable - Not a container such as lists, tuples, and dictionaries

#SOLVED PROBLEMS TO LESSON 1.1
print(x + y) #NameError: name 'q' is not defined - Check if you have defined this variable earlier as something else
print(x + int(z)) #TypeError: unsupported operand type(s) for +: 'int' and 'str'' - Change both to the same type
print(x + y) #SyntaxError: unexpected EOF while parsing - You might be missing part of your code to complete the action
print(x + y) #TypeError: 'builtin_function_or_method' object is not subscriptable - Not a container such as lists, tuples, and dictionaries

#PYTHON CHALLENGE: BASIC CALCULATOR

def calcadd(x, y):
    calcadd = x + y
    print(calcadd)

def calcsub(x, y):
    calcsub = x - y
    print(calcsub)

def calcmulti(x, y):
    calcmulti = x * y
    print(calcmulti)

def calcdivide(x, y):
    calcdivide = x / y
    print(calcdivide)

calcadd(7, 2)
calcsub(100, 10)
calcmulti(5, 3)
calcdivide(10, 2)

#Strings - Create, Format, Change
#In this section, I will demonstrate a short section of how to use strings.

#This section will cover:

#basic string commands such as printing strings
#slicing
#indexing, length of strings
#replace, splitting
#changing case formatting
#stripping blank space

str1 = 'python code'
str2 = 'is easy to use'

print(str1)
print(str1 * 2) #multiply string occurance
print(len(str1)) #length of strin
print(str1[2]) #forward count
print(str1[-2]) #backward count
print(str1[0:6]) #display part of a string
print(str1 + str2) #concatenate strings
print(str1 +' '+ str2) #add a space
print(str1, str2 + ' after some practice') #add variables and string

str3 = 'clearing space   '
str4 = 'LOW CASE'
str5 = 'high case'
str6 = 'list:seperated:at:colon'

print(str1.split()) #split up the string by finding a seperator
print(str1 + ' ' + str2.replace("easy", "hard")) #replace the word easy with hard
print(str3.strip()) #clear space at end of string
print(str3.swapcase()) #converts the other case level
print(str4.lower()) #change to lower
print(str5.upper()) #change to upper
print(str6.title()) #changes first character of each word to an upper characte
print(str6.split(":")) #split using a specific character

#Lesson 1.2 - COMMON ERRORS AND HOW TO FIX THEM
#print(str1(2)) #TypeError: 'str' object is not callable - Functions are callable, strings are not
#print(st1) #NameError: name 'st1' is not defined - Check the variable name is correct and that you have run the piece of code that defined this variable
#print(st1[10]) #IndexError: string index out of range - Adjust index number based on string length to avoid out of range
#print(str1.strip) #<built-in method strip of str object at 0x0000020EB66F8970> - Check parentheses and run as a function - Stored as a method instead of running as a function

#SOLVED PROBLEMS TO LESSON 1.2
print(str1[2]) #TypeError: 'str' object is not callable - Functions are callable, strings are not
print(str1[10]) #IndexError: string index out of range - Adjust index number based on string length to avoid out of range
print(str1) #NameError: name 'st1' is not defined - Check the variable name is correct and that you have run the piece of code that defined this variable
print(str1.strip()) #<built-in method strip of str object at 0x0000020EB66F8970> - Check parenthesis and run as function - Stored as a method instead of running as a function

#Boolean
#In this section, I will demonstrate the use of Boolean code segments. A Boolean data type is a data type with only two possible values: True or False.

boolean1 = 7
boolean2 = 9
boolean3 = 7
boolean4 = 21
boolean5 = 'string text'

#= is for variable assignment
#== is for condition checking / comparisons

print(boolean1 == boolean2) #False
print(boolean1 == boolean3) #True
print(boolean5.startswith('s')) #True
print(boolean5.endswith('t')) #True
print(boolean5.endswith('x')) #False
print(boolean1 < boolean2) #True
print(boolean1 > boolean2) #False
print(3 == 3) #True
print(7 != 2) #True
print(10 < 2 * 2) #False

#Lists - Create, Format, Change
#In this section, I will demonstrate how to use lists. The simplest data structure in Python and it is used to store a list of values. Lists are collections of items (strings, integers, or even other lists).
#Each item in the list has an assigned index value.
#Lists are enclosed in [ ]
#Each item in a list is separated by a comma
#Lists are mutable, which means they can be changed.

emptylist = [ ] #an empty list is created using just square brackets
listone = ['item1', 'item2', 'item3', 'item4', 'item5'] #a string list
listtwo = [1, 2, 3, 4, 5] #a number list
listthree = [1, 'one', 2, 'two'] #a mixed list
listfour = ['orange', 'red', 'blue', 'green']

print(len(emptylist)) #length of a list without items in it
print(len(listone)) #length of a list with items in it
print(listone[0]) #retrieve the first element
print(listone[-1]) #retrieve the last element
print(listtwo)
listtwo.append(6) #add an item to the end of the list
print(listtwo)
#The more you run this code, the more it will add numbers to the lists

print(listthree)
listthree.insert(4, 'Three') #insert an item. first item is the place index, and the second is the list item
print(listthree)
#The more you run this code, the more it will add numbers to the lists

print(listthree)
listthree.remove('two')
print(listthree)
listone.extend(listtwo) #join two lists together
print(listone)
del listthree[3] #delete item from list three in position [3]
print(listthree)
listthree.reverse() #reverse the order of the list
print(listthree)
listtwo.sort() #sort the list
print(listtwo)
print(listfour)
listfour[0] = 'black' #change the first item 'red' to 'black'
print(listfour)

#Lesson 1.3 - COMMON ERRORS AND HOW TO FIX THEM
#listtwo.append(5, 6) #TypeError: append() takes exactly one argument (2 given) - you can only append one item at a time
#listthree.sort() #TypeError: '<' not supported between instances of 'int' and 'str' - you are not able to sort a list with strings inside it

#Tuples
#In this section, I will demonstrate how to use tuples. A tuple is a list that cannot be changed once it has been defined. They are designated by parentheses instead of square brackets.

importantdimensions = (500, 550) #create a tuple
for value in importantdimensions: #print values from a tuple using a for loop
    print(value)

#Lesson 1.4 - COMMON ERRORS AND HOW TO FIX THEM
#importantdimensions[0] = (200) #TypeError: 'tuple' object does not support item assignment. A tuple is a list that cannot be changed once it has been defined.
#importantdimensions.append(750) #AttributeError: 'tuple' object has no attribute 'append' - A tuple is not a list. You cannot use the .append list command on a tuple.

#Dictionaries
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

myfirstdictionary = {"course": "compsci", "unit code": "101"}
print(myfirstdictionary)
print(myfirstdictionary.get('course')) #return the value of the specified key
print(myfirstdictionary.items()) #returns a list containing a tuple for each key value pair
print(myfirstdictionary.keys()) #return a list with keys only
print(myfirstdictionary.values()) #return a list with values only

seconddictionary = myfirstdictionary.copy()
seconddictionary['course'] = 'business'
seconddictionary['unit code'] = '303'
print(myfirstdictionary)
print(seconddictionary)
myfirstdictionary['tutor'] = 'nicole robinson'
print(myfirstdictionary)
#a different way to make a dictionary
thirddictionary = dict(colour='red', texture='soft', cost='$2')
print(thirddictionary)

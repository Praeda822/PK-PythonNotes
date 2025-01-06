import debug_colours
debug_colours.Colours

from decimal import Decimal

# print is basically the console.log of python as it prints my string to the console.
print("This is a simple Python string")

# Since I've installed the Python extension for VSCode, I can run this file by right-clicking and selecting "Run Python File in Terminal" from the context menu.
#
#
# ======================
#       VARIABLES
# ======================

# Variables are my containers for storing data values.
# I can assign a value to a variable using the assignment operator (=).
# I don't need to declare var/let/const like in Javascript.
#
#       Strings
# ======================
#

name = "bro"
print("========== STRINGS ==========")
print(name) # Bro

# I can also typecast my variables to specified data types, just like with C#.
# When I cast a variable to a different data type, I'm NOT mutating the original variable's data type, only the REFERENCE to it (_need to double check this.._).
# I can check the data type of a variable by using the type() function.
# When I'm checking the data type, I can see in my output that it's a string/int/float/whatever class.
print(type(name)) # <class 'str'>

# A (_the?_) common naming convention in Python is to use snake_case for my variable names.

new_first_name = "Bro"
new_last_name = "Sup"
new_full_name = new_first_name + " " + new_last_name
print("Hello, " + new_full_name) # Hello Bro Sup
#
#
#       Integers
# ======================
#
# Generally speaking I can't use strings to do any math operations
# I should instead be using integers (_WHOLE NUMBERS_) or floats (_DECIMAL NUMBERS_).

age = 31
age += 1 # += works the same as JS, mutating the OG variable's value.
# print(type(age)) # 32

# But what if I want to use BOTH a String AND an inbteger in the same print statement?
# I have to CONVERT the age variable to the STRING data type by Typecasting, just like in C#!
# SO, recalling all the shit they jammed into my head at college when I was learning OOP...
# I originally interpreted striung variables using Parse() and TryParse(), respectively
# Where I would only convert a string into an integer ONLY IF the variable being parsed _was_ a string by checking the inverse value of it _NOT_ being a string (_yes, I know, very convulted but it makes sense to me_):

# ```
# if (!int.TryParse(stringVar, out int result)) {
#       Console.WriteLine($"Parsed number: {result}"); 
#   }
#   else {
#       Console.WriteLine("Invalid number format.");
#   }
# ```
#
# In Python, however, I typecast in a slightly syntatically different, but less verbose, way:

print("========== INTEGERS ==========")
print("Your age is: " +str(age)) # Your age is 32
#
#
#       Floats
# ======================
#
# Floats are integers that can hold BOTH **whole** numbers, as well as **decimal** values.
height = 189.0
# Typecast the float to a string SO I can use string concatenation
print("========== FLOATS ==========")
print("Your height is: " +str(height) + "cm")
print(type(height)) # <class 'float'>
#
#
#       Booleans
# ======================
# 
# Booleans are used to represent the truth values of logic and can be either True or False.
# Typically, I've bene using booleans to handle my if logic, and act as a switch to determine whether or not a certain block of code should be executed.
# Important to note, Python is case-sensitive, so I need to make sure I'm using the correct case for my booleans.

human = True
print("========== BOOLEANS ==========")
print("Are you a human: " +str(human))

#
#
#  Multiple Assignments
# ======================
#
# Multiple assignment allows me to assign multiple values to multiple variables in one line of code.

# myname = "Pat"
# myage = 31
# myfuckability = True

# So instead of having to shit out lines & lines of unnecessarily verbose code, I can do it all (_ideally) in one line of code!

myname, myage, myfuckability = "Pat", 31, True
print("========== SINGLE ASSIGNMENTS ==========")
print(myname)
print(myage)
print(myfuckability)

# I can also use multiple assignments to minimise code redundancy:

bikini_bottom = Patrick = Sandy = Spongebob = 30
print("========== MULTIPLE ASSIGNMENTS ==========")
print(bikini_bottom) # 30
#
#
#     String Methods
# ======================
#
# Python has in-built methods for working with strings, just like JS
# For instance, I can check the length of a string:
print("========== .length() METHOD ==========")
print(len(name)) # 3 (Bro)

# And there's a method for finding the index value, .find(), similar to indexOf()
print("========== .find() METHOD ==========")
print(name.find("o")) # 2

# I can also capitalise names with the .capitalize() method
# Beats toUpperCase(), but not using the Queen's English bothers the fuck outta' me..
print("========== .capitalize() METHOD ==========")
print(name.capitalize()) # Bro

# Same again for converting an entire string to uppercase
print("========== .upper() METHOD ==========")
print(name.upper()) # Bro
# Same again for converting an entire string to lowercase
print("========== .lower() METHOD ==========")
print(name.lower()) # bro

# I can also check if a string value is an integer using the isdigit() method:
print("========== .isdigit() METHOD ==========")
print(name.isdigit()) # False

# I can check if my string contains any alphabetical characters
# In this instance, it returns True, but if I had a space, or trailing whitespace, then it would return False
print("========== .isalpha() METHOD ==========")
print(name.isalpha()) # True

# Next I have the .count() method, which will return the exact sum amount of _SPECIFIED_ characters within my string:
print("========== .count() METHOD ==========")
print(name.count("o")) # 1

# And I can also replace characters in my string using the .replace() method
# The first argument is the character I want to replace
# The second argument is the character I want to replace the first character with
# Important to note that this _DOESN'T_ mutate the OG variable value
print("========== .replace() METHOD ==========")
print(name.replace("o","a")) # bra

# Something really cool, with Python is that I can return a string _multiple times_ in _one line of code_!
# I can achieve this by using the multiplication operator (*) as part of the print statement:
print("========== MULTIPLIACTION OPERATOR ==========")
print(name*3) # BroBroBro
#
#
#     Type Casting
# ======================
#
# Type casting is the process of converting the value of one data type (integer, string, float, etc.) to another data type.
x = 1 # int
y = 2.0 # float
z = "3" # str
print("========== TYPE CASTING ==========")
print(x)
# I can typecast my float value into an integer by wrapping my variable with the int() function
# Important to note that this _DOESN'T_ mutate the OG variable value, either!
print(y) # 2.0
print(z)

# If I _do_ want to mutate the OG variable, then I would need to reassign it
# Keeping in mind, that I can _still_ typecast the variable to a different data type:
y = int(y)
print(y) # 2

# Now I can typecast my Z variable as an integer, as well:
z = int(z)
print(z) # 3

# I can also typecast my integer values into floats by wrapping my variables with the float() function:
x = float(x)
print(x) # 1.0

# Important to note here that when performing maths operations on a float and an integer, the result will always be a float.
# This is because the float data type is more precise than the integer data type.
# And when I uuse the multiplication operator with a string, I will get the string repeated the number of times specified by the integer specified.
z = float(z)
print(z*3) # 9.0

# The main situation where I want to really get into Typecasting my variables is when I may want to display an integer with a float and/or a string.
# In this instance, I can use the str() function to convert my integer to a string:
print("X is: " +str(x)) # TypeError: can only concatenate str (not "float") to str
print("Y is: " +str(x)) # Y is: 1.0
#
#
# ======================
#      USER INPUT
# ======================
#
# With Python, I can use the input() function to get user input.
# Like I learned in OOP/OOD: always helpful to let the user know what sort of input I'm expecting from them.
# Since I'm expecting input from a user, I'll want to store that input into a variable
# Kind of dodgy that I have to open another terminal window to be able to fuck with the input...
print("========== USER INPUT ==========")
name = input("Please enter your name: ")
print("Hello, " +name)

# Whenever I'm taking an input, it is **always a STRING data type**
# So what if I want to accept an integer data type, like whe I'm expecting a number input when asking a user their age?
# Then I want to take in that input, of the STRING data type
# And then I _immediately__ cast that string input data type to an integer
# But in order to use string concatenation, I have to convert it _BACK_ to a string
age = int(input("Please enter your age: "))
print("Hello, " +name, ", you are " +str(age), "years old")

# Only issue here is that if I submit a decimal as an input, I end up with an error!
# Well, I need to typecast my input field as the _float_ data type to work around this
height = float(input("Please enter your height in centimetres: "))
print("Hello, " +name, ", you are " +str(age), "years old and " +str(height), "cm tall.")
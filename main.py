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

name = "Bro"
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

print("Your age is: " +str(age)) # Your age is 32
#
#
#       Floats
# ======================
#
# Floats are integers that can hold BOTH **whole** numbers, as well as **decimal** values.
height = 189.0
# Typecast the float to a string SO I can use string concatenation
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
print("Are you a human: " +str(human))
import math #importing the math module for use further in the program
import os

print("Hello World")        # using the print function for the first time
print("Today we will be practicing some fundamentals of Python\n")

print("I will be adding 3 numbers of your choosing")    # using inputs for the first time, also converting an input into an int and not adding strings
num1 = int(input("Please enter number 1: "))
num2 = int(input("Please enter number 2: "))
num3 = int(input("Please enter number 3: "))
sum = num1 + num2 + num3
print("The sum of the 3 numbers is", sum,"\n")

string1 = "Hello "   # something cool about Python is that varibles do not have to be decalred, also their type does not have to be specfied, Python does it for you
string2 = 'World '   # here I am adding strings together
string3 = "My name is Noe Rivera Jr."  # also strings in Python can be in single or double quotes
stringSum = string1 + string2 + string3
print(stringSum,"\n")

a = 10  # I will be using these variables to show if, if else, and if-elif statements  
b = 20
c = 30
if a<b:
    print("The number",a,"is less than",b)
else:
    print("The number",b,"is less than",a)

if a>b:
   print("The number",a, "is greater than",b)
elif b>c:
    print("The number",b, "is greater than",c)
else:
    print("The number",c, "is greater than both the number",a, "and the number",b,"\n")
print("Now I'm going to print all the numbers from 0 to 10 that are even using a for loop") # for loops and while loops in Python
for i in range(2,12,2):
    print(i)
print("Now I'm going to print all the numbers from 0 to 10 that are odd using a while loop")
num = 1
while(num<=10):
    print(num)
    num+=2

input("Press Enter to continue...")
os.system('cls')

def helloWorld():  # creating functions in Python
    print("Hello World")
def Average(num1,num2,num3):
    avg = (num1+num2+num3)/3
    return avg
print("I will be printing hello world using a funtion") #calling the helloWorld function
helloWorld()
print('The average of the numbers you inputted earlier is:', Average(num1,num2,num3),"\n") #calling the Average function and using the numbers that were inputs from the addition above

print("4 to the power of 3 is", int(math.pow(4,3))) # before I can utilize the following funtions, I had to import the math module
print("I will be using math functions for the next 8 lines")
print(math.floor(4.3))
print(math.floor(10.9))
print(math.ceil(4.3))
print(math.ceil(10.9))
print(math.log(10))
print(math.log(10,2))
print(int(math.sqrt(9)))
print(int(math.sqrt(16)),"\n")

print("Now I will demonstrate string functions") # showing the use of string functions
myName = "noe rivera"
print(myName.capitalize())
print(myName.count("e"))
print(myName.find("ri"))
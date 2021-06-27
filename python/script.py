#!/bin/python3

# File used for remainder of python videos

# Variables and Methods
quote = "I have no fear, for fear is the little death that kills me over and over. Without fear, I die but once."
print(quote)

print(quote.upper()) # upper is a method of the string object
print(quote.title())
print(quote.lower())

print(len(quote))

name = "Nick"
age = 22
gpa = 3.6

print(int(age))
print(int(gpa))

print("My name is " + name + " and my age is " +str(age)+ " and my gpa is " +str(gpa))

age = age + 1
print(age)
age += 1
print(age)


print('\n')
## Functions
print("Here are function examples")

def who_am_i():
    name = "nick"
    age = 22
    print("My name is " + name + " and I am " +str(age))

who_am_i()

#parameters
def add_one_hundred(num):
    print(num + 100)

add_one_hundred(200)

#multiple parameters
def add_x_y(x,y):
    print(x + y)

add_x_y(4,9)

def multiply(x,y):
    return x * y

print(multiply(4,6))

def square_root(x):
    print(x ** .5)

square_root(8)

def new_line():
    print('\n')

new_line()
new_line()

# Boolean Expressions
print("Boolean expressions")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

new_line()
new_line()

#Relational operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True
test_not2 = not False

new_line()
new_line()
#Conditional Statements

def drink(money):
    if money >= 2:
        return "Drink dispensed"
    else:
        return "no sir"
print(drink(2))
print(drink(1))

def alcho(age,money):
    if (age >= 21) and (money >= 5):
        return "Drinks on me!"
    elif (age >= 21) and (money < 5):
        return "Get your bills up!"
    elif (age <21) and (money >= 5):
        return "Nice try!"
    else:
        return "who are you?"
print(alcho(21,5))
print(alcho(21,4))
print(alcho(20,4))

new_line()
new_line()

### Lists
movies = ["Bobby Hill", "arrival", "the last temptation of christ","chocolate and cheese"]
print(movies[0])
print(movies[1])
print(movies[-1]) # grabs the last item
print(movies[1:3]) # print item 1 and stop before 3
print(movies[1:]) # print everything starting with item 1
print(movies[:1]) # print everything before item 1

print(len(movies))
movies.append("JAWS")

movies.pop() # deletes the very last item

movies.pop(0) # deletes the 0 item

new_line()
new_line()

# Tuples - like lists but not mutable, cannot be changed!!
grades = ("a","b","c","d","f")
print(grades[1])

new_line()
new_line()

# Looping
# For loops - start to finish of an iterate
vegies = ["cuce", "spinach", "carrot"]
for x in vegies:
    print(x)

# While looks - execute while true
i = 1
while i < 10:
    print(i)
    i+=1
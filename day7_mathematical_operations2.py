#importing numpy library

import numpy as np


#creating two arrays

numbers1 = np.array([25, 40, 55, 70, 85])

numbers2 = np.array([4, 6, 8, 10, 12])

print(numbers1)
print(numbers2)



# // operator (Floor Division)

#definition

#floor division divides the numbers and returns the largest whole number
#that is less than or equal to the actual answer

#it removes the decimal part

#types

#1 array // array

#2 array // scalar(single value)

#uses

#used when only whole numbers are required

#used to calculate

#number of boxes

#number of students in groups

#number of pages

#inventory management

#syntax

#array1 // array2

#array // value

#return type

#numpy.ndarray

floor_result = numbers1 // numbers2

print(floor_result)



#floor division using scalar

result = numbers1 // 5

print(result)



#real world example

#suppose one box can store 12 chocolates

chocolates = np.array([50, 80, 100, 130])

boxes = chocolates // 12

print(boxes)



# % operator (Modulus)

#definition

#modulus returns the remainder after division

#types

#1 array % array

#2 array % scalar

#uses

#used to check

#even and odd numbers

#cyclic operations

#divisibility

#data grouping

#syntax

#array1 % array2

#array % value

#return type

#numpy.ndarray

remainder = numbers1 % numbers2

print(remainder)



#checking even and odd numbers

numbers = np.array([10,15,22,31,48,57])

print(numbers % 2)

#0 means even

#1 means odd



#real world example

#finding students whose roll numbers are even

roll_numbers = np.array([101,102,103,104,105,106])

print(roll_numbers % 2)



# ** operator (Power)

#definition

#raises one number to the power of another number

#types

#1 array ** scalar

#2 array ** array

#uses

#used in

#machine learning

#scientific calculations

#physics formulas

#mathematics

#syntax

#array ** value

#array1 ** array2

#return type

#numpy.ndarray

square = numbers2 ** 2

print(square)



cube = numbers2 ** 3

print(cube)



#real world example

#calculating square of distances

distance = np.array([2,4,6,8])

distance_square = distance ** 2

print(distance_square)



# np.add()

#definition

#np.add() performs element wise addition

#it gives the same result as the + operator

#uses

#preferred while writing numpy functions

#used in scientific computing

#syntax

#np.add(array1,array2)

#return type

#numpy.ndarray

addition = np.add(numbers1, numbers2)

print(addition)



# np.subtract()

#definition

#performs element wise subtraction

#syntax

#np.subtract(array1,array2)

subtraction = np.subtract(numbers1, numbers2)

print(subtraction)



# np.multiply()

#definition

#performs element wise multiplication

#syntax

#np.multiply(array1,array2)

multiplication = np.multiply(numbers1, numbers2)

print(multiplication)



# np.divide()

#definition

#performs element wise division

#always returns floating point values

#syntax

#np.divide(array1,array2)

division = np.divide(numbers1, numbers2)

print(division)



#important interview points

# // removes the decimal part

# % returns the remainder

# ** calculates powers

# np.add() and + produce the same result

# np.subtract() and - produce the same result

# np.multiply() and * produce the same result

# np.divide() and / produce the same result
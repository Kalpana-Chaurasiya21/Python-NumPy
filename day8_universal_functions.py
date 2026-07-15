#importing numpy library

import numpy as np


#creating a numpy array

numbers = np.array([4, 9, 16, 25, 36])

print(numbers)



#Universal Functions (ufuncs)

#definition

#universal functions (ufuncs) are built-in numpy functions

#they perform operations on every element of an array automatically

#without using loops

#they are very fast because they are implemented in C language

#types

#1 mathematical functions

#2 trigonometric functions

#3 comparison functions

#4 statistical functions

#5 logical functions

#uses

#used in

#data analysis

#machine learning

#scientific computing

#image processing

#financial calculations



#np.sqrt()

#definition

#sqrt stands for square root

#it returns the square root of every element in the array

#syntax

#np.sqrt(array)

#return type

#numpy.ndarray

square_root = np.sqrt(numbers)

print(square_root)

#output

#[2. 3. 4. 5. 6.]



#np.square()

#definition

#square() returns the square of every element

#it is equivalent to number ** 2

#syntax

#np.square(array)

#return type

#numpy.ndarray

square = np.square(numbers)

print(square)



#np.power()

#definition

#raises every element to the given power

#syntax

#np.power(array,power)

#return type

#numpy.ndarray

cube = np.power(numbers,3)

print(cube)



#power can also be different for every element

base = np.array([2,3,4])

power = np.array([3,2,4])

result = np.power(base,power)

print(result)

#2³ = 8

#3² = 9

#4⁴ = 256



#np.abs()

#definition

#abs means absolute value

#absolute value removes the negative sign

#positive numbers remain unchanged

#syntax

#np.abs(array)

#return type

#numpy.ndarray

temperature = np.array([-5,-12,18,-20,30])

absolute = np.abs(temperature)

print(absolute)



#real world example

#bank transactions

balance = np.array([-500,-1500,2500,-700])

absolute_balance = np.abs(balance)

print(absolute_balance)



#important interview points

#ufunc means universal function

#ufuncs perform operations element by element

#ufuncs are much faster than python loops

#np.square(x) is the same as x ** 2

#np.sqrt(x) returns square roots

#np.power(x,n) raises values to a given power

#np.abs(x) removes negative signs
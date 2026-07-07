#creating arrays is one of the first things you learn in numpy
#numpy provides many built in functions to create arrays quickly
#these functions save time and make code cleaner

#import numpy library

import numpy as np



#--------------------------------------------------
#np.array()
#--------------------------------------------------

#used to create a numpy array from a python list

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

#output
#[10 20 30 40 50]



#--------------------------------------------------
#np.zeros()
#--------------------------------------------------

#creates an array filled with zeros

zeros = np.zeros(5)

print(zeros)

#output
#[0. 0. 0. 0. 0.]



#creating two dimensional array

zeros_2d = np.zeros((3, 4))

print(zeros_2d)

#output
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]



#--------------------------------------------------
#np.ones()
#--------------------------------------------------

#creates an array filled with ones

ones = np.ones(5)

print(ones)

#output
#[1. 1. 1. 1. 1.]



#two dimensional array

ones_2d = np.ones((2, 3))

print(ones_2d)

#output
#[[1. 1. 1.]
# [1. 1. 1.]]



#--------------------------------------------------
#np.empty()
#--------------------------------------------------

#creates an array without initializing values
#values are random because memory already contains data

empty = np.empty(5)

print(empty)

#output
#random values



#--------------------------------------------------
#np.arange()
#--------------------------------------------------

#similar to python range()
#last value is excluded

numbers = np.arange(1, 10)

print(numbers)

#output
#[1 2 3 4 5 6 7 8 9]



#start stop step

numbers = np.arange(0, 20, 2)

print(numbers)

#output
#[ 0 2 4 6 8 10 12 14 16 18]



#--------------------------------------------------
#np.linspace()
#--------------------------------------------------

#creates evenly spaced numbers
#last value is included

numbers = np.linspace(1, 10, 5)

print(numbers)

#output
#[ 1.    3.25  5.5   7.75 10. ]



#--------------------------------------------------
#difference between arange and linspace
#--------------------------------------------------

#arange uses step value

print(np.arange(1, 11, 2))

#output
#[1 3 5 7 9]



#linspace uses number of values

print(np.linspace(1, 10, 5))

#output
#[ 1.    3.25  5.5   7.75 10. ]



#--------------------------------------------------
#np.eye()
#--------------------------------------------------

#creates an identity matrix

matrix = np.eye(3)

print(matrix)

#output
#[[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]



#--------------------------------------------------
#np.identity()
#--------------------------------------------------

#also creates an identity matrix

matrix = np.identity(4)

print(matrix)

#output
#4x4 identity matrix



#--------------------------------------------------
#np.full()
#--------------------------------------------------

#creates an array filled with one specific value

numbers = np.full(5, 100)

print(numbers)

#output
#[100 100 100 100 100]



#two dimensional array

matrix = np.full((2, 3), 7)

print(matrix)

#output
#[[7 7 7]
# [7 7 7]]



#--------------------------------------------------
#specifying data type
#--------------------------------------------------

numbers = np.array([1, 2, 3], dtype=float)

print(numbers)

print(numbers.dtype)

#output
#float64



#--------------------------------------------------
#real world example
#--------------------------------------------------

#suppose a company has not yet received sales data
#initialize sales of 7 days with zero

weekly_sales = np.zeros(7)

print(weekly_sales)

#output
#[0. 0. 0. 0. 0. 0. 0.]



#suppose every employee gets joining bonus of 5000

bonus = np.full(10, 5000)

print(bonus)

#output
#[5000 5000 5000 ...]
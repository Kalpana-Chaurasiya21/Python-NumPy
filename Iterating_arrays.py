#importing numpy library

import numpy as np


#Iterating NumPy Arrays

#definition

#iterating means visiting each element of an array one by one

#numpy provides multiple ways to iterate through arrays

#depending on whether the array is 1D, 2D or multidimensional

#uses

#printing values

#processing datasets

#applying conditions

#performing calculations



#creating a one dimensional array

numbers = np.array([10,20,30,40,50])

print(numbers)



#iterating through a 1D array

#definition

#a simple for loop accesses one element at a time

#syntax

#for variable in array

print("Iterating 1D Array")

for value in numbers:

    print(value)



#creating a two dimensional array

marks = np.array([[85,90,95],

                  [76,88,92]])

print(marks)



#iterating through a 2D array

#the first loop accesses each row

#the second loop accesses each value inside that row

print("Iterating 2D Array")

for row in marks:

    for value in row:

        print(value)



#creating a three dimensional array

data = np.array([[[1,2],

                  [3,4]],

                 [[5,6],

                  [7,8]]])

print(data)



#iterating through a 3D array

#three loops are required because there are three dimensions

print("Iterating 3D Array")

for matrix in data:

    for row in matrix:

        for value in row:

            print(value)



#np.nditer()

#definition

#nditer stands for n-dimensional iterator

#it automatically visits every element of a numpy array

#without writing multiple nested loops

#uses

#working with multidimensional arrays

#cleaner code

#better readability

#syntax

#np.nditer(array)

#return type

#numpy.nditer object

print("Using nditer")

for value in np.nditer(data):

    print(value)



#np.ndenumerate()

#definition

#ndenumerate() returns both the index and the value

#it is useful when you need to know the position of each element

#syntax

#np.ndenumerate(array)

#return type

#iterator returning (index,value)

print("Using ndenumerate")

for index, value in np.ndenumerate(marks):

    print(index, value)



#real world example

#suppose these are product prices

prices = np.array([[250,300],

                   [450,500]])

print("Product Prices")

for index, price in np.ndenumerate(prices):

    print("Index :", index, "Price :", price)



#important interview points

#for loop is suitable for simple arrays

#nested loops are needed for multidimensional arrays

#nditer() automatically iterates through all elements

#ndenumerate() returns both index and value

#nditer() makes code shorter for multidimensional arrays
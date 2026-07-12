#importing numpy library

import numpy as np


#creating a one dimensional array

numbers = np.array([10,20,30,40,50,60,70,80,90,100,110,120])

print(numbers)



#reshape()

#definition

#reshape() is used to change the shape of an array without changing its data

#it only changes the arrangement of elements

#types

#1 reshape into 2D array

#2 reshape into 3D array

#3 reshape using -1 (automatic calculation)

#uses

#used in data analysis

#used in machine learning

#used to prepare datasets

#used while working with images

#syntax

#array.reshape(rows, columns)

#return type

#numpy.ndarray

matrix = numbers.reshape(3,4)

print(matrix)

#output

#[[ 10  20  30  40]
# [ 50  60  70  80]
# [ 90 100 110 120]]



#changing into another shape

matrix = numbers.reshape(4,3)

print(matrix)



#using -1

#numpy automatically calculates the missing dimension

matrix = numbers.reshape(2,-1)

print(matrix)



matrix = numbers.reshape(-1,6)

print(matrix)



#important note

#total number of elements must remain the same

#12 elements can become

#3 x 4

#4 x 3

#2 x 6

#6 x 2

#but cannot become 5 x 3 because 15 positions are required



#flatten()

#definition

#flatten() converts a multidimensional array into a one dimensional array

#flatten() creates a completely new copy

#if the flattened array changes the original array does not change

#uses

#used before exporting data

#used before plotting

#used before passing data to machine learning models

#syntax

#array.flatten()

#return type

#numpy.ndarray

flat = matrix.flatten()

print(flat)



flat[0] = 999

print(flat)

print(matrix)

#original array remains unchanged



#ravel()

#definition

#ravel() also converts a multidimensional array into a one dimensional array

#difference

#ravel() usually returns a view instead of a copy

#changing the ravel array may also change the original array

#uses

#uses less memory

#faster than flatten()

#preferred when a copy is not required

#syntax

#array.ravel()

#return type

#numpy.ndarray

ravel_array = matrix.ravel()

print(ravel_array)



ravel_array[1] = 555

print(ravel_array)

print(matrix)

#notice the original array also changes



#transpose()

#definition

#transpose() converts rows into columns and columns into rows

#types

#1 transpose()

#2 .T

#uses

#used in matrix operations

#used in linear algebra

#used in machine learning

#used while preparing datasets

#syntax

#array.transpose()

#return type

#numpy.ndarray

student_marks = np.array([

    [85,90,95],

    [70,80,88],

    [92,84,91]

])

print(student_marks)



transposed = student_marks.transpose()

print(transposed)



#another way

print(student_marks.T)



#real world example

#suppose every row represents one student

#every column represents one subject

marks = np.array([

    [88,90,85],

    [75,80,79],

    [92,95,91],

    [68,72,70]

])

print(marks)



#convert all marks into one list

all_marks = marks.flatten()

print(all_marks)



#reshape them into 2 rows

new_marks = all_marks.reshape(2,6)

print(new_marks)



#important interview points

#reshape()

#changes the shape only

#does not change data



#flatten()

#returns a copy

#original array is not affected



#ravel()

#returns a view whenever possible

#original array may change



#transpose()

#interchanges rows and columns
#importing numpy library
#numpy is required because indexing and slicing are performed on numpy arrays

import numpy as np


#indexing means accessing a specific element from an array

#slicing means accessing multiple elements from an array

#numpy supports
#1 positive indexing
#2 negative indexing
#3 slicing
#4 fancy indexing
#5 boolean indexing

#all these are heavily used in
#data analysis
#machine learning
#image processing
#data cleaning



#creating a one dimensional array

numbers = np.array([10,20,30,40,50,60,70,80])

print(numbers)



#positive indexing

#positive indexing starts from 0

#index     0   1   2   3   4   5   6   7
#value    10  20  30  40  50  60  70  80

print(numbers[0])

#returns first element

print(numbers[3])

#returns fourth element

print(numbers[7])

#returns last element



#negative indexing

#negative indexing starts from the end

#index    -8  -7  -6  -5  -4  -3  -2  -1
#value    10  20  30  40  50  60  70  80

print(numbers[-1])

#returns last element

print(numbers[-2])

#returns second last element

print(numbers[-5])

#returns value 40



#slicing

#definition

#slicing is used to extract multiple values from an array

#syntax

#array[start : stop : step]

#start
#starting position

#stop
#ending position is excluded

#step
#how many positions to skip

print(numbers[1:5])

#starts from index 1
#stops before index 5

#output
#[20 30 40 50]



print(numbers[:4])

#starts from beginning
#stops before index 4

#output
#[10 20 30 40]



print(numbers[3:])

#starts from index 3
#goes till end

#output
#[40 50 60 70 80]



print(numbers[:])

#returns complete array



print(numbers[::2])

#step is 2

#returns every second element

#output
#[10 30 50 70]



print(numbers[::-1])

#negative step reverses the array

#output
#[80 70 60 50 40 30 20 10]



#creating a two dimensional array

marks = np.array([

    [85,90,95],

    [75,80,88],

    [92,91,89]

])

print(marks)



#indexing in two dimensional array

#syntax

#array[row,column]

print(marks[0,0])

#first row
#first column

#output
#85



print(marks[1,2])

#second row
#third column

#output
#88



print(marks[2,1])

#third row
#second column

#output
#91



#slicing rows

print(marks[0:2])

#returns first two rows



#slicing columns

print(marks[:,1])

#:
#means all rows

#1
#means second column

#output
#[90 80 91]



print(marks[:,2])

#returns third column

#output
#[95 88 89]



#selecting specific rows and columns

print(marks[0:2,1:3])

#first two rows

#second and third columns

#output

#[[90 95]
# [80 88]]



#fancy indexing

#definition

#fancy indexing means selecting elements using a list of indexes

#used when specific values are required

print(numbers[[0,2,5,7]])

#output

#[10 30 60 80]



#boolean indexing

#definition

#boolean indexing filters data based on a condition

#extremely important for data analysis

print(numbers>40)

#returns boolean values

#[False False False False True True True True]



print(numbers[numbers>40])

#returns only values greater than 40

#[50 60 70 80]



print(numbers[numbers%2==0])

#returns even numbers

#all numbers are even



print(numbers[numbers>=50])

#returns values greater than or equal to 50



#real world example

#suppose these are employee salaries

salary = np.array([25000,42000,65000,18000,71000,50000])

print(salary[salary>40000])

#returns employees having salary greater than 40000



#interview question

#difference between indexing and slicing

#indexing returns one element

#slicing returns multiple elements
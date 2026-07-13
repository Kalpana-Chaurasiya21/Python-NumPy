#importing numpy library

import numpy as np


#creating two arrays

#suppose these arrays contain marks of students in two subjects

subject1 = np.array([80, 75, 90, 85, 95])

subject2 = np.array([5, 10, 5, 10, 5])

print(subject1)
print(subject2)



#+ operator

#definition

#the + operator adds corresponding elements of two arrays

#types

#1 array + array

#2 array + scalar(single value)

#uses

#used for calculating

#total marks

#total sales

#total expenses

#adding bonus values

#syntax

#array1 + array2

#array + value

#return type

#numpy.ndarray

addition = subject1 + subject2

print(addition)



#adding one value to every element

#numpy automatically performs this operation on every element

bonus_marks = subject1 + 5

print(bonus_marks)



#real world example

#every student receives 5 grace marks

marks = np.array([45,55,62,71,89])

updated_marks = marks + 5

print(updated_marks)



#- operator

#definition

#the - operator subtracts corresponding elements

#types

#1 array - array

#2 array - scalar

#uses

#used for

#negative marking

#remaining balance

#profit and loss

#temperature difference

#syntax

#array1 - array2

#array - value

#return type

#numpy.ndarray

subtraction = subject1 - subject2

print(subtraction)



#subtracting one value from every element

updated = subject1 - 2

print(updated)



#real world example

#2 marks deducted due to negative marking

exam_marks = np.array([90,82,76,95])

final_marks = exam_marks - 2

print(final_marks)



#* operator

#definition

#the * operator multiplies corresponding elements

#important note

#this performs element wise multiplication

#this is not matrix multiplication

#types

#1 array * array

#2 array * scalar

#uses

#price × quantity

#salary × increment

#distance × rate

#image processing

#syntax

#array1 * array2

#array * value

#return type

#numpy.ndarray

multiplication = subject1 * subject2

print(multiplication)



#multiplying every element by 2

double_marks = subject1 * 2

print(double_marks)



#real world example

#salary increased by 10%

salary = np.array([25000,30000,45000])

updated_salary = salary * 1.10

print(updated_salary)



#/ operator

#definition

#the / operator divides corresponding elements

#important note

#division always returns floating point values

#types

#1 array / array

#2 array / scalar

#uses

#average calculation

#percentage

#growth rate

#ratio

#syntax

#array1 / array2

#array / value

#return type

#numpy.ndarray

division = subject1 / subject2

print(division)



#dividing every element by 2

half_marks = subject1 / 2

print(half_marks)



#real world example

#monthly salary distributed equally between two accounts

salary = np.array([40000,50000,60000])

account = salary / 2

print(account)



#multiple operations together

result = (subject1 + subject2) / 2

print(result)



#important interview points

#numpy performs all arithmetic operations element by element

#this feature is called element wise operation

#vectorized operations make numpy much faster than python lists

#the original arrays never change unless we assign the result back
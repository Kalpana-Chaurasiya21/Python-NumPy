#importing numpy library

import numpy as np


#creating a numpy array

numbers = np.array([10,20,30,40,50])

print(numbers)



#Copy and View

#definition

#copy() creates a completely new array

#view() creates another reference to the same array

#this is one of the most important interview topics in numpy



#np.copy()

#definition

#copy() creates an independent copy of an array

#the copied array has its own memory location

#changing the copied array does not affect the original array

#syntax

#array.copy()

#return type

#numpy.ndarray

copy_array = numbers.copy()

print(copy_array)



#changing copied array

copy_array[0] = 100

print("Copied Array :", copy_array)

print("Original Array :", numbers)



#notice

#the original array remains unchanged

#because copy() creates a completely separate array



#checking memory location

print(id(numbers))

print(id(copy_array))

#both memory addresses are different



#np.view()

#definition

#view() creates another view of the original array

#it does not create a new copy

#both arrays share the same memory

#changing one array changes the other

#syntax

#array.view()

#return type

#numpy.ndarray

view_array = numbers.view()

print(view_array)



#changing view array

view_array[1] = 999

print("View Array :", view_array)

print("Original Array :", numbers)



#notice

#the original array also changes

#because both arrays share the same memory



#changing original array

numbers[2] = 555

print("Original Array :", numbers)

print("View Array :", view_array)



#checking memory addresses

print(id(numbers))

print(id(view_array))

#the array objects have different ids

#but they share the same underlying data



#checking base attribute

#definition

#base tells whether an array owns its data

#if base is None

#the array owns its own memory

#if base is another array

#it shares memory with that array

print(copy_array.base)

print(view_array.base)



#real world example

#employee salaries

salary = np.array([25000,30000,35000,40000])



#creating a backup copy

backup_salary = salary.copy()

backup_salary[0] = 50000

print(backup_salary)

print(salary)



#creating a view

live_salary = salary.view()

live_salary[1] = 60000

print(live_salary)

print(salary)



#important interview points

#copy() creates a new independent array

#view() shares the original data

#copy() uses more memory

#view() uses less memory

#changes in copy do not affect the original array

#changes in view affect the original array
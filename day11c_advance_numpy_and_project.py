#importing numpy library

import numpy as np


#Advanced NumPy Functions

#definition

#these are some advanced functions provided by numpy

#they help in creating arrays efficiently

#and writing cleaner code



#np.vectorize()

#definition

#vectorize() converts a normal python function

#so that it can work on every element of a numpy array

#uses

#applying custom functions

#avoiding manual loops

#syntax

#np.vectorize(function)

def grade(mark):

    if mark >= 90:

        return "A"

    elif mark >= 75:

        return "B"

    elif mark >= 60:

        return "C"

    else:

        return "Fail"



marks = np.array([95,82,76,65,45])

vectorized_grade = np.vectorize(grade)

print(vectorized_grade(marks))



#np.fromiter()

#definition

#fromiter() creates a numpy array

#from any iterable object

#uses

#converting generators

#lists

#tuples

#ranges into numpy arrays

#syntax

#np.fromiter(iterable,dtype)

numbers = range(1,11)

array = np.fromiter(numbers,dtype=int)

print(array)



#np.fromfunction()

#definition

#fromfunction() creates an array

#based on a function

#the function receives the index values

#syntax

#np.fromfunction(function,shape)

matrix = np.fromfunction(lambda row,column : row + column,(3,4),dtype=int)

print(matrix)



#Mini Project

#Employee Salary Analysis

employee_id = np.array([101,102,103,104,105])

salary = np.array([25000,40000,35000,55000,30000])



print("Employee IDs")

print(employee_id)



print("Employee Salaries")

print(salary)



print("Average Salary")

print(np.mean(salary))



print("Highest Salary")

print(np.max(salary))



print("Lowest Salary")

print(np.min(salary))



print("Employees earning more than 35000")

print(salary[salary > 35000])



print("Sorted Salaries")

print(np.sort(salary))



print("Salary Standard Deviation")

print(np.std(salary))



print("Unique Salaries")

print(np.unique(salary))



print("Highest Salary Index")

print(np.argmax(salary))



print("Lowest Salary Index")

print(np.argmin(salary))



#important interview points

#vectorize() applies custom functions

#fromiter() creates arrays from iterables

#fromfunction() creates arrays using index values

#boolean masking filters data

#aggregation functions summarize data

#sorting organizes data

#numpy is optimized for fast numerical computation
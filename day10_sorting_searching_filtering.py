#importing numpy library

import numpy as np


#creating a numpy array

marks = np.array([85, 67, 92, 76, 95, 81, 67])

print(marks)



#np.sort()

#definition

#sort() arranges the elements in ascending order by default

#it returns a new sorted array

#the original array remains unchanged

#types

#1 ascending order

#2 descending order (using slicing)

#uses

#used for ranking

#report generation

#salary analysis

#exam results

#syntax

#np.sort(array)

#return type

#numpy.ndarray

sorted_marks = np.sort(marks)

print(sorted_marks)



#descending order

descending = np.sort(marks)[::-1]

print(descending)



#printing original array

print(marks)



#np.argsort()

#definition

#argsort() returns the indices that would sort the array

#it does not return the sorted values

#it returns the positions of those values

#uses

#sorting records

#finding ranks

#sorting related arrays

#syntax

#np.argsort(array)

#return type

#numpy.ndarray

index = np.argsort(marks)

print(index)



#printing sorted values using indices

print(marks[index])



#np.where()

#definition

#where() returns the indices of elements that satisfy a condition

#types

#1 single condition

#2 multiple conditions

#uses

#filtering data

#finding students who passed

#finding employees with high salary

#syntax

#np.where(condition)

#return type

#tuple containing numpy arrays

passed_students = np.where(marks >= 80)

print(passed_students)



#printing actual values

print(marks[passed_students])



#students scoring above 90

top_students = np.where(marks > 90)

print(marks[top_students])



#multiple conditions

excellent = np.where((marks >= 80) & (marks <= 90))

print(marks[excellent])



#np.searchsorted()

#definition

#searchsorted() finds the position where a value should be inserted

#so that the array remains sorted

#important note

#the array should already be sorted

#syntax

#np.searchsorted(sorted_array, value)

#return type

#numpy integer

numbers = np.array([10,20,30,40,50])

position = np.searchsorted(numbers,35)

print(position)



position = np.searchsorted(numbers,45)

print(position)



#np.unique()

#definition

#unique() returns only unique values

#duplicate values are removed automatically

#uses

#finding unique cities

#unique customer ids

#removing duplicates

#syntax

#np.unique(array)

#return type

#numpy.ndarray

cities = np.array(["Delhi","Mumbai","Delhi","Pune","Mumbai","Chennai"])

unique_cities = np.unique(cities)

print(unique_cities)



numbers = np.array([10,20,10,30,40,20,50])

unique_numbers = np.unique(numbers)

print(unique_numbers)



#real world example

#suppose these are employee salaries

salary = np.array([25000,40000,35000,25000,50000,40000])

print("Sorted Salary :", np.sort(salary))

print("Unique Salary :", np.unique(salary))

print("Salary Greater Than 30000 :", salary[np.where(salary > 30000)])



#important interview points

#sort() returns sorted values

#argsort() returns sorted indices

#where() returns indices that satisfy a condition

#searchsorted() finds insertion position

#unique() removes duplicate values
#importing numpy library

import numpy as np


#Broadcasting

#definition

#broadcasting is a feature in numpy that allows arrays of different shapes

#to perform arithmetic operations without manually making their sizes equal

#numpy automatically expands the smaller array whenever possible

#without actually creating extra copies in memory

#this makes operations very fast and memory efficient



#why do we use broadcasting?

#without broadcasting we would have to write loops

#or manually create arrays of the same size

#broadcasting makes the code shorter

#faster

#and easier to understand



#broadcasting rules

#rule 1

#numpy compares the shapes from right to left

#rule 2

#two dimensions are compatible if

#they are equal

#or one of them is 1

#rule 3

#if neither condition is satisfied

#numpy raises a ValueError



#Example 1

#array + scalar

marks = np.array([75,80,85,90,95])

print(marks)



#adding 5 bonus marks to every student

bonus_marks = marks + 5

print(bonus_marks)



#numpy automatically adds 5 to every element

#this is broadcasting



#Example 2

#multiplying every salary by 10%

salary = np.array([25000,30000,35000,40000])

updated_salary = salary * 1.10

print(updated_salary)



#Example 3

#adding two arrays having the same shape

array1 = np.array([10,20,30])

array2 = np.array([1,2,3])

result = array1 + array2

print(result)



#Example 4

#broadcasting in two dimensional arrays

matrix = np.array([[10,20,30],

                   [40,50,60],

                   [70,80,90]])

print(matrix)



#adding 100 to every element

updated_matrix = matrix + 100

print(updated_matrix)



#Example 5

#broadcasting between 2D and 1D arrays

sales = np.array([[1000,1200,1500],

                  [2000,2200,2500],

                  [3000,3200,3500]])

print(sales)



#monthly bonus added to each column

bonus = np.array([100,200,300])

print(bonus)



final_sales = sales + bonus

print(final_sales)



#numpy compares the last dimensions

#sales shape is (3,3)

#bonus shape is (3,)

#they are compatible

#therefore broadcasting happens automatically



#Example 6

#broadcasting with column values

numbers = np.array([[1],

                    [2],

                    [3]])

print(numbers)



values = np.array([10,20,30])

print(values)



answer = numbers + values

print(answer)



#shape of numbers

#(3,1)

#shape of values

#(3,)

#numpy expands both arrays automatically

#result becomes a 3x3 matrix



#Example 7

#incompatible shapes

a = np.array([10,20,30])

b = np.array([5,10])



#print(a + b)



#this gives ValueError

#because shapes are incompatible

#(3,) and (2,)



#important interview points

#broadcasting does not create duplicate arrays

#it is memory efficient

#it follows three broadcasting rules

#broadcasting works only if shapes are compatible

#broadcasting is one of the reasons numpy is much faster than python lists
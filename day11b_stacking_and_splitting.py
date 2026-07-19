#importing numpy library

import numpy as np


#Stacking and Splitting Arrays

#definition

#stacking means combining two or more arrays

#splitting means dividing one array into multiple smaller arrays

#these operations are commonly used while combining datasets

#or preparing data for machine learning



#creating arrays

array1 = np.array([10,20,30])

array2 = np.array([40,50,60])

print(array1)

print(array2)



#np.concatenate()

#definition

#concatenate() joins two or more arrays

#the arrays must have compatible shapes

#syntax

#np.concatenate((array1,array2))

#return type

#numpy.ndarray

combined = np.concatenate((array1,array2))

print(combined)



#creating two dimensional arrays

matrix1 = np.array([[1,2],
                    [3,4]])

matrix2 = np.array([[5,6],
                    [7,8]])

print(matrix1)

print(matrix2)



#concatenate rows

row_join = np.concatenate((matrix1,matrix2),axis=0)

print(row_join)



#concatenate columns

column_join = np.concatenate((matrix1,matrix2),axis=1)

print(column_join)



#np.vstack()

#definition

#vstack means vertical stack

#it joins arrays row wise

#syntax

#np.vstack((array1,array2))

#return type

#numpy.ndarray

vertical = np.vstack((array1,array2))

print(vertical)



#np.hstack()

#definition

#hstack means horizontal stack

#for one dimensional arrays

#it joins arrays side by side

#syntax

#np.hstack((array1,array2))

horizontal = np.hstack((array1,array2))

print(horizontal)



#np.dstack()

#definition

#dstack means depth stack

#it stacks arrays along the third dimension

#mostly used while working with images

depth = np.dstack((matrix1,matrix2))

print(depth)



#np.split()

#definition

#split() divides an array into equal parts

#syntax

#np.split(array,number_of_parts)

#return type

#list of numpy arrays

numbers = np.array([10,20,30,40,50,60])

parts = np.split(numbers,3)

print(parts)



#printing each part

for part in parts:

    print(part)



#np.vsplit()

#definition

#vsplit() splits a matrix row wise

matrix = np.array([[10,20],
                   [30,40],
                   [50,60],
                   [70,80]])

vertical_split = np.vsplit(matrix,2)

print(vertical_split)



#np.hsplit()

#definition

#hsplit() splits a matrix column wise

matrix = np.array([[10,20,30,40],
                   [50,60,70,80]])

horizontal_split = np.hsplit(matrix,2)

print(horizontal_split)



#real world example

#sales data from two branches

branch1 = np.array([1200,1500,1800])

branch2 = np.array([2100,2400,2600])

total_sales = np.concatenate((branch1,branch2))

print(total_sales)



#important interview points

#concatenate() joins arrays

#vstack() joins vertically

#hstack() joins horizontally

#dstack() joins along the third dimension

#split() divides arrays into equal parts

#vsplit() splits rows

#hsplit() splits columns
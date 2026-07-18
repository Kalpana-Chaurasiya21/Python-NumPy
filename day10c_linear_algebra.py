#importing numpy library

import numpy as np


#Linear Algebra

#definition

#linear algebra is a branch of mathematics

#it deals with vectors

#matrices

#and matrix operations

#numpy provides a separate module called numpy.linalg

#used in

#machine learning

#computer vision

#deep learning

#data science

#scientific computing



#creating matrices

matrix1 = np.array([[2,4],
                    [6,8]])

matrix2 = np.array([[1,3],
                    [5,7]])

print(matrix1)
print(matrix2)



#matrix addition

#definition

#adds corresponding elements

addition = matrix1 + matrix2

print(addition)



#matrix subtraction

subtraction = matrix1 - matrix2

print(subtraction)



#matrix multiplication

#definition

#matrix multiplication follows mathematical matrix rules

#do not confuse it with *

#* performs element wise multiplication

#syntax

#np.matmul(matrix1,matrix2)

#or

#matrix1 @ matrix2

multiplication = np.matmul(matrix1,matrix2)

print(multiplication)



multiplication2 = matrix1 @ matrix2

print(multiplication2)



#element wise multiplication

element = matrix1 * matrix2

print(element)



#transpose

#definition

#rows become columns

transpose = matrix1.T

print(transpose)



#determinant

#definition

#determinant is a special value calculated from a square matrix

#used to check whether a matrix is invertible

#syntax

#np.linalg.det(matrix)

det = np.linalg.det(matrix1)

print(det)



#inverse

#definition

#inverse is a matrix which when multiplied with the original matrix

#produces the identity matrix

#syntax

#np.linalg.inv(matrix)

inverse = np.linalg.inv(matrix1)

print(inverse)



#identity matrix

identity = np.eye(3)

print(identity)



#real world example

#suppose matrix represents sales

sales = np.array([[100,200],
                  [300,400]])

growth = np.array([[2,0],
                   [0,2]])

updated_sales = np.matmul(sales,growth)

print(updated_sales)



#important interview points

#* performs element wise multiplication

#@ and np.matmul() perform matrix multiplication

#transpose changes rows into columns

#determinant is calculated only for square matrices

#inverse exists only if determinant is not zero
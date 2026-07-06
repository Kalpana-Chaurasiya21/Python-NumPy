#numpy stands for numerical python

#numpy is an open source python library

#it is mainly used for numerical computing

#numpy is faster than normal python lists

#it is widely used in
#data analysis
#machine learning
#artificial intelligence
#scientific computing
#deep learning




#IMPORTING NUMPY


#first install numpy if it is not installed

#pip install numpy

#import numpy library

import numpy as np

#np is an alias
#it is shorter and easier to write

print(np.__version__)

#output
#your installed numpy version




#WHY NUMPY IS USED


#python list

numbers = [10, 20, 30, 40, 50]

print(numbers)

#output
#[10, 20, 30, 40, 50]



#numpy array

array = np.array([10, 20, 30, 40, 50])

print(array)

#output
#[10 20 30 40 50]




#CHECKING DATA TYPE


#type() returns the type of object

numbers = [1, 2, 3]

array = np.array([1, 2, 3])

print(type(numbers))

#output
#<class 'list'>

print(type(array))

#output
#<class 'numpy.ndarray'>




#WHY NUMPY IS FASTER


#python list stores different object types separately

python_list = [1, 2, 3, 4]



#numpy stores elements in continuous memory

numpy_array = np.array([1, 2, 3, 4])



#continuous memory makes
#reading
#writing
#calculations
#much faster




#CREATING A NUMPY ARRAY


numbers = np.array([5, 10, 15, 20])

print(numbers)

#output
#[ 5 10 15 20 ]




#ARRAY CAN STORE DIFFERENT DATA TYPES


integer_array = np.array([10, 20, 30])

print(integer_array)

#output
#[10 20 30]



float_array = np.array([10.5, 20.5, 30.5])

print(float_array)

#output
#[10.5 20.5 30.5]



string_array = np.array(["python", "numpy", "pandas"])

print(string_array)

#output
#['python' 'numpy' 'pandas']



boolean_array = np.array([True, False, True])

print(boolean_array)

#output
#[ True False  True ]




#MIXED DATA TYPE

#numpy converts all elements to a common compatible type

mixed = np.array([10, 20.5, 30])

print(mixed)

#output
#[10.  20.5 30. ]



print(mixed.dtype)

#output
#float64




#CHECKING ARRAY DATA TYPE


numbers = np.array([100, 200, 300])

print(numbers.dtype)

#output
#int64 (may be int32 on some systems)




#CHECKING ARRAY DIMENSION


numbers = np.array([1, 2, 3])

print(numbers.ndim)

#output
#1




#CHECKING ARRAY SHAPE


numbers = np.array([1, 2, 3, 4])

print(numbers.shape)

#output
#(4,)




#CHECKING TOTAL ELEMENTS


numbers = np.array([1, 2, 3, 4, 5])

print(numbers.size)

#output
#5




#CHECKING MEMORY USED


numbers = np.array([1, 2, 3, 4])

print(numbers.itemsize)

#output
#memory used by one element in bytes



print(numbers.nbytes)

#output
#total memory used by array




#REAL WORLD EXAMPLE


#marks of students

marks = np.array([85, 92, 76, 88, 95])

print(marks)

#later we can easily calculate
#average
#maximum
#minimum
#percentage
#using numpy functions




#array attributes provide information about a numpy array
#they tell us about the array's dimensions shape size data type and memory usage

#import numpy

import numpy as np




#CREATING A ONE DIMENSIONAL ARRAY


numbers = np.array([10, 20, 30, 40, 50])

print(numbers)




#ndim


#ndim means number of dimensions

print(numbers.ndim)

#output
#1




#shape


#shape returns the size of each dimension
#for a one dimensional array it returns number of elements

print(numbers.shape)

#output
#(5,)




#size


#size returns total number of elements

print(numbers.size)

#output
#5




#dtype


#dtype tells us the data type stored inside the array

print(numbers.dtype)

#output
#int64
#some systems may show int32




#itemsize


#itemsize tells memory occupied by one element
#memory is measured in bytes

print(numbers.itemsize)

#output
#8
#or 4 depending on your system




#nbytes


#nbytes returns total memory used by array

print(numbers.nbytes)

#output
#40




#creating a two dimensional array


marks = np.array([
    [85, 90, 88],
    [92, 80, 75]
])

print(marks)




#ndim for 2d array


print(marks.ndim)

#output
#2




#shape for 2d array


#2 rows
#3 columns

print(marks.shape)

#output
#(2,3)




#size


#total elements = rows × columns

print(marks.size)

#output
#6




#dtype


print(marks.dtype)

#output
#int64




#memory occupied


print(marks.itemsize)

print(marks.nbytes)




#astype()


#astype changes the data type of an array

numbers = np.array([1, 2, 3, 4])

print(numbers.dtype)

#output
#int64



#convert integer array into float array

float_numbers = numbers.astype(float)

print(float_numbers)

print(float_numbers.dtype)

#output
#[1. 2. 3. 4.]
#float64




#convert float into integer


decimal_numbers = np.array([10.5, 20.9, 30.2])

integer_numbers = decimal_numbers.astype(int)

print(integer_numbers)

#output
#[10 20 30]




#copy()


#copy creates a completely separate array
#changing copied array does not affect original array

numbers = np.array([10, 20, 30])

new_numbers = numbers.copy()

new_numbers[0] = 100

print(numbers)

print(new_numbers)

#output
#[10 20 30]
#[100 20 30]




#view()


#view shares memory with original array
#changing one affects the other

numbers = np.array([10, 20, 30])

new_view = numbers.view()

new_view[0] = 999

print(numbers)

print(new_view)

#output
#[999 20 30]
#[999 20 30]




#flags


#flags give information about memory layout

numbers = np.array([1, 2, 3])

print(numbers.flags)




#real world example


#marks of students

marks = np.array([
    [88, 91, 75],
    [95, 82, 90],
    [78, 85, 92]
])

print("dimensions :", marks.ndim)

print("shape :", marks.shape)

print("students :", marks.shape[0])

print("subjects :", marks.shape[1])

print("total marks entered :", marks.size)

print("memory used :", marks.nbytes, "bytes")




#important interview question


#difference between copy() and view()

#copy()
#creates independent array

#view()
#shares memory with original array
#importing numpy library

import numpy as np


#creating a numpy array

marks = np.array([85,92,76,88,95])

print(marks)



#NumPy File Handling

#definition

#numpy provides functions to save arrays into files

#and load them back whenever needed

#this helps avoid creating the same arrays again

#uses

#saving datasets

#storing machine learning data

#sharing arrays

#loading data later



#np.save()

#definition

#save() stores a numpy array in binary format

#the file extension is .npy

#syntax

#np.save(filename,array)

#return type

#None

np.save("student_marks.npy", marks)

print("Array Saved Successfully")



#np.load()

#definition

#load() reads a previously saved .npy file

#syntax

#np.load(filename)

#return type

#numpy.ndarray

loaded_marks = np.load("student_marks.npy")

print(loaded_marks)



#creating a two dimensional array

students = np.array([

    [101,85],

    [102,92],

    [103,76],

    [104,88]

])

print(students)



#saving another array

np.save("students.npy", students)



#loading it

loaded_students = np.load("students.npy")

print(loaded_students)



#np.savetxt()

#definition

#savetxt() stores data in a text file

#text files can be opened using notepad or excel

#syntax

#np.savetxt(filename,array)

#return type

#None

np.savetxt("marks.txt", marks)

print("Text File Saved")



#saving with comma separator

np.savetxt("students.csv", students, delimiter=",", fmt="%d")

print("CSV File Saved")



#np.loadtxt()

#definition

#loadtxt() loads data from a text or csv file

#syntax

#np.loadtxt(filename)

#return type

#numpy.ndarray

loaded_text = np.loadtxt("marks.txt")

print(loaded_text)



loaded_csv = np.loadtxt("students.csv", delimiter=",")

print(loaded_csv)



#real world example

#suppose these are employee salaries

salary = np.array([25000,32000,41000,50000])



#saving salary data

np.save("salary.npy", salary)



#loading salary data

salary_data = np.load("salary.npy")

print(salary_data)



#important interview points

#save() stores arrays in binary format

#load() reads .npy files

#savetxt() stores arrays as text files

#loadtxt() reads text or csv files

#npy files are faster than text files

#csv files are easy to open in excel
#importing numpy library

import numpy as np


#Random Module

#definition

#the random module is used to generate random numbers

#it helps create sample datasets for testing

#it is widely used in

#data analysis

#machine learning

#deep learning

#simulations

#games



#np.random.rand()

#definition

#generates random decimal numbers between 0 and 1

#types

#1 one dimensional

#2 two dimensional

#3 multidimensional

#syntax

#np.random.rand(rows,columns)

#return type

#numpy.ndarray

random_numbers = np.random.rand(5)

print(random_numbers)



matrix = np.random.rand(3,4)

print(matrix)



#np.random.randn()

#definition

#generates random numbers from the standard normal distribution

#mean = 0

#standard deviation = 1

#values can be positive or negative

#uses

#machine learning

#statistics

#scientific simulations

#syntax

#np.random.randn(rows,columns)

#return type

#numpy.ndarray

normal_numbers = np.random.randn(5)

print(normal_numbers)



matrix = np.random.randn(2,3)

print(matrix)



#np.random.randint()

#definition

#generates random integers between a given range

#the upper limit is excluded

#syntax

#np.random.randint(low,high,size)

#return type

#numpy.ndarray

marks = np.random.randint(40,101,size=10)

print(marks)



matrix = np.random.randint(1,10,size=(3,4))

print(matrix)



#np.random.choice()

#definition

#randomly selects values from a given array

#uses

#random sampling

#survey selection

#lottery systems

#syntax

#np.random.choice(array,size)

#return type

#numpy.ndarray

subjects = np.array(["Python","SQL","Power BI","Excel"])

selected = np.random.choice(subjects,size=2)

print(selected)



#np.random.shuffle()

#definition

#randomly rearranges the elements

#important note

#shuffle changes the original array

#it does not return a new array

#syntax

#np.random.shuffle(array)

#return type

#None

cards = np.array([1,2,3,4,5,6,7,8])

print(cards)

np.random.shuffle(cards)

print(cards)



#np.random.seed()

#definition

#seed() fixes the sequence of random numbers

#every time the program runs

#the same random numbers will be generated

#uses

#testing

#debugging

#machine learning experiments

#syntax

#np.random.seed(number)

#return type

#None

np.random.seed(10)

print(np.random.randint(1,100,size=5))

np.random.seed(10)

print(np.random.randint(1,100,size=5))



#real world example

#generating random customer ids

customer_ids = np.random.randint(1000,9999,size=10)

print(customer_ids)



#generating random ratings

ratings = np.random.randint(1,6,size=20)

print(ratings)



#important interview points

#rand() returns decimal values between 0 and 1

#randn() returns values from a normal distribution

#randint() returns random integers

#choice() randomly selects values

#shuffle() changes the original array

#seed() makes random numbers reproducible
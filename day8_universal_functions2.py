#importing numpy library

import numpy as np


#creating a decimal array

numbers = np.array([2.35, 5.67, 8.91, 10.49, 15.50])

print(numbers)



#np.round()

#definition

#round() rounds each element to the nearest value

#if decimal places are provided it rounds to that many decimal places

#types

#1 round to nearest integer

#2 round to specified decimal places

#uses

#used in financial reports

#used while displaying results

#used to reduce unnecessary decimal values

#syntax

#np.round(array)

#np.round(array, decimals)

#return type

#numpy.ndarray

rounded = np.round(numbers)

print(rounded)



#rounding to one decimal place

rounded_one = np.round(numbers,1)

print(rounded_one)



#rounding to two decimal places

rounded_two = np.round(numbers,2)

print(rounded_two)



#np.ceil()

#definition

#ceil means ceiling

#it always rounds the value upward to the nearest integer

#even if the decimal part is very small

#syntax

#np.ceil(array)

#return type

#numpy.ndarray

ceil_result = np.ceil(numbers)

print(ceil_result)



#real world example

#suppose a customer uses 2.1 GB internet

#the company charges for the next complete GB

internet_usage = np.array([2.1,3.4,5.8,7.2])

billable_usage = np.ceil(internet_usage)

print(billable_usage)



#np.floor()

#definition

#floor always rounds downward to the nearest integer

#it removes the decimal part by moving towards the smaller integer

#syntax

#np.floor(array)

#return type

#numpy.ndarray

floor_result = np.floor(numbers)

print(floor_result)



#real world example

#counting completed hours only

hours = np.array([5.8,6.2,7.9,8.1])

completed_hours = np.floor(hours)

print(completed_hours)



#np.exp()

#definition

#exp stands for exponential

#it calculates e raised to the power of each element

#e is approximately equal to 2.71828

#uses

#used in machine learning

#used in probability

#used in deep learning

#syntax

#np.exp(array)

#return type

#numpy.ndarray

values = np.array([1,2,3])

exp_result = np.exp(values)

print(exp_result)



#np.log()

#definition

#returns the natural logarithm of each element

#natural logarithm means logarithm with base e

#syntax

#np.log(array)

#return type

#numpy.ndarray

numbers = np.array([1,2,4,8,16])

log_result = np.log(numbers)

print(log_result)



#np.log2()

#definition

#returns logarithm with base 2

#used in computer science and binary calculations

#syntax

#np.log2(array)

log2_result = np.log2(numbers)

print(log2_result)



#np.log10()

#definition

#returns logarithm with base 10

#used in statistics

#used in scientific calculations

#syntax

#np.log10(array)

log10_result = np.log10(numbers)

print(log10_result)



#important interview points

#np.round() rounds to the nearest value

#np.ceil() always rounds upward

#np.floor() always rounds downward

#np.exp() calculates e raised to the power x

#np.log() returns natural logarithm

#np.log2() returns logarithm with base 2

#np.log10() returns logarithm with base 10
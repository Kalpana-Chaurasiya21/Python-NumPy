#importing numpy library

import numpy as np


#creating a numpy array

#suppose these are marks obtained by students

marks = np.array([85,92,76,88,95,67,81])

print(marks)



#np.median()

#definition

#median is the middle value after arranging the data in ascending order

#if the number of values is odd

#the middle value is the median

#if the number of values is even

#the average of the two middle values becomes the median

#uses

#used when data contains outliers

#used in salary analysis

#used in house price analysis

#used in business reports

#syntax

#np.median(array)

#return type

#numpy float

median_marks = np.median(marks)

print(median_marks)



#real world example

#employee salaries

salary = np.array([25000,27000,28000,30000,32000,150000])

print(np.mean(salary))

print(np.median(salary))

#notice that the mean becomes very high because of one large salary

#median represents the actual middle salary better



#np.std()

#definition

#std means standard deviation

#it measures how spread out the data is from the average

#small standard deviation means

#values are close to the average

#large standard deviation means

#values are spread far from the average

#uses

#machine learning

#statistics

#quality control

#data analysis

#syntax

#np.std(array)

#return type

#numpy float

standard_deviation = np.std(marks)

print(standard_deviation)



#np.var()

#definition

#variance is the square of the standard deviation

#it measures data dispersion

#uses

#statistics

#machine learning

#data science

#syntax

#np.var(array)

#return type

#numpy float

variance = np.var(marks)

print(variance)



#np.argmin()

#definition

#returns the index(position) of the smallest element

#important note

#it returns the index not the value

#syntax

#np.argmin(array)

#return type

#numpy integer

minimum_index = np.argmin(marks)

print(minimum_index)



print(marks[minimum_index])



#np.argmax()

#definition

#returns the index(position) of the largest element

#it returns the index not the value

#syntax

#np.argmax(array)

#return type

#numpy integer

maximum_index = np.argmax(marks)

print(maximum_index)



print(marks[maximum_index])



#np.percentile()

#definition

#returns the value below which a given percentage of observations fall

#common percentiles

#25th percentile

#50th percentile (median)

#75th percentile

#90th percentile

#uses

#exam analysis

#salary analysis

#business reports

#customer analytics

#syntax

#np.percentile(array, percentage)

#return type

#numpy float

percentile_25 = np.percentile(marks,25)

print(percentile_25)



percentile_50 = np.percentile(marks,50)

print(percentile_50)



percentile_75 = np.percentile(marks,75)

print(percentile_75)



#real world example

#monthly sales

sales = np.array([45000,52000,61000,48000,70000,68000,56000])

print("Average Sales :", np.mean(sales))

print("Median Sales :", np.median(sales))

print("Standard Deviation :", np.std(sales))

print("Variance :", np.var(sales))

print("Highest Sale :", np.max(sales))

print("Lowest Sale :", np.min(sales))

print("Highest Sale Index :", np.argmax(sales))

print("Lowest Sale Index :", np.argmin(sales))

print("75th Percentile :", np.percentile(sales,75))



#important interview points

#mean is affected by outliers

#median is less affected by outliers

#standard deviation measures spread

#variance is the square of standard deviation

#argmin returns the index of the smallest value

#argmax returns the index of the largest value

#percentile tells how data is distributed
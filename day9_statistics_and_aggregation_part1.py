#importing numpy library

import numpy as np


#creating a numpy array

#suppose these are marks obtained by students

marks = np.array([85, 92, 76, 88, 95, 67, 81])

print(marks)



#Aggregation Functions

#definition

#aggregation functions combine multiple values into a single value

#instead of returning many values they return one summarized result

#uses

#used in

#data analysis

#report generation

#business intelligence

#machine learning

#finding summary statistics

#most commonly used aggregation functions

#sum()

#mean()

#min()

#max()



#np.sum()

#definition

#sum() calculates the total of all elements in the array

#syntax

#np.sum(array)

#return type

#numpy integer or float depending on the array

total_marks = np.sum(marks)

print(total_marks)



#real world example

#finding total monthly sales

sales = np.array([25000,30000,28000,35000])

total_sales = np.sum(sales)

print(total_sales)



#np.mean()

#definition

#mean() calculates the average value

#formula

#sum of all values divided by total number of values

#syntax

#np.mean(array)

#return type

#numpy float

average_marks = np.mean(marks)

print(average_marks)



#real world example

#average monthly temperature

temperature = np.array([32,35,30,34,31])

average_temperature = np.mean(temperature)

print(average_temperature)



#np.min()

#definition

#returns the smallest value in the array

#syntax

#np.min(array)

#return type

#same data type as the array

lowest_marks = np.min(marks)

print(lowest_marks)



#real world example

#lowest salary

salary = np.array([25000,30000,45000,55000])

lowest_salary = np.min(salary)

print(lowest_salary)



#np.max()

#definition

#returns the largest value in the array

#syntax

#np.max(array)

#return type

#same data type as the array

highest_marks = np.max(marks)

print(highest_marks)



#real world example

#highest product price

prices = np.array([1200,1500,950,2000])

highest_price = np.max(prices)

print(highest_price)



#multiple aggregation functions together

print("Total Marks :", np.sum(marks))

print("Average Marks :", np.mean(marks))

print("Minimum Marks :", np.min(marks))

print("Maximum Marks :", np.max(marks))



#important interview points

#sum() returns the total

#mean() returns the average

#min() returns the smallest value

#max() returns the largest value

#aggregation functions summarize data into one value
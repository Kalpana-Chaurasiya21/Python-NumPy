#importing numpy library

import numpy as np


#Boolean Masking

#definition

#boolean masking is used to filter elements from an array

#based on one or more conditions

#it returns only those values for which the condition is True

#uses

#filtering students who passed

#finding high salary employees

#finding products with low stock

#cleaning datasets

#data analysis



#creating a numpy array

marks = np.array([45,67,89,92,55,76,38,99])

print(marks)



#greater than (>)

#definition

#returns True for values greater than the given number

mask = marks > 70

print(mask)

print(marks[mask])



#less than (<)

#definition

#returns True for values less than the given number

mask = marks < 60

print(mask)

print(marks[mask])



#greater than or equal to (>=)

mask = marks >= 90

print(mask)

print(marks[mask])



#less than or equal to (<=)

mask = marks <= 50

print(mask)

print(marks[mask])



#equal to (==)

mask = marks == 76

print(mask)

print(marks[mask])



#not equal to (!=)

mask = marks != 76

print(mask)

print(marks[mask])



#multiple conditions using &

#definition

#& means logical AND

#both conditions must be True

mask = (marks >= 60) & (marks <= 90)

print(mask)

print(marks[mask])



#multiple conditions using |

#definition

#| means logical OR

#at least one condition must be True

mask = (marks < 40) | (marks > 90)

print(mask)

print(marks[mask])



#using ~

#definition

#~ means logical NOT

#it reverses True to False and False to True

mask = ~(marks > 70)

print(mask)

print(marks[mask])



#real world example

#employee salaries

salary = np.array([25000,32000,41000,18000,55000,27000])



#employees earning more than 30000

high_salary = salary > 30000

print(salary[high_salary])



#employees earning between 25000 and 50000

middle_salary = (salary >= 25000) & (salary <= 50000)

print(salary[middle_salary])



#employees earning less than 25000

low_salary = salary < 25000

print(salary[low_salary])



#filtering strings

cities = np.array(["Delhi","Mumbai","Pune","Delhi","Chennai"])



#finding Delhi

print(cities[cities == "Delhi"])



#important interview points

#boolean masking returns only matching elements

#comparison operators create boolean arrays

#& means logical AND

#| means logical OR

#~ means logical NOT

#always use parentheses with multiple conditions

#do not use python's and or not with numpy arrays
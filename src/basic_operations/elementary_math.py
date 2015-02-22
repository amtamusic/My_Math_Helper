import math
def add(first_number,second_number):
    return first_number+second_number

def subtract(first_number,second_number):
    return first_number-second_number

def multiply(first_number,second_number):
    return first_number*second_number

def divide(first_number,second_number):
    return first_number/second_number
'''
Input

1 cookie = 1 dollar 
7 cookies = ?

Output

?=7 dollars
'''
def unitaryMethod(unit1,unit1_value,unit2):
    return (unit1_value*unit2)/unit1
'''
Sum of all elements in a number array divided by the array length
'''
def average(numbers):
    return sum(numbers)/len(numbers)
'''
Highest Common Factor

All factors of 4 : 1,2,4
All factors of 6 : 1,2,3,6
Al factors of 12 : 1,2,3,4,6,12

Common factors = 1,2
HCF=2
'''
def HCF(numbers):
    factors=[]
    for number in numbers:
        factors.append(find_factors(number))
    hcf=factors[0]
    for i in range(1,len(factors)):
        hcf=list(set(hcf).intersection(factors[i]))
    return max(hcf)

def find_factors(number):
    factors=[]
    for possible_factor in range(1,number+1):
        if number%possible_factor==0:
            factors.append(possible_factor)
    return factors
'''
Lowest Common Multiple
'''
def LCM(numbers):
    lcm=numbers[0]
    for number in numbers:
        temp=[lcm,number]
        lcm=(lcm*number)/HCF(temp)
    return lcm
'''
find the percentage of units relative to the sample space
'''
def percentage(units,total_units):
    return units/total_units

def inv_percentage(percentage,total_units):
    return(percentage*100/100)*total_units

def area_square(side):
    return side*side

def perimeter_square(side):
    return side*4

def perimeter_rectangle(side1,side2):
    return (side1*2) + (side2*2)

def area_triangle(base,height):
    return (base*height)/2

print add(3,23)
print subtract(5,89)
print multiply(16,23)
print divide(12.0,3.2)
print unitaryMethod(10,30,8)
print average([2,2,2,2,2,2,2,2,2,2,2])
print HCF([18,24,35])
print find_factors(35)
print LCM([18,24,27])
print percentage(2.0,4.0)
print inv_percentage(0.75,4.0)
print area_square(23)
print perimeter_square(2)
print perimeter_rectangle(12,15)
print area_triangle(12,5)



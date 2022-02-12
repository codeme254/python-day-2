#python primitive data types
#data types: strings,integers, floats, booleans

#string
print("hello"[0])#subscripting, pulling out a particular letter from a string
print("hello"[4])
#"123" is not a number, it is a string
print("123"+"345")#concatenation of strings

#integer-whole numbers with no decimal places
#write the number without anything else
print(123+345)
#large integers with comma in between, put underscores
print(123_345)

#floats-decimal places eg 3.14159
#decimal points float around a number
print(3.158)
#boolean-- True or False in python
#to know the data type, we use the type() operator
print(type(33)) #<class 'int'>
#coding exercise
#random two digit number, adding first digit to a second digit and end up with a numerical result eg, 39 will print 12, 26 is 8
number= input("Enter a two digit number: ")
summation = int(number[0]) + int(number[1])#performing type conversion to int
print(summation)

#other mathematical operators in python
print(3+5) # addition
print(7-4) # subraction
print(3*2) # multiplication
print(6/3) # division---division always produces float result
print(2**2)# exponent, x to the power of y
#order of operation for the operators
#PEMDAS|LR parentheses, exponent, mult, division, addition, subtraction performed from left to right

#BMI CALCULATOR, ,ask for height, weight,  bmi = weight over height squared, bmi result in whole number
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = float(weight)/float(height)**2
print(f"Your BMI is: {int(bmi)}")

print(round(8/3))#rounding a number in python
print(round(8/3, 2))#rounding a number in python to 2dp
print(8//3)#flow division produces an integer afterwards

result = 4/2
result /= 2 #result = result/2, same in *, +, -
#fstrings
print("Your score is" +str(result))
print(f"Your score is: {result}")

#coding challenge, your life in weeks
#assuming lifespan is 90 years old
# 365 days in a year, 52 weeks in a year and 12 months
age = int(input("What is your current age: "))
remaining_years = 90 - age
remaining_weeks = remaining_years * 52
remaining_months = remaining_years * 12
remaining_days = remaining_years * 365
print(f"You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months}")

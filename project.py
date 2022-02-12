#TIP CALCULATOR
#total bill
#percentage 10, 12, 15
#number of people to split
#calculate
#people 7, percentage 12, bill 124.56 each will pay 19.93, 2dp final bill
print("Welcome to tip calculator")
total_bill = float(input("What was the total bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, 15?  "))
number_of_people = int(input("How many people to split the bill? "))
bill_with_tip = round(total_bill *(1+percentage/100), 2)
each_people_pay = round(bill_with_tip/number_of_people, 2)
print(f"Each person should pay {each_people_pay}")
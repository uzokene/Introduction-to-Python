# # Q1:Print a box like the one below.
******************* 
******************* 
******************* 
*******************

#  Input:
 for i in range (4):
    print('*'* 19)
# OR
# Print('*' *19)
# Print('*' *19)
# Print('*' *19)
# Print('*' *19)

# # Q2:Print a box like the one below.
#******************* 
#* *             * * 
#*******************

# # Input:
# for i in range (2):
# 	print('*'* 19)
# 	print('*'* 2)

# # Q3:Print a triangle like the one below.
#* 
#** 
#*** 
#****

# # Input:
# for i in range (4):
# 	print('*'* (i +1))

# # Q4:Write a program that computes and prints the result of
# #512−282 /47·48+5
#It is roughly .1017.

# # Input:
# num = 512 – 282
# den = 47*48 + 5
# result = num /den
# result = round (result, 4)
# print (result)

# # Output:
# 0.1017

# # Q5:Ask the user to enter a number. Print out the square of the number, but use the sep optional argument to print it out in a full sentence that ends in a period.
#  Sample output is shown below.
#Enter a number: 5 
#The square of 5 is 25

# # Input:
# num = eval(input(‘enter a number: ’))
# square = num **2
# print(‘ the square of ‘ , num `is’, square, ‘ ,sep= ` ‘)

# Q6: Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x, and 5x, 
# each separated by three dashes, like below.
# Enter a number: 7 
# 7---14---21---28---35

# Input:
# value=eval(input(‘enter a number:’))
# print(1*value,2*value,3*value,4*value,5*value,sep = ‘ - - - ‘)

# Output:
# enter a number:
# 7
# 7---14---21---28---35
# 
# Q7: Write a program that asks the user for a weight in kilograms and converts it to pounds.
#  There are 2.2 pounds in a kilogram.

# Input:
# kg = float(input('Enter weight in Kg to Convert into pounds:')) 
# pounds = kg * 2.2046 print(kg,' Kilograms =', pounds,' Pounds')
# Output:
# myfirst python script
# Enter weight in Kg to Convert into pounds:67
# 67.0  Kilograms = 147.7082  Pounds

# Q8:
# Write a program that asks the user to enter three numbers (use three separate input statements). 
# Create variables called total and average that hold the sum 
# and average of the three numbers and print out the values of total and averag
# Input:
#first = eval(input('First number: '))
#second = eval(input('Second number: '))
#third = eval(input('Third number: '))
#total = first + second + third
#average = total / 3
#print()
#print('*'*20)
#print('Total:', total)
#print('Average:', average)
#print('*'*20)
# value= eval(input(‘enter 3 number:’))
# total = eval(input(‘add 3 number:’))
# average = eval(input(‘average 3 number:’))
# print(‘values of total and average’)
# Output:
# enter 4 number: 123
# add 3 number: 6
# average 3 number: 36
# values of total and average

# # Q9: A lot of cellphones have tipcalculators. Writeone. Ask the user for the price of the meal and the percent tip they want to leave.
#  Then print both the tip amount and the total bill with the tip included.
# # Input:

# meal_price = eval(input('How much is your meal(USD)? '))
# percent_tip = eval(input('How much percentage tip do you want to leave(%)? '))

# # computation

# tip_amount = meal_price * percent_tip / 100
# total_bill = meal_price + tip_amount

# # output
# print('Tip amount for', str(percent_tip) + '%', 'tip is', '$' + str(tip_amount))
# print('Total bill is',  '$' + str(total_bill))









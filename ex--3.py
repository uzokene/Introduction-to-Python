#Q1. Write a program that generates and prints 50 random integers, each between 3 and 6.
#Input
#from random import randint
#for i in range(1,50):
    #x = randint(3,6)
    #print('A random number between 3 and 6: ', x)

#Q2. Write a program that generates a random number, x, between 1 and 50, a random number y between 2 and 5,
    #and computes xy.
#Input:
#from random import randint
#for i in range(1,5):
    #x = randint(1,50)
    #y= randint(2,5)
    #z = pow(x,y)
    #print('x - A random number between 1 and 50: ', x)
    #print('y - A random number between 2 and 5: ', y)
    #print('z - : ', z)

#Q3. Write a program that generates a random number between 1 and 10 and prints your name that many times.
#Input:
#from random import randint
#x = randint(1,10)
#print ('x',x)
#for i in range(1,x):
      #print('My name is Amaka')

#Q4. Write a  program that generates a random decimal number between 1 and 10 with two decimal places of accuracy.
 #Examples are 1.23, 3.45, 9.80, and 5.00.
#Input:
#from random import randint
#for i in range(1,5):
    #x = randint(100,1000)
    #x =x/100
    #print ('x',x)

#Q5. Write a program that generates 50 random numbers such that the first number is between 1 and2,the 
#second is between 1and 3,the third is between 1 and 4,...,and the last is between 1 and 51. 

#Input:
#from random import randint
#x =2
#for i in range(0,50):
   # y = randint(1,x)
    #x = x + 1
    #print('Generated random number is ', y)

#Q6. Write a program that asks the user to enter two numbers, x and y, and computes |x−y| / x+y . 

#Input:
#x = eval(input("enter the value of x :"))
#y = eval(input("enter the value of y :"))
#z = (x - y)/(x + y)
#print ("result is" , z)

#Q7. Write a program that asks the user to enter an angle between −180◦ and 180◦. 
#Using an expression with the modulo operator, convert the angle to its equivalent between 0◦ and 360◦.

#Input:
#angle =eval(input("enter a value b/w -180 and 180:"))
#result =(angle + 360)% 360
#print("angle in range 0 + 360:;result")

#Q8. Write a program that asks the user for a  number of seconds and prints out how many minutes and seconds that is. 
#For instance, 200 seconds is 3 minutes and 20 seconds. 
#[Hint: Use the // operator to get minutes and the % operator to get seconds.]

#Input:
#x=eval(input('enter the number of seconds'))
#y=(x//60)
#z=(x%60)
#print('the number of minutes is', y)
#print('the number of seconds is', z)

#Q9. Write a program that asks the user for an hour between 1 and 12 and for how many hours in the future they 
#want to go. Print out what the hour will be that many hours into the future. An example is shown below.
#Enter hour: 8 
#How many hours ahead? 
#5 New hour: 1 o'clock

#Input:
#x=eval(input('enter the number of hours'))
#y=eval(input('how many hours ahead'))
#z=(x + y)
#v=z % 12
#print('the time is', v,'o clock')

#Q10.(a) One way to find out the last digit of a number is to mod the number by 10. Write a program that asks the user to enter a power. 
# Then find the last digit of 2 raised to that power. 
#(b) One way to find out the last two digits of a number is to mod the number by 100. 
# Write a program that asks the user to enter a power. Then find the last two digits of 2 raised to that power.
#(c) Write a program that asks the user to enter a power and how many digits they want. 
#Find the last that many digits of 2 raised to the power the user entered.
#Input:







#Q11. Write a program that asks the user to enter a weight in kilograms. The program should convert it to pounds, printing the answer rounded to the nearest tenth of a pound.
#Input:
#kg = eval(input('Enter weight in Kg to Convert into pounds:')) 
#pounds = kg * 2.2046 
#(kg,' Kilograms =', pounds,' Pounds')

#Q12. Write a program that asks the user for a number and prints out the factorial of that number
#Input:
#num = eval(input("Enter a number:"))
#fac =num**2
#print("the factorial of the number is", fac,)

#Q13.Write a program that asks the user for a number and then prints out the sine, cosine, and tangent of that number.
#Input:
#num = eval(input("Enter a number:"))
#from math import sin,cos,tan
#sine=sin(num)
#cosine= cos(num)
#tan =tan(num)
#print("The sine of number is",sine,)
#print("The cosine of number is",cosine,)
#print("The tan of number is",tan,)

#Q14. Write a program that asks the user to enter an angle in degrees and prints out the sine of that angle.
#Input:
#angle=eval(input("Enter an angle"))
#from math import radians,sin
#angle =radians(angle)
#sine= sin(angle)
#print=("The sine of angle is", sine,)

#Q15. Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦ in 15◦ increments. Each result should be rounded to 4 decimal places. Sample output is shown below:
#0 --- 0.0 1.0 
#15 --- 0.2588 0.9659 
#30 --- 0.5 0.866
# ... 
#345--- -0.2588 0.9659

#Input:
for i in range(1,345):
    from math import radians,sin,cos 
    sine=sin(i)
    cosine= cos(i)
    x= i + 15
    y= rounded up in 4 demical place
    print("The sine of y is",sine,)
    print("The cosine of y is",cosine,)


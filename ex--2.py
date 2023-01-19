#Q1. Write a program that prints your name 100 times.
#for i in range(1,101):
    #print('amaka')
    #print(i)

#Q2. Write a program to fill the screen horizontally and vertically with your name. 
#[Hint: add the option end='' into the print function to fill the screen horizontally.]
#input
#for i in range(24):
    #print('amaka'*10)
#OR
#for i in range(24):
    #print('amaka '*10)
    #print(i,end='')

#Q3.  Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. 
     #The output should look like the output below.
#1 Your name 
#2 Your name 
#3 Your name 
#4 Your name 
#... 
#100 Your name

#input
#for i in range(1,101):
    #print(i,'amaka')

#Q4. Write a program that prints out a list of the integers from 1 to 20 and their squares.
 #The output should look like this:
#1 --- 1 
#2 --- 4
#3 --- 9 
 #...
#20 --- 400

#input
#for i in range(1,21):
    #x=i**2
    #print(i,'---',x)
	#OR
#for i in range(1,21):
    #x=pow(i,2)
    #print(i,'---',x)

#Q5. Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, ..., 83, 86, 89.
#Input
#for i in range(1,101):
    #x=((i -1)*3)+ 8
    #print('x=',x)

 #Q6. Write a program that uses a for loop to print the numbers 100, 98, 96, ..., 4, 2.
 #input
#for i in range(1,101):
    #x=100-((i-1)*2)
    #print('x=',x)

 #Q7. Write a program that uses exactly four for loops to print the sequence of letters below.
      #AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
#Input
#for i in range(1):
    #s= (('A'*10)+('B'*7)+('CD'*4)+('E'*1)+('F'*6)+('G'*1))
    #print(s)

#Q8.Write a program that asks the user for their name and how many times to print it. 
   #The program should print out the user’s name the specified number of times.
#Input   
#userinput_name = str(input('Please enter your name:'))
#n = int(input('Please enter number of times you wish to print your name:')) 
#for i in range(1,n):
    #print(userinput_name)

#Q9.The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each number thereafter
   #is the sum of the two preceding numbers. Write a program that asks the user how many Fibonacci numbers to
   #print and then prints that many.
   #1,1,2,3,5,8,13,21,34,55,89..
#Input
#n = eval(input('Please specify how many numbers you want in the fibonacci series:')) 
#first=1
#second=1
#print(first,second,sep=" , ",end= " , ")
#for i in range(n-2):
    #third= first + second
    #print(third,end= " , ")
    #first=second
    #second=third

#Q10.Use afor loop to print a box like the one below. Allow the user to  specify  how wide and how high the box
      #should be. [Hint: print('*'*10) prints ten asterisks.]
#******************* 
#*******************
#******************* 
#*******************

#Input
#for i in range (4):
	#print("*" * 10)

 #Q11. Use a for loop to print a box like the on ebelow. Allow the user to specify how wide and how high the box should be.
 #******************* 
 #*                 *             
 #*                 * 
 #*******************
 #Input
#roww = eval(input("Enter Number of Rows:"))  
#coll = eval(input("Enter Number of Columns:"))  
#for i in range(1, roww+1):
    #for j in range(1, coll+1):
        #if (i == 1 or i == roww or
            #j == 1 or j == coll):
            #print("*", end="")           
        #else :
            #print(" ", end="")           
     
#Q12.Use a for loop to print a triangle like the one below. Allow the user to specify how high the triangle 
#*
#** 
#*** 
#****

#input
#for i in range (4):
	#print("*" * (i +1))

#Q13.Use a for loop to print an upside down triangle like the one below. Allow the user to specify how high the
    #triangle should be.
#**** 
#*** 
#** 
#*

#Input
#height = eval(input("how high do you want the triangle:"))
#for k in range (height,0,-1):
	#print (k* "*")

#Q14. Use for loops to print a diamond like the one below. Allow the user to specify how high the diamond should be.
   #* 
  #*** 
 #***** 
#******* 
 #*****
  #*** 
   #*

  #input
#h = eval(input("enter diamond's height:")) 
#for x in range(h):     
    #print(" " * (h - x), " * " * (2*x + 1)) 
#for x in range(h -2, -1, -1):     
    #print(" " * (h - x), " * " * (2*x + 1))

#Q15.Write a program that prints a giant letter A  like the one below. Allow the  user to specify
#how large the letter should be.
  #* 
#*   * 
#*****
#*   * 
#*   *

#input
height = eval(input("How high do you want the giant A to be?"))
print(" " * height, " * ", sep=" ")
for n in range (1,height):
        if n=height//2:
        print(" " * (height-n), " * ",(2*n-1)* " ", " * " , sep= " ")
        else:
            print(" " * (height - n), " * ",(2*n-1) * " * "," * ", sep=" ")
#write a program to display name, age, email, in three different lines.

'''Name = input("enter your name:")
Age = int(input("enter your age:"))
Email = input("enter your email:")
print("Student ID card")
print("name:", Name)
print("Age", Age)
print("Email:", Email)'''

#Write a program to solve two variable

'''a = 10
b = 20
print("number before swap:", a,b)
temp=a
a = b
b = temp
print("number after swap:", a,b)'''

#convert float into integer

'''a= 20
b = float(a)
print(b)
c=int(b)
print(c)'''

#write a program to check whether the number is positive

'''a= int(input("enter number:"))
if a>0:
    print("number is positive")
elif a==0:
    print("number is Zero")
else:
    print("number is negative")'''

#Write a program to check whether number is even or odd

'''a = int(input("enter the number:"))

if a%2 == 0:
    print("Number is Even")
else:
    print("Number is odd")'''

#Write a program to create Area calculator

'''l = int(input("enter length"))
h = int(input("enter height"))

print("Area of Square:" , l**2)
print("Area of Rectangle:" , l*h)
print("Area of Triangle" , .5*l*h)
print("Area of Circle", 3.14*l**2*h)'''

#Check whether the passed letter is vowel or not.

'''x = input("enter letter:")
if(x == 'a' or x == 'e' or x=='i' or x=='o' or x=='u'):
    print("letter is vowel")
else:
    print("letter is consonant")'''

#Write a program to sum all the even numbers from the range 1 to 50

'''Sum = 0
for i in range(0,51):
    if i%2 ==0:
        Sum += i
print(Sum)'''

#Write a program to write first 20 number and square of this number

'''num = 0
for i in range(1,21):
    num = i**2
    print(i,"=",num)'''


#write a program to find the sum of first 10 number.

'''Sum = 0
n=0
while n<=10:
    if n%2 != 0:
        Sum += n
    n += 1
print(Sum)'''

#Write a program to check whether the number os divisible by 8 and 12 in the range of 1 to 100

'''n= int(input("Enter the number here:"))
if n%8 == 0 and n%12 == 0:
    print("number is divisible by both the number")
else:
    print("not divisible")'''

#write a program to create billing system

'''Name= input("Enter the name Here:")
print("here is the customer biling:")
quantity = float(input("enter the quantity:"))
amount = float(input("enter the amount:"))
total = amount*quantity
print("here are the total bill:", total)
Repeat = input("Do you want to continue(yes/no):")
if Repeat == "NO" or Repeat == "no":
    print("-"*40)
    print("*"*30,"Happy shopping", "*"*30)
    print("-"*40)


else:
    Repeat1= input("Do ypu want to add new cx:")
    if Repeat == "no" or Repeat == "No":
        print("Happy Shopping")
    else:
        Name = input("Enter the name Here:")
        print("here is the customer biling:")
        quantity = float(input("enter the quantity:"))
        amount = float(input("enter the amount:"))
        total = amount * quantity
        print("here are the total bill:", total)'''

'''a= "Why fit in, When you are Born to stand out"

b= len(a)
print(b)

c=a.count("o")
print(c)

d=a.upper()
print(d)

e= a.title()
print(e)

f=a.find("fit in")
print(f)'''

#Pattern problem

'''for i in range(8,0,-1):
    for j in range(1,i-1):
        print("*",end=" ")
    print()'''

#strings problem

'''A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"

#1. Write a program to separate the following string into com separated values.

print(A.split("."))

#2. Write a program to sort strings alphabetically in python.
print(sorted(A))
#3. Write a program to remove a given character from a string.
print(A.replace(".",""))
Z = "F.R.I.E.N.D.S."
#4. Write a program to remove dot(.) from the following string.

print(Z.replace(".",""))
#5. Write a program to check the number of occurrence of A

print(Z.count("."))'''

#Take a user input from user as a string then, reverse it.

'''a= "hello world"
temp=a[::-1]
print(temp)

#write a program to check if a string contains only digits

a="tabu4022"
b=a.isdigit()
if b == True:
    print("it contains only digit")
else:
    print("it does not contain digit")

#check whether given string is palindrom or not

a= input("enter the string:")
b=a[::-1]
if a == b:
    print("string is a palindrome")
else:
    print("not palindrome")

#find no. of vowels in a string

a= input("enter the string:")
vowels=0
for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        vowels += 1
print("the no. of vowels are : ",vowels)

#check the every letter start with capital

a= input("enter the string:")
print(a.istitle())'''




#





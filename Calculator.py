#!/usr/bin/env python
# coding: utf-8

# In[6]:


def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        print("Couldnot divide by 0")
    else:
        return x/y

print("------------Select Operation---------------")
print("1. Addition of Two Numbers:")
print("2. Subtraction of Two Numbers:")
print("3. Multiplication of Two Numbers:")
print("4. Division of Two Numbers:")

choice = input("Enter your Operation:(1/2/3/4):")

num1 = float(input("Enter First Number:"))
num2 = float(input("Enter Second Number:"))

if choice == "1":
    print("The Result is:" , add(num1,num2))
    
elif choice == "2":
    print("The Result is:" , subtract(num1,num2))
    
elif choice == "3":
    print("The Result is:" , multiply(num1,num2))

elif choice == "4":
    print("The Result is:" , divide(num1,num2))

else:
    print("Invalid operation")
    


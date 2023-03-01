#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Write a python program to print the sum and product of the first 10 natural numbers using for and while loop

sum=0
p=1
for i in range(1,10):
    sum=sum+i
    p=p*i
print(sum)
print(p)


# In[1]:


#The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
#unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
#be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.

units=int(input("Enter the units - "))
if (units<=100):
    charges=4.5*units
elif (units>100 and units<=200):
    charges=6*units
elif (units>200 and units<=300):
    charges=10*units
else:
    charges=20*units

print("charges- ",charges)


# In[2]:


#Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
#number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
#that list.

l=[]
for i in range(1,100):
    c=i*i*i
    if(c%4==0 or c%5==0):
        l.append(c)
        j =0
    
while(j<len(l)):
    print(l[j])
    j=j+1


# In[10]:


#Write a program to filter count vowels in the below-given string. string = "I want to become a data scientist"

str="I want to become a data scientist"
count=0
vowel=["a", "e", "i", "o", "u"]
for i in str:
    if i in vowel:
        count=count+1

print("No. of vowels - ",count)


# In[ ]:





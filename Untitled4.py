#!/usr/bin/env python
# coding: utf-8

# In[5]:


numbers = int(input("How many terms?"))
n1 , n2 = 0, 1
count = 0 
if numbers <= 0: 
        print ("Please enter a positive integer:");
elif numbers == 1 :
    print ("Fibbonacci sequence upto" , numbers , ":");
    print (n1);
else:
    print ("Fibbonacci sequence: ");
    while count < numbers:
        print (n1);
        n = n1 + n2 
        n1 = n2
        n2 = n 
        count += 1
    


# In[ ]:





# In[ ]:





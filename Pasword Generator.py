#!/usr/bin/env python
# coding: utf-8

# In[9]:


import string
import random

if __name__ == "__main__":
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    
    length = int(input("Enter Password Length:"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    random.shuffle(s)
             
    print("".join(s[0:length]))


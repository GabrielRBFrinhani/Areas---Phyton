#!/usr/bin/env python
# coding: utf-8

# # if, elif, else

# In[5]:


print("Qual a temperatura hoje?")
temp = float(input())

if temp > 30:
    print("Está quente.")


# In[10]:


print("Qual a temperatura hoje?")
temp = float(input())

if temp > 30:
    print("Está quente.")
    
elif temp > 0 and temp < 20:
    print("Está normal.")
    
else:
    print("Está frio.")
    


# # Range

# In[11]:


list(range(10))


# In[12]:


# For
for i in range(10):
    print(i)


# In[13]:


# Verificador de números pares

for i in range(100):
    if i % 2 == 0:
        print("Número {} é par".format(i))


# In[14]:


# While

x = 0
while x < 10:
    print("O valor de x é: {}".format(x))
    x = x+1


# In[15]:


# Funções
def soma_numeros(x,y):
    return x + y
soma_numeros(6,9)


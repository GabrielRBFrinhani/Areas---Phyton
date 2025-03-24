#!/usr/bin/env python
# coding: utf-8

# ## 4.

# In[16]:


pessoa = {"nome":"Carlos", "idade":30,"cidade":"São Paulo"}
pessoa


# In[19]:


pessoa['nome']


# In[23]:


pessoa['idade'] = 31
pessoa['profissão'] = 'engenheiro'
pessoa


# In[35]:


pessoa.pop('cidade',None)
pessoa


# In[36]:


pessoa.keys()


# In[37]:


pessoa.values()


# ## 5.

# In[40]:


cores = ("vermelho", "azul", "verde", "amarelo", "roxo")
print("Tupla cores:", cores)


# In[41]:


print("Segundo item da tupla cores:", cores[1])


# In[42]:


print("A cor 'azul' está na tupla cores?", "azul" in cores)


# In[44]:


numeros = (1, 2, 3, 4, 5)
print("Soma dos elementos da tupla numeros:", sum(numeros))


# In[45]:


try:
    cores[2] = "laranja"  # Isso vai gerar um erro
except TypeError as e:
    print("Erro ao tentar alterar um valor na tupla:", e)


# In[47]:


nova_cores = cores + ("preto", "branco")

print("Nova tupla com cores concatenadas:", nova_cores)


# ## 9.

# In[ ]:


print


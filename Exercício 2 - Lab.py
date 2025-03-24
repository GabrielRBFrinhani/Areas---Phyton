#!/usr/bin/env python
# coding: utf-8

# ### 1. Criar variáveis de nome, iade e altura e printar tudo. 

# In[7]:


#Variável nome

nome = 'Gabriel'

#Variável idade

idade = '22'

#Variável altura

altura = '1,74'

#Printar frase

print(f'Meu nome é {nome}, tenho {idade} anos e minha altura é {altura} metros')


# ### 2. Criar variável frase e realizar alterações nela.

# In[13]:


#Variável frase

frase = 'Python é uma linguagem de programação muito poderosa.'


# In[14]:


#Transformar frase em maiúsculo

frase.upper()


# In[15]:


#Tranformar frase em minúsculo

frase.lower()


# In[17]:


#Mudar palavra da frase

frase.replace("muito","extremamente")


# In[18]:


#Separar frase por palavras

frase.split()


# ### 3. Criar lista de elementos e realizar alterações

# In[24]:


#Criando lista com frutas

listafrutas = ["maçã","banana","laranja","uva","abacaxi"]
listafrutas


# In[26]:


#Adicionando fruta a lista

listafrutas.append("manga")
listafrutas


# In[27]:


#Retirando fruta da lista

listafrutas.remove("laranja")
listafrutas


# In[32]:


#Acessando item

terceira_fruta = listafrutas[2]
terceira_fruta


# In[33]:


#Ordem alfabética

listafrutas.sort()
listafrutas


# In[36]:


#Somatório de números de um conjunto

números = [10,5,8,3,6]
somatório = sum(números)
somatório


# ### 6. IMC

# In[49]:


#Recebendo altura

print("Digite sua altura")
altura = float(input())


# In[63]:


#Recebendo peso

print("Digite seu peso")
peso = float(input())


# In[64]:


#Fazendo cálculo de IMC

imc = peso / (altura ** 2)
imc


# ### 7. Cumprimento

# In[67]:


#Recebendo nome completo

print("Olá, me diga seu nome completo.")
nome = input()


# In[77]:


#Cumprimento com o primeiro nome

primeiro_nome = nome.split()[0]
print(primeiro_nome)


# ### 8. Extraindo domínio de um email

# In[78]:


print("Digite seu email:")
email = input()


# In[83]:


#Retornando domínio

domínio = email.split('@')[1]
print(f"O domínio do email é: {domínio}")


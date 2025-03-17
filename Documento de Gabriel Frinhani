#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Rel = pd.read_csv("C:/Users/20211enpro0394/Downloads/areas.csv", sep = ";", decimal = ",")
Rel


# In[3]:


len(Rel)


# In[6]:


Rel['Bloco'].value_counts()


# In[7]:


Rel['Andar'].value_counts()


# In[8]:


Rel['Total M2'] = Rel['Sala']+Rel['Cozinha']+Rel['Banheiro']+Rel['Dorm']
Rel


# In[3]:


import matplotlib.pyplot as plt


# In[14]:


plt.hist(Rel['Banheiro'], bins = 8, edgecolor = "black")
plt.title("Distribuição banheiros por apartamento")
plt.xlabel("Metros quadrados do banheiro")
plt.ylabel("N° de Apartamentos")


# In[17]:


plt.hist(Rel['Sala'], bins = 8, edgecolor = "black")
plt.title("Distribuição sala por apartamento")
plt.xlabel("Metros quadrados do Sala")
plt.ylabel("N° de Apartamentos")


# In[18]:


plt.hist(Rel['Cozinha'], bins = 8, edgecolor = "black")
plt.title("Distribuição cozinha por apartamento")
plt.xlabel("Metros quadrados do Cozinha")
plt.ylabel("N° de Apartamentos")


# In[19]:


plt.hist(Rel['Dorm'], bins = 8, edgecolor = "black")
plt.title("Distribuição Dormitório por apartamento")
plt.xlabel("Metros quadrados do Dormitório")
plt.ylabel("N° de Apartamentos")


# In[20]:


plt.hist(Rel['Total M2'], bins = 8, edgecolor = "black")
plt.title("Distribuição área útil por apartamento")
plt.xlabel("Metros quadrados do área útil")
plt.ylabel("N° de Apartamentos")


# In[23]:


Rel.groupby(['Bloco'])['Sala'].mean()


# In[24]:


Rel.groupby(['Bloco'])['Banheiro'].mean()


# In[25]:


Rel.groupby(['Bloco'])['Cozinha'].mean()


# In[26]:


Rel.groupby(['Bloco'])['Dorm'].mean()


# In[27]:


Rel.groupby(['Bloco'])['Total M2'].mean()


# In[28]:


Rel.groupby(['Bloco'])['Sala'].std()


# In[29]:


Rel.groupby(['Bloco'])['Banheiro'].std()


# In[30]:


Rel.groupby(['Bloco'])['Cozinha'].std()


# In[31]:


Rel.groupby(['Bloco'])['Dorm'].std()


# In[32]:


Rel.groupby(['Bloco'])['Total M2'].std()


# In[4]:


import seaborn as sns


# In[35]:


sns.boxplot(x = "Bloco", y = "Sala", data = Rel)


# In[36]:


sns.boxplot(x = "Bloco", y = "Cozinha", data = Rel)


# In[37]:


sns.boxplot(x = "Bloco", y = "Banheiro", data = Rel)


# In[41]:


sns.boxplot(x = "Bloco", y = "Dorm", data = Rel)


# In[42]:


sns.boxplot(x = "Bloco", y = "Total M2", data = Rel)


# ## Sim, existe diferença entre os dois blocos. O cômodo sala apresenta o problema

# In[44]:


tabela_infiltração = Rel['Infiltr'].value_counts()
plt.barh(tabela_infiltração.index, tabela_infiltração.values, color = "#845EC2")
plt.title("Distribuição de infiltrações por apartamento")
plt.xlabel("N° de apartamentos")
plt.ylabel("Infilração")


# In[46]:


tabela_rachaduras = Rel['Rachadura'].value_counts()
plt.barh(tabela_rachaduras.index, tabela_rachaduras.values, color = "#845EC2")
plt.title("Distribuição de rachaduras por apartamento")
plt.xlabel("N° de apartamentos")
plt.ylabel("Rachaduras")


# In[47]:


tabela_rachadura_infiltrações = pd.crosstab(Rel['Rachadura'], Rel['Infiltr'])
tabela_rachadura_infiltrações


# In[6]:


Rel['Alt Andar'] = ['alto' if x > 9 else 'baixo' for x in Rel['Andar']]
Rel


# In[8]:


tabela_rachadura_Andar = pd.crosstab(Rel['Rachadura'], Rel['Alt Andar'])
tabela_rachadura_Andar


# In[9]:


tabela_infiltração_Andar = pd.crosstab(Rel['Infiltr'], Rel['Alt Andar'])
tabela_infiltração_Andar


# In[12]:


tabela_infiltração_Andar.plot(kind='bar', figsize=(10,6), colormap='viridis')
plt.xlabel('Infiltração')
plt.ylabel('Frequência')
plt.title('Distribuição de Infiltração por Andar')
plt.legend(title='Andar')
plt.show()


# In[14]:


tabela_rachadura_Andar.plot(kind='bar', figsize=(10,6), colormap='viridis')
plt.xlabel('Rachadura')
plt.ylabel('Frequência')
plt.title('Distribuição de Infiltração por Andar')
plt.legend(title='Andar')
plt.show()


# ### As infiltrações estão mais presentes nos andares altos. Já as rachaduras estão bem presentes em andares altos e baixos

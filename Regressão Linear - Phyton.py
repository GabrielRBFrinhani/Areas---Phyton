#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Importando pacotes

import pandas as pd # para importar .csv
import matplotlib.pyplot as plt # para gráficos
import seaborn as sns # para gráficos
from sklearn.linear_model import LinearRegression # para regresão linear
from sklearn.metrics import r2_score # para R²


# In[8]:


# Importando dados

dados = pd.read_csv("C:/Users/20211enpro0394/Downloads/Salary_Data.csv")
dados


# In[13]:


# (i) Diagrama de Dispersão

plt.scatter(dados['YearsExperience'], dados['Salary'], color = 'lightcoral')
plt.title('Salário ($) anual vs. Experiência')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário ($) Anual')


# In[15]:


# Separação de X e Y

X = dados.iloc[:,:1] # variável independente
Y = dados.iloc[:,1:] # variável dependente


# In[17]:


# (ii) Ajuste de modelo (Encontrar beta_0 e beta_1 que minimizam)

modelo = LinearRegression()
modelo.fit(X,Y)


# In[18]:


print('Coeficiente angular (beta_1):', modelo.coef_)
print('Intercepto (beta_0):',modelo.intercept_)


# In[19]:


# Fazendo predições para Y usando X

y_pred = modelo.predict(X)


# In[20]:


plt.scatter(dados['YearsExperience'], dados['Salary'], color = 'lightcoral')
plt.plot(X,y_pred, color = 'firebrick')
plt.title('Salário ($) anual vs. Experiência')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário ($) Anual')


# In[22]:


# (iii) Verificação do coeficiente de determinação (R²)

r2_score(Y,y_pred)


# In[27]:


# A pesssoa com 6 anos de experiência ganha quanto?

import numpy as np

X_novo = np.array([[6]])
modelo.predict(X_novo)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando pacotes

import pandas as pd # para importar .csv
import matplotlib.pyplot as plt # para gráficos
import seaborn as sns # para gráficos
from sklearn.linear_model import LinearRegression # para regresão linear
from sklearn.metrics import r2_score # para R²


# In[2]:


# Importando dados

dados = pd.read_csv("C:/Users/20211enpro0394/Downloads/score_updated.csv")
dados


# In[3]:


# (i) Diagrama de Dispersão

plt.scatter(dados['Hours'], dados['Scores'], color = 'lightcoral')
plt.title('Horas de estudo vs. Nota')
plt.xlabel('Horas de Estudo')
plt.ylabel('Nota')


# In[4]:


# Separação de X e Y

X = dados.iloc[:,:1] # variável independente
Y = dados.iloc[:,1:] # variável dependente


# In[5]:


# (ii) Ajuste de modelo (Encontrar beta_0 e beta_1 que minimizam)

modelo = LinearRegression()
modelo.fit(X,Y)


# In[6]:


print('Coeficiente angular (beta_1):', modelo.coef_)
print('Intercepto (beta_0):',modelo.intercept_)


# In[7]:


# Fazendo predições para Y usando X

y_pred = modelo.predict(X)


# In[8]:


plt.scatter(dados['Hours'], dados['Scores'], color = 'lightcoral')
plt.plot(X,y_pred, color = 'firebrick')
plt.title('Horas de estudo vs. Nota')
plt.xlabel('Horas de Estudo')
plt.ylabel('Nota')


# In[9]:


# (iii) Verificação do coeficiente de determinação (R²)

r2_score(Y,y_pred)


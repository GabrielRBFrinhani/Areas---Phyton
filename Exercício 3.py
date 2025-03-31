#!/usr/bin/env python
# coding: utf-8

# ### Exercício 1
# #### Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# 
# #### A mensagem "Aprovado", se a média alcançada for maior ou igual a 7;
# #### A mensagem "Reprovado", se a média for menor do que 7;
# #### A mensagem "Aprovado com Distinção", se a média for igual a 10.

# In[2]:


print("Nota parcial n° 1")
nota1 = float(input())
print("Nota parcial n° 2")
nota2 = float(input())


# In[6]:


média = (nota1 + nota2)/2
if média >= 7 and média < 10:
    print("Aprovado")
elif média == 10:
    print("Aprovado com distinção")
else:
    print("Reprovado")


# ### Exercício 2
# 
# #### Escreva um script que leia três números e mostre o maior e o menor deles.

# In[7]:


print("Primeiro número:")
primeiro = float(input())
print("Segundo número:")
segundo = float(input())
print("Terceiro número:")
terceiro = float(input())


# In[10]:


maior = max(primeiro,segundo,terceiro)
menor = min(primeiro,segundo,terceiro)

print("O maior número é:", maior)
print("O menor número é:", menor)


# ### Exercício 3
# 
# #### Nome na vertical em escada.
# 
# #### F
# #### FU
# #### FUL
# #### FULA
# #### FULAN
# #### FULANO

# In[11]:


nome = "FULANO"

for i in range(1, len(nome) + 1):
    print(nome[:i])


# ### Exercício 4
# 
# #### A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... (o próximo termo, a partir do terceiro, é sempre gerado a partir do somatório dos últimos dois). Faça um programa capaz de gerar a série até o n−ésimo termo (onde o valor n deve ser inserido pelo usuário).

# In[14]:


n = int(input("Digite o número da série"))

fibonacci = [1, 1]

for i in range(2, n):
    proximo_termo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo_termo)
print("A série de Fibonacci até o {}-ésimo termo é:".format(n))
print(fibonacci[:n])


# ### Exercício 5
# 
# #### Faça um programa que leia e valide as seguintes informações:
# 
# #### Nome: maior que 3 caracteres;
# #### Idade: entre 0 e 150;
# #### Salário: maior que zero;
# #### Sexo: 'f' ou 'm';
# #### Estado Civil: 's', 'c', 'v', 'd';

# In[15]:


# Função para validar os dados do usuário
def valida_dados():
    # Validação do nome
    while True:
        nome = input("Digite o seu nome: ")
        if len(nome) > 3:
            break
        else:
            print("Erro: O nome deve ter mais de 3 caracteres.")

    # Validação da idade
    while True:
        try:
            idade = int(input("Digite a sua idade: "))
            if 0 <= idade <= 150:
                break
            else:
                print("Erro: A idade deve estar entre 0 e 150.")
        except ValueError:
            print("Erro: Insira um número inteiro válido.")

    # Validação do salário
    while True:
        try:
            salario = float(input("Digite o seu salário: "))
            if salario > 0:
                break
            else:
                print("Erro: O salário deve ser maior que zero.")
        except ValueError:
            print("Erro: Insira um valor numérico válido.")

    # Validação do sexo
    while True:
        sexo = input("Digite o seu sexo (f/m): ").lower()
        if sexo in ['f', 'm']:
            break
        else:
            print("Erro: O sexo deve ser 'f' ou 'm'.")

    # Validação do estado civil
    while True:
        estado_civil = input("Digite o seu estado civil (s/c/v/d): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            break
        else:
            print("Erro: O estado civil deve ser 's', 'c', 'v' ou 'd'.")

    # Exibição dos dados validados
    print("\nDados validados com sucesso:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado_civil}")

# Chamada da função
valida_dados()


# ### Exercício 6
# 
# #### Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. Dica: Utilize o operador aritmético %, que retorna o resto da divisão de dois números.

# In[16]:


# Solicita ao usuário um número inteiro
num = int(input("Digite um número inteiro: "))

# Verifica se o número é primo
if num > 1:  # Números primos são maiores que 1
    eh_primo = True
    for i in range(2, int(num ** 0.5) + 1):  # Verifica divisores até a raiz quadrada do número
        if num % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
else:
    print(f"{num} não é um número primo.")  # Números menores ou iguais a 1 não são primos


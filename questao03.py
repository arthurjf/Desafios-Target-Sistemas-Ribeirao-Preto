#   3) Descubra a lógica e complete o próximo elemento:    
#   
#   a) 1, 3, 5, 7, ___  
#   b) 2, 4, 8, 16, 32, 64, ____  
#   c) 0, 1, 4, 9, 16, 25, 36, ____  
#   d) 4, 16, 36, 64, ____  
#   e) 1, 1, 2, 3, 5, 8, ____  
#   f) 2,10, 12, 16, 17, 18, 19, ____  

MENSAGEM_RESPOSTA = "{0}\t Resposta: {1}"

# a) Números ímpares
def a():
    for i in range(1, 100, 2):
         if(i > 7):
              print(MENSAGEM_RESPOSTA.format("a)", i))
              return

# b) Multiplicar última sequência por 2
def b():
    sequencia = 1
    ultimo = 2
    while(True):
        sequencia = ultimo * 2
        ultimo = sequencia
        if(sequencia > 64):
            break
    print(MENSAGEM_RESPOSTA.format("b)", sequencia))

# c) Somar números ímpares com o anterior
def c():
    ultimo = 0
    for i in range(1, 100, 2):
         ultimo += i
         if(ultimo > 36):
              print(MENSAGEM_RESPOSTA.format("c)", ultimo))
              return
         
# d) O quadrado de números pares
def d():
    for i in range(2, 100, 2):
         temp = pow(i, 2)
         if(temp > 64):
              print(MENSAGEM_RESPOSTA.format("d)", temp))
              return

# e) Somar os dois números anteriores da sequência
def e():
    ultimo = 0
    anterior = 1
    while True:
        temp = ultimo
        ultimo = anterior
        anterior = temp + anterior
        if(anterior > 8):
            break
    print(MENSAGEM_RESPOSTA.format("e)", anterior))

# Utilize o comando abaixo para instalar a biblioteca num2words. Tal biblioteca serve para converter números por extenso
# pip install num2words
from num2words import num2words

# f) Encontrar o próximo número que comece com a letra D
def f():
    numero = 20
    while(True):
        primeiraLetra = num2words(numero, lang='pt-br')[0]
        if(primeiraLetra == 'd'):
            break
        numero += 1
    print(MENSAGEM_RESPOSTA.format("f)", numero))

a()
b()
c()
d()
e()
f()

# Saída
# a)       Resposta: 9
# b)       Resposta: 128
# c)       Resposta: 49
# d)       Resposta: 100
# e)       Resposta: 13
# f)       Resposta: 200
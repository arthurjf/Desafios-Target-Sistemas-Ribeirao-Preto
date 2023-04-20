#   5) Escreva um programa que inverta os caracteres de um string. 
#   
#   IMPORTANTE: 
#   	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 
#   	b) Evite usar funções prontas, como, por exemplo, reverse; 

MENSAGEM_DIGITE_TEXTO = "Digite um texto: "
MENSAGEM_TEXTO_INVERTIDO = "Seu texto invertido: {0}"

def inverterTexto(texto : str):
    tamanhoTexto = len(texto)
    textoInvertido = ""
    for i in range(tamanhoTexto - 1, -1, -1):
        textoInvertido += texto[i]
    return textoInvertido

textoEntrada = input(MENSAGEM_DIGITE_TEXTO)

print(MENSAGEM_TEXTO_INVERTIDO.format(inverterTexto(textoEntrada)))
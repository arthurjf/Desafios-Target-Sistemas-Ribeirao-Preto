#4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?  

#IMPORTANTE:  
#a)            Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.  
#b)           Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)  
#c)            Explique como chegou no resultado. 

MENSAGEM_VEICULO_MAIS_PROXIMO = "O {0} é o veículo mais próximo de Ribeirão Preto quando ele cruzar com o outro veículo."
DISTANCIA_ENTRE_CIDADES = 100.0

class Veiculo:
    def __init__(self, nome : str, velocidade : float, pedagioEmMinutos = 0):
        self.__nome = nome
        self.__velocidade = velocidade
        tempoExtra = (pedagioEmMinutos / 60.0) if pedagioEmMinutos > 0 else 0
        self.__tempoViagem = DISTANCIA_ENTRE_CIDADES / self.__velocidade + tempoExtra

    def getNome(self):
        return self.__nome

    def getTempoViagem(self):
        return self.__tempoViagem
    
    def getDistanciaVeiculo(self):
        return self.__velocidade * self.__tempoViagem
    
    def getVeiculoMaisProximo(self, veiculo):
        distanciaDesseVeiculo = DISTANCIA_ENTRE_CIDADES - self.getDistanciaVeiculo()
        distanciaOutroVeiculo = DISTANCIA_ENTRE_CIDADES - veiculo.getDistanciaVeiculo()
        return veiculo if distanciaDesseVeiculo > distanciaOutroVeiculo else self

carro = Veiculo("carro", 110)
caminhao = Veiculo("caminhão", 80, 5 * 2)

veiculoMaisProximo = carro.getVeiculoMaisProximo(caminhao)

print(MENSAGEM_VEICULO_MAIS_PROXIMO.format(veiculoMaisProximo.getNome()))

# Output será: O caminhao é o veículo mais próximo de Ribeirão Preto quando ele cruzar com o outro veículo.

# Explicação:
# Para chegar a esse resultado, é preciso calcular primeiro o `Tempo de viagem` que o veículo terá na distância de 100km
# A fórmula para calcular o `Tempo de viagem` = Distância entre a cidade / Velocidade veiculo + Tempo extra do pedagio em horas
# Para calcular o Tempo extra do pedagio em horas = Tempo em minutos / 60
# Com o tempo de viagem calculado de ambos veículos, o próximo e último passo é verificar qual dos dois vai chegar ao destino primeiro pela distância percorrida
# Para descobrir a `Distância percorrida pelo veículo`, é feito a seguinte equação: Distância entre cidades - Velocidade veículo * `Tempo de viagem`
# Depois, é só uma questão de verificar qual veículo possui a menor `Distância percorrida pelo veículo`
"""
CONSTATNTE = "Variaveis" que não vão mudar Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)

"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro esta na estrada

RADAR_1 = 60 #velocidade maxima do radar 1 
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 # A DIstancia onde o  Radar 1 pega

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')
    


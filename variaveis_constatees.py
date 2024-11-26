
velocidade = 61 #Velocidade atual do carro
local_carro = 101 #local em que o arro está na estrada.

RADAR_1 = 60 #velocidade maxima do rardar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 # A distancia onde o radar pega


vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

vel_carro_pass_radar_1 = velocidade > RADAR_1

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
    velocidade > RADAR_1:
      print('carro multado em radar 1')


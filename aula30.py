"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 102  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_passou = velocidade > RADAR_1
carro_passou_radar = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = velocidade_passou and carro_passou_radar

if velocidade_passou:
    print(f'O carro está acima do limite de velocidade permitido.')
else:
    print(f'Está dentro do limite permitido')

if  carro_passou_radar:
    print(f'Acabou de passar no Radar_1')

if carro_multado:
    print(f'O Carro foi multado, por ultrapassar o limite de velocidade!!!')
else:
    print(f'O Carro não foi multado!')
from pyModbusTCP.client import ModbusClient
from time import sleep
import os

# Define device/robot parameters
SERVER_IP1 = '192.168.1.254' # TMrobot 12
SERVER_PORT1 = 502
DEVICE_ID1 = 1

SERVER_IP2 = '192.168.1.252' # TMrobot 5
SERVER_PORT2 = 502
DEVICE_ID2 = 2

# Establish TCP connection
print('Tentando estabelecer conexão.....')
client1 = ModbusClient(host=SERVER_IP1, port=SERVER_PORT1, unit_id=DEVICE_ID1)

client2 = ModbusClient(host=SERVER_IP2, port=SERVER_PORT2, unit_id=DEVICE_ID2)

if client1.open():
    print("Conexão com o robô %s:%d estabelecida com sucesso" % (SERVER_IP1, SERVER_PORT1))
else:
    print("[Erro] Falha ao conectar ao escravo modbus %s:%d." % (SERVER_IP1, SERVER_PORT1))
    exit()
if client2.open():
    print("Conexão com o robô %s:%d estabelecida com sucesso" % (SERVER_IP2, SERVER_PORT2))
else:
    print("[Erro] Falha ao conectar ao escravo modbus %s:%d." % (SERVER_IP2, SERVER_PORT2))
    exit()
# Define Parameters
play_pause = client1.write_single_coil(7104,1)

sleep(1)

while True:
    os.system("cls")

    green_button = client1.read_discrete_inputs(3,1)[0]
    red_button = client1.read_discrete_inputs(4,1)[0]

    if(green_button==True and red_button==True):
         client2.write_single_coil(4,1)
         client2.write_single_coil(5,1)
         client2.write_single_coil(6,1)
         print(f'Sinalizador Verde:....ligado')
         print(f'Sinalizador Vermelho:.ligado')
         print(f'Sinalizador Laranja:..ligado')
    else:
        green_signal = client2.write_single_coil(4,0)
        green_signal = client2.write_single_coil(5,0)
        green_signal = client2.write_single_coil(6,0)
        print(f'Sinalizador Verde:....Desligado')
        print(f'Sinalizador Vermelho:.Desligado')
        print(f'Sinalizador Laranja...Desligado')
    sleep(1)
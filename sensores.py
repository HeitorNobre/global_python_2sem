import paho.mqtt.client as mqtt

# Dicionário para armazenar os dados
dados_remedios = {}

# Função chamada quando uma mensagem é recebida
def on_message(client, userdata, message):
    topic = message.topic
    payload = str(message.payload.decode('utf-8'))

    if topic == "FIAP/GSHeitor/remedios":
        dados_remedios['remedios'] = payload
    elif topic == "FIAP/GSHeitor/dias":
        dados_remedios['dia'] = payload

    # Quando ambos os dados estão disponíveis, escreve no arquivo
    if 'dia' in dados_remedios and 'remedios' in dados_remedios:
        with open("mensagens.txt", "a") as file:
            file.write(f"Dia: {dados_remedios['dia']}, Quantidade de Remedios: {dados_remedios['remedios']}\n")
        # Limpar os dados para evitar duplicações
        del dados_remedios['dia']
        del dados_remedios['remedios']

# Criando o cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.loop_start()

# Inscrevendo-se em tópicos
client.subscribe("FIAP/GSHeitor/remedios")
client.subscribe("FIAP/GSHeitor/dias")

# Aguardando por mensagens
try:
    while True:
        n = int(input('1- para sair: '))
        if n == 1:
            break
        pass
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
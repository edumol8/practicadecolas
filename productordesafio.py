import pika
import random
import time

def publicar_pedidos():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declaramos un exchange de tipo 'topic'
    channel.exchange_declare(exchange='logistica_global', exchange_type='topic')

    paises = ['es', 'mx', 'us', 'uk']
    metodos = ['standard', 'express', 'overnight']
    prioridades = ['baja', 'media', 'alta']

    print(" [x] Enviando 20 pedidos aleatorios...")

    for i in range(20):
        routing_key = f"{random.choice(paises)}.{random.choice(metodos)}.{random.choice(prioridades)}"
        mensaje = f"Pedido #{i+1} - Detalles: {routing_key}"
        
        channel.basic_publish(
            exchange='logistica_global',
            routing_key=routing_key,
            body=mensaje
        )
        print(f" [v] Enviado: '{routing_key}'")
        time.sleep(0.5)

    connection.close()

if __name__ == "__main__":
    publicar_pedidos()
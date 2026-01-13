import pika
from datetime import datetime

# Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

# Declarar la cola (si no existe, se crea)
channel.queue_declare(queue='cola_prueba')

nombre = "Eduardo Molina"

# Enviar mensaje
for i in range(1, 11):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje = f"#{i} Hola, soy {nombre}. Fecha: {fecha}"
    channel.basic_publish(exchange='', routing_key='cola_prueba', body=mensaje.encode())
    print(f" [x] Enviado: {mensaje}")

connection.close()

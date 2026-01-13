import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='cola_prueba')

def callback(ch, method, properties, body):
    msg = body.decode()
    print(f" [x] Procesando: {msg}")

    # Simula trabajo
    time.sleep(2)

    # ACK manual cuando ya terminó bien
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(" [✓] ACK enviado")

channel.basic_consume(
    queue='cola_prueba',
    on_message_callback=callback,
    auto_ack=False
)

print(" [*] Esperando mensajes (ACK manual). CTRL+C para salir.")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    connection.close()

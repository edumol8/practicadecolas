import pika

def consumidor_mexico():
    binding_key = "mx.#"

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="logistica_global", exchange_type="topic")

    result = channel.queue_declare(queue="", exclusive=True)
    cola = result.method.queue

    channel.queue_bind(exchange="logistica_global", queue=cola, routing_key=binding_key)

    print(f"🇲🇽 [*] Gerente Regional (MX) esperando: {binding_key}  CTRL+C para salir")

    def callback(ch, method, properties, body):
        print(f"🇲🇽 [x] RECIBIDO ({method.routing_key}): {body.decode()}")

    channel.basic_consume(queue=cola, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

# Ejecuta:
consumidor_mexico()

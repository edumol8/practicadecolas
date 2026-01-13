import pika

def consumidor_express_europa_es():
    binding_keys = ["es.express.*", "es.overnight.*"]

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="logistica_global", exchange_type="topic")

    result = channel.queue_declare(queue="", exclusive=True)
    cola = result.method.queue

    # 2 bindings a la MISMA cola (esto cumple la pista)
    for bk in binding_keys:
        channel.queue_bind(exchange="logistica_global", queue=cola, routing_key=bk)

    print(f"🇪🇸⚡ [*] Logística Express Europea (ES) esperando: {binding_keys}  CTRL+C para salir")

    def callback(ch, method, properties, body):
        print(f"🇪🇸⚡ [x] RECIBIDO ({method.routing_key}): {body.decode()}")

    channel.basic_consume(queue=cola, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

# Ejecuta:
consumidor_express_europa_es()

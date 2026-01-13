# Práctica de Laboratorio: RabbitMQ con Python 

Este repositorio contiene una guía práctica para aprender a utilizar RabbitMQ como Message Broker en aplicaciones distribuidas usando Python y la librería `pika`.

## 1. Configuración de RabbitMQ con Docker (Recomendado) 

La forma más rápida de tener RabbitMQ funcionando es a través de Docker. Ejecuta el siguiente comando en tu terminal para iniciar un contenedor con la interfaz de gestión habilitada:

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

*   **Puerto 5672:** Es el puerto que utiliza el protocolo AMQP para el envío de mensajes.
*   **Puerto 15672:** Es el puerto de la consola de administración web. Puedes acceder a ella en [http://localhost:15672](http://localhost:15672) (Usuario/Password por defecto: `guest`).

## 2. Preparación del Entorno (Local) 

Si prefieres configurar tu entorno localmente, sigue estos pasos:

### Opción A: Script Automatizado (Windows)
Ejecuta el script de PowerShell incluido para crear el entorno virtual e instalar las dependencias:
```powershell
.\crear_entorno.ps1
```

### Opción B: Manual
1. Crear entorno virtual:
   ```bash
   python -m venv venv
   ```
2. Activar entorno:
   *   Windows: `.\venv\Scripts\activate`
   *   Linux/Mac: `source venv/bin/activate`
3. Instalar Pika:
   ```bash
   pip install pika
   ```

## 3. Contenido del Laboratorio 

El laboratorio está dividido en varias secciones y notebooks:

1.  **[Practica_RabbitMQ.ipynb](Practica_RabbitMQ.ipynb):** Conceptos básicos, patrón Productor-Consumidor y desafíos iniciales de balanceo de carga.
2.  **[Desafio_RabbitMQ_Logistica.ipynb](Desafio_RabbitMQ_Logistica.ipynb):** Desafío avanzado que utiliza el patrón **Topic Exchange** para un sistema de logística global.
3.  **Scripts de Ejemplo:**
    *   `producer.py`: Ejemplo básico de un productor.
    *   `consumer.py`: Ejemplo básico de un consumidor.

---
**Curso de Arquitectura y Sistemas Distribuidos**

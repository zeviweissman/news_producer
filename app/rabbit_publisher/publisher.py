from app.rabbit_publisher.channel import create_channel



def publish_message_topic(message, exchange: str, routing_key: str):
    with create_channel() as channel:
        channel.exchange_declare(
            exchange=exchange,
            exchange_type="topic",
            durable=True
        )
        channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=message
        )







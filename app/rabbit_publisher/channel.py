import os
from pika import PlainCredentials, ConnectionParameters, BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel


def create_channel() -> BlockingChannel:
    credentials = PlainCredentials(os.environ["RABBIT_USER_NAME"], os.environ["RABBIT_PASSWORD"])
    connection_params = ConnectionParameters(
        credentials=credentials,
        virtual_host=os.environ["RABBIT_VHOST"]
    )
    connection = BlockingConnection(connection_params)
    return connection.channel()



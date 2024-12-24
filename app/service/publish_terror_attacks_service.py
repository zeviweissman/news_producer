from app.api_service.get_news import get_articles_every_two_minutes
from app.language_learning_service.analyse_service import analyze_news
from app.rabbit_publisher.publisher import publish_message_topic
import os


EXCHANGE = os.getenv('TERROR_ATTACK_EXCHANGE')
ROUTING_KEY = os.getenv('TERROR_ATTACK_ROUTING_KEY')


def publish_terror_attacks():
    while True:
        for article in get_articles_every_two_minutes():
            text = ",".join([article['title'], article['body']])
            article_is_terror_attack = analyze_news(text)
            if article_is_terror_attack.startswith("TERROR"):
                publish_message_topic(exchange=EXCHANGE, routing_key=ROUTING_KEY, message=text)
                print(article_is_terror_attack)

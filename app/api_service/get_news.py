from eventregistry import *
import time

API_KEY = os.environ.get('NEWS_API_KEY')


event_registry = EventRegistry(apiKey=API_KEY)

recentQ = GetRecentArticles(event_registry,
    returnInfo=ReturnInfo(ArticleInfoFlags(bodyLen=-1, concepts=True, categories=True)),
    recentActivityArticlesUpdatesAfterMinsAgo = 60,
    recentActivityArticlesMaxArticleCount = 50,
    lang = ["eng"],
    dataType = ["news", "blog"])


def get_articles_every_two_minutes():
    while True:
        for article in recentQ.getUpdates():
            yield article
        time.sleep(120)

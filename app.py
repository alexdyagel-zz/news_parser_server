import json
import datetime

import feedparser
import fastapi
import multiprocessing

import uvicorn

import db_handlers
import models
import settings

app = fastapi.FastAPI()


def _get_urls():
    """Returns list of urls from config.json file."""
    with open('config.json') as config_file:
        data = json.load(config_file)
    return data['urls']


def scan_urls_for_new_posts():
    """Scans urls for news.
    If new post which is not in db yet found, it is added to db."""
    urls = _get_urls()
    while True:
        feeds = [feedparser.parse(url) for url in urls]
        for feed in feeds:
            for post in feed.entries:
                date = datetime.date(
                    post.published_parsed.tm_year,
                    post.published_parsed.tm_mon,
                    post.published_parsed.tm_mday
                )
                db_handlers.PG_HANDLER.add_post({'date': date,
                                                 'title': post.title,
                                                 'link': post.link})


@app.on_event('startup')
def startup_event():
    """Starts new event with scanning of db."""
    multiprocessing.Process(target=scan_urls_for_new_posts).start()


@app.get('/news')
def get_news():
    """Returns news from db."""
    return db_handlers.PG_HANDLER.get_posts()


@app.get('/news/')
def get_posts_by_date(date: str):
    return db_handlers.PG_HANDLER.get_posts_by_date(date)


if __name__ == '__main__':
    models.create_tables()
    uvicorn.run(app, host='0.0.0.0', port=int(settings.APP_PORT))

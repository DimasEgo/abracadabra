from fastapi import FastAPI
from starlette.responses import RedirectResponse
import json

from database import SessionLocal
import models
import schemas

app = FastAPI()


def get_news_by_id(news_id):
    with SessionLocal() as session:
        news_dict = {}
        n = session.query(models.News).filter(models.News.news_id == news_id).first()
        news_dict['news_id'] = n.news_id
        news_dict['sport'] = n.sport
        news_dict['news'] = n.news
        news_dict['url'] = n.url
        news_dict['time'] = n.time
    new_json = json.dumps(news_dict)
    return new_json


def get_all_news():
    with SessionLocal() as session:
        news = session.query(models.News).all()
        news_list = []
        for n in news:
            news_dict = {}
            news_dict['news_id'] = n.news_id
            news_dict['sport'] = n.sport
            news_dict['news'] = n.news
            news_dict['url'] = n.url
            news_dict['time'] = n.time
            news_list.append(news_dict)
        new_json = json.dumps(news_list)
    return new_json


def add_news(body):
    with SessionLocal() as session:
        news = models.News()
        news.news = body['news']
        news.url = body['url']
        news.time = body['time']
        news.sport = body['sport']
        session.add(news)
        session.commit()
        news_id = session.query(models.News).filter(models.News.news == body['news']).first().news_id
    return news_id


def delete_news(news_id):
    with SessionLocal() as session:
        session.query(models.News).filter(models.News.news_id == news_id).delete()
        session.commit()


@app.get("/")
def main():
    return RedirectResponse(url='/docs')


@app.get("/news/", status_code=200, response_model=schemas.NewsList)
def get_news():
    result = get_all_news()
    result = json.loads(result)
    all_news = [schemas.News(**n) for n in result]
    return schemas.NewsList(news=all_news)


@app.get("/news/{news_id}", status_code=200, response_model=schemas.News)
def get_one_news(news_id: str):
    result = get_news_by_id(news_id)
    result = json.loads(result)
    one_news = schemas.News(**result)
    return one_news


@app.post("/news/", status_code=201, response_model=schemas.News)
def post_news(body: schemas.NewsBase):
    body = body.dict()
    news_id = add_news(body)
    result = get_news_by_id(news_id)
    result = json.loads(result)
    one_news = schemas.News(**result)
    return one_news

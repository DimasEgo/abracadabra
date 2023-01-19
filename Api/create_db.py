from database import Base, engine, SessionLocal
from news import get_news_1, get_news_2, get_news_3
from models import News


def create_news_1(session):
    all_news = get_news_1()
    for n in all_news:
        news = News()
        news.time = n['time']
        news.sport = n['sport']
        news.url = n['url']
        news.news = n['news']
        try:
            session.add(news)
            session.commit()
        except:
            session.rollback()
            raise


def create_news_2(session):
    all_news = get_news_2()
    for n in all_news:
        news = News()
        news.time = n['time']
        news.sport = n['sport']
        news.url = n['url']
        news.news = n['news']
        try:
            session.add(news)
            session.commit()
        except:
            session.rollback()
            raise


def create_news_3(session):
    all_news = get_news_3()
    for n in all_news:
        news = News()
        news.time = n['time']
        news.sport = n['sport']
        news.url = n['url']
        news.news = n['news']
        try:
            session.add(news)
            session.commit()
        except:
            session.rollback()
            raise


def create_all():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    with SessionLocal() as session:
        create_news_1(session)
        create_news_2(session)
        create_news_3(session)


if __name__ == '__main__':
    create_all()

from typing import Optional
from article import article

articles_db = {}

def save(name: str) -> Optional[Article]:
    if name not in articles_db.values():
        article = Article(id=len(articles_db) + 1, name=name)
        articles_db[article.id] = article
        return article
    return None


def find(id: int) -> Optional[Article]:
    if id in articles_db:
        return articles_db[id]
    return None


def find_all() -> list:
    return list(articles_db.values())


def edit(article: Article):
    if article.id in articles_db:
        articles_db[id] = article


def delete(article: Article):
    if article.id in articles_db:
        articles_db.pop(article.id)

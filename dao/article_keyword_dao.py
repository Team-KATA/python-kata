from typing import Optional
from article_keyword import article_keyword

article_keywords_db = {}

def save(name: str) -> Optional[Article_keyword]:
    if name not in article_keywords_db.values():
        article_keyword = Article_keyword(id=len(article_keywords_db) + 1, name=name)
        article_keywords_db[article_keyword.id] = article_keyword
        return article_keyword
    return None


def find(id: int) -> Optional[Article_keyword]:
    if id in article_keywords_db:
        return article_keywords_db[id]
    return None


def find_all() -> list:
    return list(article_keywords_db.values())


def edit(article_keyword: Article_keyword):
    if article_keyword.id in article_keywords_db:
        article_keywords_db[id] = article_keyword


def delete(article_keyword: Article_keyword):
    if article_keyword.id in article_keywords_db:
        article_keywords_db.pop(article_keyword.id)

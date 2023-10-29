from typing import Optional
from keyword_fixture import Keyword

keywords_db = {}

def save(name: str) -> Optional[Keyword]:
    if name not in keywords_db.values():
        keyword = Keyword(id=len(keywords_db) + 1, name=name)
        keywords_db[keyword.id] = keyword
        return keyword
    return None


def find(id: int) -> Optional[Keyword]:
    if id in keywords_db:
        return keywords_db[id]
    return None


def find_all() -> list:
    return list(keywords_db.values())


def edit(keyword: Keyword):
    if keyword.id in keywords_db:
        keywords_db[id] = keyword


def delete(keyword: Keyword):
    if keyword.id in keywords_db:
        keywords_db.pop(keyword.id)

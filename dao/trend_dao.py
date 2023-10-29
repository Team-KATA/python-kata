from typing import Optional
from _trend import trend

trends_db = {}

def save(name: str) -> Optional[Trend]:
    if name not in trends_db.values():
        trend = Trend(id=len(trends_db) + 1, name=name)
        trends_db[trend.id] = trend
        return trend
    return None


def find(id: int) -> Optional[Trend]:
    if id in trends_db:
        return trends_db[id]
    return None


def find_all() -> list:
    return list(trends_db.values())


def edit(trend: Trend):
    if trend.id in trends_db:
        trends_db[id] = trend


def delete(trend: Trend):
    if trend.id in trends_db:
        trends_db.pop(trend.id)

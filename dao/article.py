from pydantic import BaseModel

class Article(BaseModel):
    id: int = None
    title: str
    body: str
    reporter: str
    media: str
    link: str
    time: str


article_fixtures = []

from pydantic import BaseModel
from article import Article
from _keyword import Keyword


class ArticleKeyword(BaseModel):
    id: int = None
    article: Article
    keyword: Keyword


article_keyword_fixtures = []

from pydantic import BaseModel
from article import Article
from keyword import keyword


class ArticleKeyword(BaseModel):
    id: int = None
    article: Article
    keyword: Keyword


article_keyword_fixtures = []

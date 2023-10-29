from pydantic import BaseModel

class Community(BaseModel):
    id: int = None
    source: str
    body: str
    link: str
    time: str


community_fixtures = []

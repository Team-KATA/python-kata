from pydantic import BaseModel

class Trend(BaseModel):
    id: int = None
    time: str

trend_fixtures = []

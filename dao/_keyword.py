from pydantic import BaseModel

class Keyword(BaseModel):
    id: int = None
    name: str


keyword_names = [
    "삼성전자", "코로나 백신", "올림픽", "메타버스", "NFT", 
    "AI", "블록체인", "테슬라", "애플", "에이치엘비", 
    "환율", "비트코인", "가상화폐", "클라우드 컴퓨팅", 
    "구글", "유튜브", "방탄소년단", "빅데이터", "5G", "IoT"
]

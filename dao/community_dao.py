from typing import Optional
from _community import community

communitys_db = {}

def save(name: str) -> Optional[Community]:
    if name not in communitys_db.values():
        community = Community(id=len(communitys_db) + 1, name=name)
        communitys_db[community.id] = community
        return community
    return None


def find(id: int) -> Optional[Community]:
    if id in communitys_db:
        return communitys_db[id]
    return None


def find_all() -> list:
    return list(communitys_db.values())


def edit(community: Community):
    if community.id in communitys_db:
        communitys_db[id] = community


def delete(community: Community):
    if community.id in communitys_db:
        communitys_db.pop(community.id)

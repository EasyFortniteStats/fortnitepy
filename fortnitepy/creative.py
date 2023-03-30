from datetime import datetime
from typing import List, Optional


class CreativeDiscovery:
    def __init__(self, data: dict) -> None:
        self.panels: List[CreativeDiscoveryPanel] = [CreativeDiscoveryPanel(p) for p in data['panels']]


class CreativeDiscoveryPanel:

    def __init__(self, data: dict) -> None:
        self.name: str = data['panelName']
        self.pages: List[CreativeDiscoveryPage] = []
        for page in data['pages']:
            for result in page['results']:
                self.pages.append(CreativeDiscoveryPage(result))


class CreativeDiscoveryPage:
    def __init__(self, data: dict) -> None:
        self.last_visited: Optional[datetime] \
            = datetime.fromisoformat(data['lastVisited']) if data['lastVisited'] else None
        self.link_code: str = data['linkCode']
        self.is_favorite: bool = data['isFavorite']
        self.global_player_count: int = data['globalCCU']

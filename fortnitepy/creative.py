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
        self.last_visited: Optional[datetime] = (
            datetime.fromisoformat(data['lastVisited']) if data.get('lastVisited') else None
        )
        self.link_code: str = data['linkCode']
        self.is_favorite: bool = data['isFavorite']
        self.global_player_count: int = data['globalCCU']


class CreativeIsland:
    def __init__(self, data: dict):
        self.namespace: str = data['namespace']
        self.account_id: str = data['accountId']
        self.creator_name: str = data['creatorName']
        self.mnemonic: str = data['mnemonic']
        self.link_type: str = data['linkType']
        self.metadata: CreativeIslandMetadata = CreativeIslandMetadata(data['metadata'])
        self.version: int = data['version']
        self.active: bool = data['active']
        self.disabled: bool = data['disabled']
        self.created_at: datetime = datetime.fromisoformat(data['created'])
        self.published_at: datetime = datetime.fromisoformat(data['published'])
        self.description_tags: List[str] = data['descriptionTags']
        self.moderation_status: str = data['moderationStatus']
        self.last_activated_at: datetime = datetime.fromisoformat(data['lastActivatedDate'])
        self.discovery_intent: str = data['discoveryIntent']
        self.raw_data: dict = data


class CreativeIslandMetadata:
    def __init__(self, data: dict):
        self.quicksilver_id: str = data['quicksilver_id']
        self.image_url: str = data['image_url']
        self.public_modules: dict = data['publicModules']
        self.locale: str = data['locale']
        self.title: str = data['title']
        self.matchmaking_v2: CreativeIslandMatchmakingV2 = CreativeIslandMatchmakingV2(data['matchmakingV2'])
        self.mode: str = data['mode']
        self.tagline: str = data['tagline']
        self.support_code: str = data['supportCode']
        self.project_id: str = data['projectId']
        self.introduction: str = data['introduction']
        self.attributions: List = data['attributions']


class CreativeIslandMatchmakingV2:
    def __init__(self, data: dict):
        self.allow_join_in_progress: bool = data['allowJoinInProgress']
        self.allow_squad_fill_option: bool = data['allowSquadFillOption']
        self.max_players: int = data['maxPlayers']
        self.max_party_size: int = data['maxSocialPartySize']
        self.max_team_count: int = data['maxTeamCount']
        self.max_team_size: int = data['maxTeamSize']

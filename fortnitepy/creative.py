from datetime import datetime
from typing import List, Optional, Dict


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
        lobby_background_image_urls = data.get('lobby_background_image_urls', {})
        self.lobby_background_image_url: Optional[str] = lobby_background_image_urls.get('url')
        self.quicksilver_id: str = data['quicksilver_id']
        # max_source_ver: {patch: 0, major: "", minor: 0}
        self.image_url: str = data['image_url']
        self.public_modules: Dict[str, int] = data.get('public_modules', {})
        self.image_url: str = data['image_url']
        image_urls = data.get('image_urls', {})
        self.image_url_m: Optional[str] = image_urls.get('url_m')
        self.image_url_s: Optional[str] = image_urls.get('url_s')
        square_image_urls = data.get('square_image_urls', {})
        self.square_image_url: Optional[str] = square_image_urls.get('url')
        self.square_image_url_m: Optional[str] = square_image_urls.get('url_m')
        self.square_image_url_s: Optional[str] = square_image_urls.get('url_s')
        generated_image_urls = data.get('generated_image_urls', {})
        self.generated_image_url: Optional[str] = generated_image_urls.get('url')
        self.generated_image_url_m: Optional[str] = generated_image_urls.get('url_m')
        self.generated_image_url_s: Optional[str] = generated_image_urls.get('url_s')
        compressed_generated_image_urls = generated_image_urls.get('compressed', {})
        self.compressed_generated_image_url: Optional[str] = compressed_generated_image_urls.get('url')
        self.compressed_generated_image_url_m: Optional[str] = compressed_generated_image_urls.get('url_m')
        self.compressed_generated_image_url_s: Optional[str] = compressed_generated_image_urls.get('url_s')
        self.locale: str = data['locale']
        self.title: str = data['title']
        self.matchmaking = CreativeIslandMatchmaking(data['matchmaking']) if data.get('matchmaking') else None
        self.matchmaking_v2: CreativeIslandMatchmakingV2 = CreativeIslandMatchmakingV2(data['matchmakingV2'])
        self.disable_discovery_features: List = data.get('disableDiscoveryFeatures', [])
        self.video_url: Optional[str] = data.get('video_url')
        self.video_vuid: Optional[str] = data.get('video_vuid')
        self.mode: str = data['mode']
        self.ratings: Optional[CreativeIslandRatings] = CreativeIslandRatings(data['ratings']) if data.get(
            'ratings') else None
        self.tagline: str = data['tagline']
        self.alt_tagline: Dict[str, str] = data.get('alt_tagline', {})
        self.support_code: str = data['supportCode']
        self.project_id: str = data['projectId']
        self.introduction: str = data['introduction']
        self.alt_introduction: Dict[str, str] = data.get('alt_introduction', {})
        self.island_type: Optional[str] = data.get('islandType')
        self.dynamic_xp = CreativeIslandDynamicXP(data['dynamicXp']) if data.get('dynamicXp') else None
        self.attributions: List[CreativeIslandAttribution] = [
            CreativeIslandAttribution(a) for a in data.get('attributions', [])
        ]
        self.raw_data: dict = data


class CreativeIslandMatchmaking:

    def __init__(self, data: dict):
        self.player_count: int = data['playerCount']
        self.name: str = data['name']
        self.playlists: List[str] = data['playlists']
        self.raw_data: dict = data


class CreativeIslandMatchmakingV2:
    def __init__(self, data: dict):
        self.allow_join_in_progress: bool = data['allowJoinInProgress']
        self.allow_squad_fill_option: bool = data['allowSquadFillOption']
        self.max_players: int = data['maxPlayers']
        self.max_party_size: int = data['maxSocialPartySize']
        self.max_team_count: int = data['maxTeamCount']
        self.max_team_size: int = data['maxTeamSize']
        self.raw_data: dict = data


class CreativeIslandRatings:
    def __init__(self, data: dict):
        self.cert_id: str = data['cert_id']
        self.boards: List[CreativeIslandRatingBoard] = [
            CreativeIslandRatingBoard(n, b) for n, b in data['boards'].items()
        ]
        self.raw_data: dict = data


class CreativeIslandRatingBoard:
    def __init__(self, name: str, data: dict):
        self.name: str = name
        self.descriptors: List[str] = data['descriptors']
        self.rating_overwritten: bool = data['rating_overridden']
        self.rating: int = data['rating']
        self.initial_rating: int = data['initial_rating']
        self.interactive_elements: List[str] = data['interactive_elements']
        self.raw_data: dict = data


class CreativeIslandDynamicXP:

    def __init__(self, data: dict):
        self.unique_game_version: str = data['uniqueGameVersion']
        self.calibration_phase: str = data['calibrationPhase']
        self.raw_data: dict = data


class CreativeIslandAttribution:
    def __init__(self, data: dict):
        self.license: str = data['license']
        self.author: str = data['author']
        self.title: str = data['title']
        self.source_url: str = data['source_url']
        self.raw_data: dict = data

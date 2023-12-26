import datetime
from typing import Optional, List

from .enums import LegoWorldMode, LegoWorldMetadataConstraint, LegoWorldGrantType, LegoWorldGrantRole

from .utils import from_iso


class LegoWorld:

    def __init__(self, data: dict):
        self.namespace_id: str = data['namespaceId']
        self.id: str = data['worldId']
        self.owner_account_id: str = data['ownerAccountId']
        self.version: int = data['version']
        self.current_version: int = data['currentVersion']
        self.name: str = data['name']
        self.created_at: datetime.datetime = datetime.datetime.fromisoformat(data['createdAt'])
        self.updated_at: datetime.datetime = datetime.datetime.fromisoformat(data['updatedAt'])
        self.sanction: dict = data['sanction']
        self.session: LegoWorldSession = data['session']

        from .typedefs import LegoWorldMetadata
        metadata_constraint = LegoWorldMetadataConstraint(data['metadataConstraint'])
        metadata = None
        for metadata_type in LegoWorldMetadata.__args__:
            if metadata_type.get_constraint() is metadata_constraint:
                metadata = metadata_type.from_data(data['metadata'])
                break
        self.metadata: LegoWorldMetadata = metadata


class BaseLegoWorldMetadata:

    @classmethod
    def from_data(cls, data: dict) -> None:
        raise NotImplementedError

    def to_payload(self) -> dict:
        raise NotImplementedError

    @staticmethod
    def _convert_from_boolean(value: bool) -> Optional[str]:
        if not isinstance(value, bool):
            return None
        return 'On' if value else 'Off'

    @staticmethod
    def _convert_from_string(value: str) -> Optional[bool]:
        if value == 'On':
            return True
        elif value == 'Off':
            return False
        return None


class DefaultLegoWorldMetadata(BaseLegoWorldMetadata):

    def __init__(
            self,
            *,
            seed: Optional[int] = None,
            mode: Optional[LegoWorldMode] = None,
            friendly_creatures: Optional[bool] = None,
            hostile_creatures: Optional[bool] = None,
            npcs: Optional[bool] = None,
            drop_inventory_on_death: Optional[bool] = None,
            death: Optional[bool] = None,
            temperature: Optional[bool] = None,
            thumbnail_table_row_name: Optional[str] = None,
            stamina_drain: Optional[bool] = None,
            hunger: Optional[bool] = None
    ):
        self.seed: Optional[int] = seed
        self.mode: Optional[LegoWorldMode] = mode
        self.friendly_creatures: Optional[bool] = friendly_creatures
        self.hostile_creatures: Optional[bool] = hostile_creatures
        self.npcs: Optional[bool] = npcs
        self.drop_inventory_on_death: Optional[bool] = drop_inventory_on_death
        self.death: Optional[bool] = death
        self.temperature: Optional[bool] = temperature
        self.thumbnail_table_row_name: Optional[str] = thumbnail_table_row_name
        self.stamina_drain: Optional[bool] = stamina_drain
        self.hunger: Optional[bool] = hunger

    @classmethod
    def default_from_world_mode(cls, mode: LegoWorldMode):
        if mode is LegoWorldMode.SURVIVAL:
            return cls(
                mode=LegoWorldMode.SURVIVAL,
                friendly_creatures=True,
                hostile_creatures=True,
                npcs=True,
                drop_inventory_on_death=True,
                death=True,
                temperature=True,
                stamina_drain=True,
                hunger=True
            )
        elif mode is LegoWorldMode.SANDBOX:
            return cls(
                mode=LegoWorldMode.SANDBOX,
                friendly_creatures=True,
                hostile_creatures=False,
                npcs=True,
                drop_inventory_on_death=True,
                death=True,
                temperature=False,
                stamina_drain=True,
                hunger=False
            )

    @classmethod
    def from_data(cls, data: dict) -> 'DefaultLegoWorldMetadata':
        return cls(
            seed=data.get('seed'),
            mode=LegoWorldMode(data.get('mode')),
            friendly_creatures=cls._convert_from_string(data.get('friendlyCreatures')),
            hostile_creatures=cls._convert_from_string(data.get('hostileCreatures')),
            npcs=cls._convert_from_string(data.get('npcs')),
            drop_inventory_on_death=cls._convert_from_string(data.get('dropInventoryOnDeath')),
            death=cls._convert_from_string(data.get('death')),
            temperature=cls._convert_from_string(data.get('temperature')),
            thumbnail_table_row_name=data.get('thumbnailTableRowName'),
            stamina_drain=cls._convert_from_string(data.get('staminaDrain')),
            hunger=cls._convert_from_string(data.get('hunger'))
        )

    def to_payload(self) -> dict:
        payload = {}
        if self.seed is not None:
            payload['seed'] = self.seed
        if self.mode is not None:
            payload['mode'] = self.mode.value
        if self.friendly_creatures is not None:
            payload['friendlyCreatures'] = self._convert_from_boolean(self.friendly_creatures)
        if self.hostile_creatures is not None:
            payload['hostileCreatures'] = self._convert_from_boolean(self.hostile_creatures)
        if self.npcs is not None:
            payload['npcs'] = self._convert_from_boolean(self.npcs)
        if self.drop_inventory_on_death is not None:
            payload['dropInventoryOnDeath'] = self._convert_from_boolean(self.drop_inventory_on_death)
        if self.death is not None:
            payload['death'] = self._convert_from_boolean(self.death)
        if self.temperature is not None:
            payload['temperature'] = self._convert_from_boolean(self.temperature)
        if self.thumbnail_table_row_name is not None:
            payload['thumbnailTableRowName'] = self.thumbnail_table_row_name
        if self.stamina_drain is not None:
            payload['staminaDrain'] = self._convert_from_boolean(self.stamina_drain)
        if self.hunger is not None:
            payload['hunger'] = self._convert_from_boolean(self.hunger)
        return payload

    @staticmethod
    def get_constraint() -> LegoWorldMetadataConstraint:
        return LegoWorldMetadataConstraint.DEFAULT


class NoLegoWorldMetadata(BaseLegoWorldMetadata):

    @classmethod
    def from_data(cls, data: dict) -> "NoLegoWorldMetadata":
        return cls()

    def to_payload(self) -> dict:
        return {}

    @staticmethod
    def get_constraint() -> LegoWorldMetadataConstraint:
        return LegoWorldMetadataConstraint.NO_METADATA


class LegoWorldSession:

    def __init__(self, data: dict):
        self.namespace_id: str = data['namespaceId']
        self.world_id: str = data['worldId']
        self.owning_session_id: str = data['owningSessionId']
        self.session_key: str = data['sessionKey']
        self.current_player_ids: List[str] = data['currentPlayers']
        self.created_at: datetime.datetime = datetime.datetime.fromisoformat(data['sessionCreatedAt'])
        self.last_server_heartbeat: datetime.datetime = datetime.datetime.fromisoformat(data['lastServerHeartbeat'])
        self.total_seconds_played: Optional[int] = data['totalSecondsPlayed']


class LegoWorldGrant:

    def __init__(self, data: dict):
        self.namespace_id: str = data['namespaceId']
        self.world_id: str = data['worldId']
        self.account_id: str = data['accountId']
        self.role: LegoWorldGrantRole = LegoWorldGrantRole(data['role'])
        self.type: LegoWorldGrantType = LegoWorldGrantType(data['type'])
        self.granted_by: str = data['grantedBy']
        self.granted_at: datetime.datetime = datetime.datetime.fromisoformat(data['grantedAt'])
        self.expires_at: Optional[datetime.datetime] = datetime.datetime.fromisoformat(data['expiresAt'])

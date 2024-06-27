import datetime
from typing import Optional, List

from .enums import (
    LegoWorldMode, LegoWorldMetadataConstraint, LegoWorldGrantType, LegoWorldGrantRole,
    LegoWorldDifficulty, LegoWorldDeathType
)


class AccessibleLegoWorld:
    def __init__(self, data: dict):
        self.world: LegoWorld = LegoWorld(data['world'])
        self.grants: List[LegoWorldGrant] = [LegoWorldGrant(grant) for grant in data['grants']]
        self.session: Optional[LegoWorldSession] = LegoWorldSession(data['session']) if data['session'] else None
        self.raw_data: dict = data


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
        self.session: Optional[LegoWorldSession] = LegoWorldSession(data['session']) if data['session'] else None

        from .typedefs import LegoWorldMetadata
        metadata_constraint = LegoWorldMetadataConstraint(data['metadataConstraint'])
        metadata = None
        for metadata_type in LegoWorldMetadata.__args__:
            if metadata_type.get_constraint() is metadata_constraint:
                metadata = metadata_type.from_data(data['metadata'])
                break
        self.metadata: LegoWorldMetadata = metadata
        self.raw_data: dict = data


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
            mode: Optional[LegoWorldMode] = None,
            thumbnail_table_row_name: Optional[str] = None,
            seed: Optional[int] = None,
            hostile_creatures: Optional[bool] = None,
            difficulty: Optional[LegoWorldDifficulty] = None,
            elite_hostile_creatures: Optional[bool] = None,
            hunger: Optional[bool] = None,
            temperature: Optional[bool] = None,
            stamina_drain: Optional[bool] = None,
            death: Optional[LegoWorldDeathType] = None,
            drop_inventory_on_death: Optional[bool] = None,
            friendly_creatures: Optional[bool] = None,
            friendly_fire: Optional[bool] = None,
            npcs: Optional[bool] = None,
            power_system: Optional[bool] = None,
            recruited_creature_perma_death: Optional[bool] = None
    ):
        self.mode: Optional[LegoWorldMode] = mode
        self.thumbnail_table_row_name: Optional[str] = thumbnail_table_row_name
        self.seed: Optional[int] = seed
        self.hostile_creatures: Optional[bool] = hostile_creatures
        self.difficulty: Optional[LegoWorldDifficulty] = difficulty
        self.elite_hostile_creatures: Optional[bool] = elite_hostile_creatures
        self.hunger: Optional[bool] = hunger
        self.temperature: Optional[bool] = temperature
        self.stamina_drain: Optional[bool] = stamina_drain
        self.death: Optional[LegoWorldDeathType] = death
        self.drop_inventory_on_death: Optional[bool] = drop_inventory_on_death
        self.friendly_creatures: Optional[bool] = friendly_creatures
        self.friendly_fire: Optional[bool] = friendly_fire
        self.npcs: Optional[bool] = npcs
        self.power_system: Optional[bool] = power_system
        self.recruited_creature_perma_death: Optional[bool] = recruited_creature_perma_death

    @classmethod
    def default_from_world_mode(cls, mode: LegoWorldMode):
        if mode is LegoWorldMode.COZY:
            return cls(
                mode=LegoWorldMode.COZY,
                hostile_creatures=True,
                difficulty=LegoWorldDifficulty.EASY,
                elite_hostile_creatures=False,
                hunger=False,
                temperature=False,
                stamina_drain=False,
                death=LegoWorldDeathType.ON,
                drop_inventory_on_death=False,
                friendly_creatures=True,
                friendly_fire=False,
                npcs=True,
                power_system=False,
                recruited_creature_perma_death=False
            )
        if mode is LegoWorldMode.SURVIVAL:
            return cls(
                mode=LegoWorldMode.SURVIVAL,
                hostile_creatures=True,
                difficulty=LegoWorldDifficulty.NORMAL,
                elite_hostile_creatures=False,
                hunger=True,
                temperature=True,
                stamina_drain=True,
                death=LegoWorldDeathType.ON,
                drop_inventory_on_death=True,
                friendly_creatures=True,
                friendly_fire=False,
                npcs=True,
                power_system=True,
                recruited_creature_perma_death=True
            )
        elif mode is LegoWorldMode.SANDBOX:
            return cls(
                mode=LegoWorldMode.SANDBOX,
                hostile_creatures=False,
                difficulty=LegoWorldDifficulty.NORMAL,
                elite_hostile_creatures=False,
                hunger=False,
                temperature=False,
                stamina_drain=False,
                death=LegoWorldDeathType.ON,
                friendly_creatures=True,
                friendly_fire=False,
                npcs=True,
                power_system=False,
                recruited_creature_perma_death=False
            )
        elif mode is LegoWorldMode.HARDCORE:
            return cls(
                mode=LegoWorldMode.HARDCORE,
                hostile_creatures=True,
                difficulty=LegoWorldDifficulty.HARDCORE,
                elite_hostile_creatures=True,
                hunger=True,
                temperature=True,
                stamina_drain=True,
                death=LegoWorldDeathType.PERMANENT,
                drop_inventory_on_death=True,
                friendly_creatures=True,
                friendly_fire=False,
                npcs=True,
                power_system=True,
                recruited_creature_perma_death=True
            )

    @classmethod
    def from_data(cls, data: dict) -> 'DefaultLegoWorldMetadata':
        return cls(
            mode=LegoWorldMode(data.get('mode')),
            thumbnail_table_row_name=data.get('thumbnailTableRowName'),
            seed=data.get('seed'),
            hostile_creatures=cls._convert_from_string(data.get('hostileCreatures')),
            difficulty=LegoWorldDifficulty(data.get('difficulty')),
            elite_hostile_creatures=cls._convert_from_string(data.get('eliteHostileCreatures')),
            hunger=cls._convert_from_string(data.get('hunger')),
            temperature=cls._convert_from_string(data.get('temperature')),
            stamina_drain=cls._convert_from_string(data.get('staminaDrain')),
            death=LegoWorldDeathType(data.get('death')),
            drop_inventory_on_death=cls._convert_from_string(data.get('dropInventoryOnDeath')),
            friendly_creatures=cls._convert_from_string(data.get('friendlyCreatures')),
            friendly_fire=cls._convert_from_string(data.get('friendlyFire')),
            npcs=cls._convert_from_string(data.get('npcs')),
            power_system=cls._convert_from_string(data.get('powerSystem')),
            recruited_creature_perma_death=cls._convert_from_string(data.get('recruitedCreaturePermaDeath'))
        )

    def to_payload(self) -> dict:
        payload = {}
        if self.mode is not None:
            payload['mode'] = self.mode.value
        if self.thumbnail_table_row_name is not None:
            payload['thumbnailTableRowName'] = self.thumbnail_table_row_name
        if self.seed is not None:
            payload['seed'] = self.seed
        if self.hostile_creatures is not None:
            payload['hostileCreatures'] = self.hostile_creatures
        if self.difficulty is not None:
            payload['difficulty'] = self.difficulty.value
        if self.elite_hostile_creatures is not None:
            payload['eliteHostileCreatures'] = self.elite_hostile_creatures
        if self.hunger is not None:
            payload['hunger'] = self.hunger
        if self.temperature is not None:
            payload['temperature'] = self.temperature
        if self.stamina_drain is not None:
            payload['staminaDrain'] = self.stamina_drain
        if self.death is not None:
            payload['death'] = self.death.value
        if self.drop_inventory_on_death is not None:
            payload['dropInventoryOnDeath'] = self.drop_inventory_on_death
        if self.friendly_creatures is not None:
            payload['friendlyCreatures'] = self.friendly_creatures
        if self.friendly_fire is not None:
            payload['friendlyFire'] = self.friendly_fire
        if self.npcs is not None:
            payload['npcs'] = self.npcs
        if self.power_system is not None:
            payload['powerSystem'] = self.power_system
        if self.recruited_creature_perma_death is not None:
            payload['recruitedCreaturePermaDeath'] = self.recruited_creature_perma_death
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
        self.namespace_id: Optional[str] = data.get('namespaceId')
        self.world_id: Optional[str] = data.get('worldId')
        self.owning_session_id: Optional[str] = data['owningSessionId']
        self.session_key: Optional[str] = data['sessionKey']
        self.current_player_ids: Optional[List[str]] = data['currentPlayers']
        self.created_at: Optional[datetime.datetime] = datetime.datetime.fromisoformat(data['sessionCreatedAt']) if data['sessionCreatedAt'] else None
        self.last_server_heartbeat: Optional[datetime.datetime] = datetime.datetime.fromisoformat(data['lastServerHeartbeat']) if data['lastServerHeartbeat'] else None
        self.total_seconds_played: int = data['totalSecondsPlayed']
        self.raw_data: dict = data


class LegoWorldGrant:

    def __init__(self, data: dict):
        self.namespace_id: str = data['namespaceId']
        self.world_id: str = data['worldId']
        self.account_id: str = data['accountId']
        self.role: LegoWorldGrantRole = LegoWorldGrantRole(data['roleId'])
        self.type: LegoWorldGrantType = LegoWorldGrantType(data['type'])
        self.granted_by: str = data['grantedBy']
        self.granted_at: datetime.datetime = datetime.datetime.fromisoformat(data['grantedAt'])
        try:
            self.expires_at: Optional[datetime.datetime] = datetime.datetime.fromisoformat(data['expiresAt'])
        except ValueError:
            self.expires_at: Optional[datetime.datetime] = None
        self.raw_data: dict = data

from datetime import datetime
from typing import List

from .utils import from_iso


class Code:

    def __init__(self, data: dict):
        self.code: str = data['code']
        self.namespace: str = data['namespace']
        self.creator: str = data['creator']
        self.created_at: datetime = from_iso(data['dateCreated'])
        self.starts_at: datetime = from_iso(data['startDate'])
        self.ends_at: datetime = from_iso(data['endDate'])
        self.allowed_users: list = data['allowedUsers']
        self.allowed_countries: list = data['allowedCountries']
        self.allowed_clients: list = data['allowedClients']
        self.distribution_metadata: dict = data['distributionMetadata']
        self.allowed_distribution_clients: list = data['allowedDistributionClients']
        self.code_type: str = data['codeType']
        self.max_uses: int = data['maxNumberOfUses']
        self.allow_repeated_uses_by_same_user: bool = data['allowRepeatedUsesBySameUser']
        self.use_count: int = data['useCount']
        self.completed_count: int = data['completedCount']
        self.consumption_metadata: ConsumptionMetadata = ConsumptionMetadata(data['consumptionMetadata'])
        self.code_status: str = data['codeStatus']
        self.batch_id: str = data['batchId']
        self.batch_number: int = data['batchNumber']
        self.labels: List[str] = data['labels']
        self.blocked_countries: list = data['blockedCountries']


class ConsumptionMetadata:

    def __init__(self, data: dict):
        self.namespace: str = data['namespace']
        self.offer_id: str = data['offerId']

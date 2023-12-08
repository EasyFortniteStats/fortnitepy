from datetime import datetime
from typing import List, Optional

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
        self.consumption_metadata: CodeConsumptionMetadata = CodeConsumptionMetadata(data['consumptionMetadata'])
        self.code_status: str = data['codeStatus']
        self.batch_id: str = data['batchId']
        self.batch_number: int = data['batchNumber']
        self.labels: List[str] = data['labels']
        self.blocked_countries: list = data['blockedCountries']
        self.raw_data: dict = data


class CodeConsumptionMetadata:

    def __init__(self, data: dict):
        self.criteria: Optional[CodeConsumptionCriteria] = CodeConsumptionCriteria(data['criteria']) \
            if data.get('criteria') else None
        self.namespace: str = data['namespace']
        self.offer_id: str = data['offerId']
        self.raw_data: dict = data


class CodeConsumptionCriteria:

    def __init__(self, data: dict):
        self.checks: List[CodeConsumptionCheck] = [CodeConsumptionCheck(check) for check in data['checks']]
        self.else_action: str = data['elseAction']
        self.reject_error_type: str = data['rejectErrorType']
        self.action: str = data['action']
        self.operator: str = data['operator']
        self.raw_data: dict = data


class CodeConsumptionCheck:

    def __init__(self, data: dict):
        self.data: str = data['data']
        self.type: str = data['type']
        self.raw_data: dict = data


class CodeRedemption:

    def __init__(self, data: dict):
        self.offer_id: str = data['offerId']
        self.account_id: str = data['accountId']
        self.identity_id: str = data['identityId']
        self.details: List[CodeRedemptionDetail] = [CodeRedemptionDetail(detail) for detail in data['details']]
        self.raw_data: dict = data


class CodeRedemptionDetail:

    def __init__(self, data: dict):
        self.entitlement_id: str = data['entitlementId']
        self.entitlement_name: str = data['entitlementName']
        self.item_id: str = data['itemId']
        self.namespace: str = data['namespace']
        self.country: str = data['country']
        self.raw_data: dict = data

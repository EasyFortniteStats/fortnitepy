from datetime import date, datetime
from typing import Optional, List

from .utils import from_iso


class SACEarnedProduct:

    def __init__(self, id_: str, data: dict):
        self.id: str = id_
        self.title: str = data['title']
        self.icon_url: str = data['icon']
        self.link: Optional[str] = data['link']
        self.share_rate: int = data['shareRate']
        self.url_slug: str = data['urlSlug']
        self.page_slug: str = data['pageSlug']
        self.data_entries: List[SACEarnedProductDataEntry] = [
            SACEarnedProductDataEntry(entry) for entry in data['data']
        ]
        self.total_unique_supporters: int = data['totalUniqueSupporters']
        self.total_estimated_earnings: int = data['totalEstimatedEarnings']
        self.raw_data: dict = data


class SACEarnedProductDataEntry:

    def __init__(self, data: dict):
        self.date: date = date.fromisoformat(data['date'])
        self.referrals: int = data['referrals']
        self.average_share_rate: int = data['avgShareRate']
        self.currency: str = data['currency']
        self.raw_data: dict = data


class SACEarnings:

    def __init__(self, data: dict):
        self.lifetime_payouts: int = data['lifetimePayouts']
        self.lifetime_payout_currency: str = data['lifetimePayoutCurrency']
        self.last_payout: int = data['lastPayout']
        self.last_payout_currency: str = data['lastPayoutCurrency']
        self.last_payout_at: datetime = from_iso(data['lastPayoutDate'])
        self.eligible_earnings: int = data['eligibleEarnings']
        self.eligible_earnings_currency: str = data['eligibleEarningsCurrency']

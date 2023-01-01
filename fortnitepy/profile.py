import datetime
from datetime import timedelta
from typing import Optional, List, Dict

from .enums import CosmeticType, PaymentPlatform
from .utils import from_iso


class BattleRoyaleProfile:

    def __init__(self, data: dict):
        self.items = [ItemProfile(item) for item in data['items'].values()]

        stats = data['stats']['attributes']

        self.account_level = stats['accountLevel']

        self.season: int = stats['season_num']
        self.season_level: int = stats['level']
        self.season_wins: int = stats.get('season', {}).get('numWins', 0)
        self.last_match_ended_at: Optional[datetime] = \
            from_iso(stats['last_match_end_datetime']) if stats['last_match_end_datetime'] else None

        self.total_season_battlestars: int = stats['battlestars_season_total']
        self.battle_stars: int = stats.get('battlestars', 0)
        self.purchased_battlepass_offers: List[PurchasedBattlePassOffer] = [
            PurchasedBattlePassOffer(offer) for offer in stats.get('purchased_bp_offers', [])
        ]

        self.total_season_style_points: int = stats.get('style_points_season_total', 0)
        self.style_points: int = stats.get('style_points', 0)

        self.lifetime_wins: int = stats['lifetime_wins']
        self.past_season_stats: List[PastSeasonStats] = [
            PastSeasonStats(ss) for ss in stats.get('past_seasons', [])
        ]

        self.saved_loadout_ids: List[str] = stats['loadouts']
        self.use_random_loadout = stats.get('use_random_loadout', False)
        self.last_applied_loadout_id: Optional[str] = stats.get('last_applied_loadout')

        self.season_match_boost: int = stats.get('season_match_boost', 0)
        self.season_friend_match_boost: int = stats.get('season_friend_match_boost', 0)

        self.has_claimed_2fa_reward: bool = stats['mfa_reward_claimed']

        self.party_assist_quest: Optional[str] = stats.get('party_assist_quest')

        self.xp = stats['xp']
        self.last_xp_interaction: datetime = from_iso(stats['last_xp_interaction'])
        self.supercharged_xp: int = stats.get('rested_xp', 0)
        self.supercharged_xp_multiplier: float = stats['rested_xp_mult']
        self.supercharged_xp_overflow: int = stats['rested_xp_overflow']
        self.supercharged_xp_exchange: float = stats['rested_xp_exchange']
        self.supercharged_xp_golden_path_granted: int = stats.get('rested_xp_golden_path_granted', 0)
        self.supercharged_xp_cumulative: int = stats.get('rested_xp_cumulative', 0)
        self.supercharged_xp_consumed_cumulative: int = stats.get('rested_xp_consumed_cumulative', 0)

        self.has_purchased_book: bool = stats.get('book_purchased', False)
        self.book_level: int = stats['book_level']
        self.book_xp: Optional[int] = stats.get('book_xp')

        self.creative_dynamic_xp: Optional[dict] = stats.get('creative_dynamic_xp')
        self.vote_data: Optional[dict] = stats.get('vote_data')

        self.raw_data = data

    def get_cosmetics(self, *cosmetic_types: CosmeticType) -> List["ItemProfile"]:
        if not cosmetic_types:
            cosmetic_types = list(CosmeticType)
        cosmetic_types = [c.value for c in cosmetic_types]
        return [item for item in self.items if item.type in cosmetic_types]

    def count_cosmetics(self) -> Dict[CosmeticType, int]:
        cosmetics = {}
        for item in self.items:
            cosmetic_type = CosmeticType(item.type)
            if item.type not in cosmetics:
                cosmetics[cosmetic_type] = 0
            cosmetics[cosmetic_type] += 1
        return cosmetics

    def get_legacies(self) -> List["ItemProfile"]:
        return [item for item in self.items if item.type == 'Accolades']

    def get_locker(self) -> "Locker":
        item = [item for item in self.items if item.type == 'CosmeticLocker'][0]
        return Locker(item.attributes)


class PastSeasonStats:

    def __init__(self, data: dict):
        self.season = data['seasonNumber']
        self.wins: int = data['numWins']
        self.xp: int = data['seasonXp']
        self.level: int = data['seasonLevel']
        self.has_purchased_battle_pass: bool = data['purchasedVIP']
        self.crown_wins: int = data['numRoyalRoyales']

        self.raw_data: dict = data


class PurchasedBattlePassOffer:

    def __init__(self, data: dict):
        self.offer_id: str = data['offerId']
        self.free_reward: bool = data['bIsFreePassReward']
        self.purchase_date: datetime = from_iso(data['purchaseDate'])
        self.items = [
            Item(item) for item in data['lootResult']
        ]
        self.currency: str = data['currencyType']
        self.currency_paid: int = data['totalCurrencyPaid']

        self.attributes: Optional[dict] = data.get('attributes')

        self.raw_data: dict = data


class Item:

    def __init__(self, data: dict):
        item_type_split = data['itemType'].split(':')
        self.type: str = item_type_split[0]
        self.id: str = item_type_split[1]
        self.guid: str = data['itemGuid']
        self.profile: str = data['itemProfile']
        self.quantity: int = data['quantity']


class ItemProfile:

    def __init__(self, data: dict):
        item_type_split = data['templateId'].split(':')
        self.type: str = item_type_split[0]
        self.id: str = item_type_split[1]
        self.attributes: dict = data['attributes']
        self.quantity: int = data['quantity']


class Locker:

    def __init__(self, data: dict):
        self.outfit: LockerSlot = LockerSlot(data['locker_slots_data']['slots']['Character'])
        self.backpack: LockerSlot = LockerSlot(data['locker_slots_data']['slots']['Backpack'])
        self.harvesting_tool: LockerSlot = LockerSlot(data['locker_slots_data']['slots']['Pickaxe'])
        self.glider: LockerSlot = LockerSlot(data['locker_slots_data']['slots']['Glider'])
        self.contrail: LockerSlot = LockerSlot(data['locker_slots_data']['slots']['SkyDiveContrail'])
        self.emote: LockerSlot = LockerSlot(data['locker_slots_data']['slots']['Dance'])
        self.music: LockerSlot = LockerSlot(data['locker_slots_data']['slots']['MusicPack'])
        self.wrap: LockerSlot = LockerSlot(data['locker_slots_data']['slots']['ItemWrap'])
        self.loading_screen: LockerSlot = LockerSlot(data['locker_slots_data']['slots']['LoadingScreen'])
        self.name: Optional[str] = data.get('locker_name')
        self.banner_icon_id: Optional[str] = data.get('banner_icon_template')
        self.banner_color_id: Optional[str] = data.get('banner_color_template')
        self.use_count: Optional[int] = data.get('useCount')


class LockerSlot:

    def __init__(self, data: dict):
        self.name: Optional[str] = data.get('locker_slot_name')
        self.use_count: int = data['useCount']
        self.item: Optional[ItemProfile] = data.get('item')


class CommonCoreProfile:

    def __init__(self, data: dict):
        self.items = [ItemProfile(item) for item in data['items'].values()]
        stats = data['stats']['attributes']

        self.survey_data: dict = stats['survey_data']
        self.intro_game_played: bool = stats['intro_game_played']
        self.vbucks_purchase_history = VBucksPurchaseHistory(stats['mtx_purchase_history']) \
            if stats.get('mtx_purchase_history') else None
        self.money_purchase_history = MoneyPurchaseHistory(stats['rmt_purchase_history']) \
            if stats.get('rmt_purchase_history') else None
        self.gift_history = GiftHistory(stats['gift_history']) if stats.get('gift_history') else None

        self.undo_cooldowns: List[UndoCooldown] = [UndoCooldown(cooldown) for cooldown in
                                                   stats.get('undo_cooldowns', [])]

        self.creator_code: Optional[str] = stats.get('mtx_affiliate')
        self.creator_code_owner_id: Optional[str] = stats.get('mtx_affiliate_id')
        self.creator_code_set_on: Optional[datetime] = from_iso(stats.get('mtx_affiliate_set_time'))

        self.current_vbucks_platform: PaymentPlatform = PaymentPlatform(stats['current_mtx_platform'])
        self.receipt_ids: List[str] = stats['in_app_purchases'].get('receipts', [])

        self.allowed_sending_gifts: bool = stats['allowed_to_send_gifts']
        self.allowed_receiving_gifts: bool = stats['allowed_to_receive_gifts']

        self.enabled_2fa = stats['mfa_enabled']

        self.raw_data: dict = data

    def get_overall_vbucks_count(self, platform: Optional[PaymentPlatform] = None, strict: bool = False) -> int:
        return sum((
            self.get_save_the_world_vbucks(),
            self.get_purchased_vbucks(platform, strict),
            self.get_free_obtained_vbucks()
        )) - self.get_vbucks_debt()

    def get_save_the_world_vbucks(self) -> int:
        return sum(item.quantity for item in self.items if item.type == 'Currency' and item.id == 'MtxComplimentary')

    def get_purchased_vbucks(self, platform: Optional[PaymentPlatform] = None, strict: bool = False) -> int:
        platforms = {platform}
        if not strict:
            if platform is not PaymentPlatform.NINTENDO:
                platforms = set(PaymentPlatform) - {PaymentPlatform.NINTENDO}
            else:
                platforms = {PaymentPlatform.NINTENDO}
        platforms = [platform.value for platform in platforms]

        return sum(
            item.quantity for item in self.items
            if item.type == 'Currency' and item.id == 'MtxPurchased' and
            (platform is None or item.attributes['platform'] in platforms)
        )

    def get_free_obtained_vbucks(self) -> int:
        return sum(item.quantity for item in self.items if item.id == 'MtxGiveaway')

    def get_vbucks_debt(self) -> int:
        return sum(item.quantity for item in self.items if item.id == 'MtxDebt')

    def get_banner(self) -> List[ItemProfile]:
        return [item for item in self.items if item.type == 'HomebaseBannerIcon']

    def get_banner_color(self):
        return [item for item in self.items if item.type == 'HomebaseBannerColor']

    def has_custom_games_access(self):
        return any(item.id == 'athenacancreatecustomgames_token' for item in self.items)

    def has_save_the_world_access(self):
        return any(item.id == 'campaignaccess' for item in self.items)


class VBucksPurchaseHistory:

    def __init__(self, data: dict):
        self.refunds_used: int = data['refundsUsed']
        self.refund_credits: int = data['refundCredits']
        self.next_refund_grant_at: Optional[datetime] = (
                from_iso(data['tokenRefreshReferenceTime']) + timedelta(days=365)
        ) if data.get('tokenRefreshReferenceTime') else None
        self.purchases: List[VBucksPurchase] = [VBucksPurchase(purchase) for purchase in data['purchases']]


class MoneyPurchaseHistory:

    def __init__(self, data: dict):
        self.purchases: List[MoneyPurchase] = [MoneyPurchase(purchase) for purchase in data['purchases']]


class GiftUser:

    def __init__(self, user_id: str, timestamp: str):
        self.user_id: str = user_id
        self.timestamp: datetime = from_iso(timestamp)


class Gift:

    def __init__(self, data: dict):
        self.date: datetime = from_iso(data['date'])
        self.offer_id: str = data['offerId']
        self.recipient_user_id: str = data['toAccountId']


class GiftHistory:

    def __init__(self, data: dict):
        self.sent_count: int = data['num_sent']
        self.received_count: int = data['num_received']
        self.sent_to: List[GiftUser] = [GiftUser(uid, ts) for uid, ts in data['sentTo'].items()]
        self.received_from: List[GiftUser] = [GiftUser(uid, ts) for uid, ts in data['receivedFrom'].items()]
        self.gifts: List[Gift] = [Gift(gift) for gift in data['gifts']]


class VBucksPurchase:
    def __init__(self, data: dict):
        self.id: str = data['purchaseId']
        self.offer_id: str = data['offerId']
        self.purchased_at: datetime = from_iso(data['purchaseDate'])
        self.free_refund_eligible: bool = data['freeRefundEligible']
        self.fulfillments: list = data['fulfillments']
        self.price: int = data['totalMtxPaid']
        self.creator_code: Optional[str] = data['metadata'].get('mtx_affiliate')
        self.creator_code_owner_id: Optional[str] = data['metadata'].get('mtx_affiliate_id')
        self.game_context: Optional[str] = data.get('gameContext')
        self.items: List[Item] = [Item(item) for item in data['lootResult']]


class MoneyPurchase:
    def __init__(self, data: dict):
        self.fulfillment_id: str = data['fulfillmentId']
        self.purchased_at: datetime = from_iso(data['purchaseDate'])
        self.items: List[Item] = [Item(item) for item in data['lootResult']]


class UndoCooldown:

    def __init__(self, data: dict):
        self.offer_id: str = data['offerId']
        self.expires_at: datetime = from_iso(data['cooldownExpires'])

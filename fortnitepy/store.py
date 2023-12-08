# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2019-2021 Terbau

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import dataclasses
import re
import datetime
from dataclasses import dataclass

from typing import TYPE_CHECKING, Optional, List

from .utils import from_iso

if TYPE_CHECKING:
    from .client import Client


class StoreItemBase:
    def __init__(self, data: dict) -> None:
        self._dev_name = data['devName']
        self._asset_path = data.get('displayAssetPath')

        try:
            self._asset = re.search(r'\.(.+)', self._asset_path).group(1)
        except (TypeError, AttributeError):
            self._asset = None

        self._gifts_enabled = (data['giftInfo']['bIsEnabled']
                               if 'giftInfo' in data else False)
        self._daily_limit = data['dailyLimit']
        self._weekly_limit = data['weeklyLimit']
        self._monthly_limit = data['monthlyLimit']
        self._offer_id = data['offerId']
        self._offer_type = data['offerType']
        self._price = data['prices'][0]['finalPrice']
        self._refundable = data['refundable']
        self._items_grants = data['itemGrants']
        self._meta_info = data.get('metaInfo', [])
        self._meta = data.get('meta', {})

    def __str__(self) -> str:
        return self.dev_name

    @property
    def display_names(self) -> List[str]:
        """List[:class:`str`]: The display names for this item."""
        match = re.search(r'^\[VIRTUAL][0-9]+ x (.*) for [0-9]+ .*$',
                          self._dev_name).group(1)
        return re.split(r', [0-9]+ x ', match)

    @property
    def dev_name(self) -> str:
        """:class:`str`: The dev name of this item."""
        return self._dev_name

    @property
    def asset_path(self) -> Optional[str]:
        """:class:`str`: The asset path of the item. Could be ``None`` if
        not found.
        """
        return self._asset_path

    @property
    def asset(self) -> Optional[str]:
        """:class:`str`: The asset of the item. Usually a CID or
        or something similar. Could be ``None`` if not found.
        """
        return self._asset

    @property
    def encryption_key(self) -> Optional[str]:
        """:class:`str`: The encryption key for this item. If no encryption
        key is found, this will be ``None``.
        """
        for meta in self._meta_info:
            if meta['key'] == 'EncryptionKey':
                return meta['value']

    @property
    def gifts_enabled(self) -> bool:
        """:class:`bool`: ``True`` if gifts is enabled for this
        item else ``False``.
        """
        return self._gifts_enabled

    @property
    def daily_limit(self) -> int:
        """:class:`int`: The daily account limit for this item.
        ``-1`` = Unlimited.
        """
        return self._daily_limit

    @property
    def weekly_limit(self) -> int:
        """:class:`int`: The weekly account limit for this item.
        ``-1`` = Unlimited.
        """
        return self._weekly_limit

    @property
    def monthly_limit(self) -> int:
        """:class:`int`: The monthly account limit for this item.
        ``-1`` = Unlimited.
        """
        return self._monthly_limit

    @property
    def offer_id(self) -> str:
        """:class:`str`: The offer id of this item."""
        return self._offer_id

    @property
    def offer_type(self) -> str:
        """:class:`str`: The offer type of this item."""
        return self._offer_type

    @property
    def price(self) -> int:
        """:class:`int`: The price of this item in v-bucks."""
        return self._price

    @property
    def refundable(self) -> bool:
        """:class:`bool`: ``True`` if item is refundable else
        ``False``.
        """
        return self._refundable

    @property
    def grants(self) -> List[dict]:
        """:class:`list`: A list of items you get from this purchase.

        Typical output: ::

            [{
                'quantity': 1,
                'type': 'AthenaCharacter',
                'asset': 'cid_318_athena_commando_m_demon'
            }]
        """
        grants = []
        for item in self._items_grants:
            _type, _asset = item['templateId'].split(':')
            grants.append({
                'quantity': item['quantity'],
                'type': _type,
                'asset': _asset
            })
        return grants

    @property
    def new(self) -> bool:
        """:class:`bool`: ``True`` if the item is in the item shop for
        the first time, else ``False``.
        """
        for meta in self._meta_info:
            if meta['value'].lower() == 'new':
                return True
        return False

    @property
    def violator(self) -> Optional[str]:
        """:class:`str`: The violator of this item. Violator is the
        red tag at the top of an item in the shop. Will be ``None``
        if no violator is found for this item.
        """
        unfixed = self._meta.get('BannerOverride')
        if unfixed:
            return ' '.join(re.findall(r'[A-Z][^A-Z]*', unfixed))


class FeaturedStoreItem(StoreItemBase):
    """Featured store item."""
    def __init__(self, data: dict) -> None:
        super().__init__(data)
        self._panel = int((data['categories'][0].split(' '))[1])

    def __repr__(self) -> str:
        return ('<FeaturedStoreItem dev_name={0.dev_name!r} asset={0.asset!r} '
                'price={0.price!r}>'.format(self))

    @property
    def panel(self) -> int:
        """:class:`int`: The panel the item is listed in from left
        to right.
        """
        return self._panel


class DailyStoreItem(StoreItemBase):
    """Daily store item."""
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    def __repr__(self) -> str:
        return ('<DailyStoreItem dev_name={0.dev_name!r} asset={0.asset!r} '
                'price={0.price!r}>'.format(self))


class Store:
    """Object representing store data from Fortnite Battle Royale.

    Attributes
    ----------
    client: :class:`Client`
        The client.
    """
    def __init__(self, client: 'Client', data: dict) -> None:
        self.client = client
        self._daily_purchase_hours = data['dailyPurchaseHrs']
        self._refresh_interval_hours = data['refreshIntervalHrs']
        self._expires_at = from_iso(data['expiration'])

        self._featured_items = self._create_featured_items(
            'BRWeeklyStorefront',
            data
        )
        self._daily_items = self._create_daily_items(
            'BRDailyStorefront',
            data
        )
        self._special_featured_items = self._create_featured_items(
            'BRSpecialFeatured',
            data
        )
        self._special_daily_items = self._create_daily_items(
            'BRSpecialDaily',
            data,
        )

    def __repr__(self) -> str:
        return ('<Store created_at={0.created_at!r} '
                'expires_at={0.expires_at!r}>'.format(self))

    @property
    def featured_items(self) -> List[FeaturedStoreItem]:
        """List[:class:`FeaturedStoreItem`]: A list containing data about
        featured items in the item shop.
        """
        return self._featured_items

    @property
    def daily_items(self) -> List[DailyStoreItem]:
        """List[:class:`DailyStoreItem`]: A list containing data about
        daily items in the item shop.
        """
        return self._daily_items

    @property
    def special_featured_items(self) -> List[FeaturedStoreItem]:
        """List[:class:`FeaturedStoreItem`]: A list containing data about
        special featured items in the item shop.
        """
        return self._special_featured_items

    @property
    def special_daily_items(self) -> List[DailyStoreItem]:
        """List[:class:`DailyStoreItem`]: A list containing data about
        special daily items in the item shop.
        """
        return self._special_daily_items

    @property
    def daily_purchase_hours(self) -> int:
        """:class:`int`: How many hours a day it is possible to purchase
        items. It most likely is ``24``.
        """
        return self._daily_purchase_hours

    @property
    def refresh_interval_hours(self) -> int:
        """:class:`int`: Refresh interval hours."""
        return self._refresh_interval_hours

    @property
    def created_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: The UTC time of the creation
        and current day.
        """
        return self._expires_at - datetime.timedelta(days=1)

    @property
    def expires_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: The UTC time of when this
        item shop expires.
        """
        return self._expires_at

    def _find_storefront(self, data: dict, key: str) -> Optional[dict]:
        for storefront in data['storefronts']:
            if storefront['name'] == key:
                return storefront

    def _create_featured_items(self, storefront: str,
                               data: dict) -> List[FeaturedStoreItem]:
        storefront = self._find_storefront(data, storefront)

        res = []
        for item in storefront['catalogEntries']:
            res.append(FeaturedStoreItem(item))
        return res

    def _create_daily_items(self, storefront: str,
                            data: dict) -> List[DailyStoreItem]:
        storefront = self._find_storefront(data, storefront)

        res = []
        for item in storefront['catalogEntries']:
            res.append(DailyStoreItem(item))
        return res


class CatalogEntry:

    def __init__(self, data: dict) -> None:
        self.id: str = data['id']
        self.title: str = data['title']
        self.description: str = data['description']
        self.long_description: str = data['longDescription']
        self.key_images: List[CatalogEntryKeyImage] = [
            CatalogEntryKeyImage(image) for image in data.get('keyImages', [])
        ]
        self.categories: List = data['categories']
        self.namespace: str = data['namespace']
        self.status: str = data['status']
        self.created_at: datetime.datetime = from_iso(data['creationDate'])
        self.last_modified_at: datetime.datetime = from_iso(data['lastModifiedDate'])
        self.custom_attributes: dict = data['customAttributes']
        self.internal_name: str = data['internalName']
        self.recurrence: str = data['recurrence']
        self.items: List[CatalogEntryItem] = [CatalogEntryItem(item) for item in data['items']]
        self.currency_code: str = data['currencyCode']
        self.current_price: int = data['currentPrice']
        self.price: int = data['price']
        self.base_price: int = data['basePrice']
        self.recurring_price: int = data['recurringPrice']
        self.free_days: int = data['freeDays']
        self.max_billing_cycles: int = data['maxBillingCycles']
        self.seller: CatalogEntrySeller = CatalogEntrySeller(data['seller'])
        self.effective_at: datetime.datetime = from_iso(data['effectiveDate'])
        self.vat_included: bool = data['vatIncluded']
        self.is_code_redemption_only: bool = data['isCodeRedemptionOnly']
        self.is_featured: bool = data['isFeatured']
        self.tax_sku_id: str = data['taxSkuId']
        self.merchant_group: str = data['merchantGroup']
        self.price_tier: str = data['priceTier']
        self.url_slug: str = data['urlSlug']
        self.role_names_to_grant: List = data['roleNamesToGrant']
        self.tags: List = data['tags']
        self.purchase_limit: int = data['purchaseLimit']
        self.ignore_order: bool = data['ignoreOrder']
        self.fullfill_to_group: bool = data['fulfillToGroup']
        self.fraud_item_type: str = data['fraudItemType']
        self.share_revenue: bool = data['shareRevenue']
        self.unsearchable: bool = data['unsearchable']
        self.release_offer: str = data['releaseOffer']
        self.sort_title: str = data['title4Sort']
        self.self_refundable: bool = data['selfRefundable']
        self.refund_type: str = data['refundType']
        self.price_calculation_mode: str = data['priceCalculationMode']
        self.assemble_mode: str = data['assembleMode']
        self.currency_decimals: int = data['currencyDecimals']
        self.allow_purchase_for_partial_owned: bool = data['allowPurchaseForPartialOwned']
        self.share_revenue_with_underage_affiliates: bool = data['shareRevenueWithUnderageAffiliates']
        self.platform_whitelist: List = data['platformWhitelist']
        self.platform_blacklist: List = data['platformBlacklist']
        self.partial_item_prerequisite_check: bool = data['partialItemPrerequisiteCheck']
        self.upgrade_mode: str = data['upgradeMode']
        self.raw_data: dict = data


class CatalogEntryKeyImage:

    def __init__(self, data: dict) -> None:
        self.type: str = data['type']
        self.url: str = data['url']
        self.md5: str = data['md5']
        self.width: int = data['width']
        self.height: int = data['height']
        self.size: int = data['size']
        self.uploaded_at: datetime.datetime = from_iso(data['uploadedDate'])
        self.raw_data: dict = data


class CatalogEntryItem:

    def __init__(self, data: dict) -> None:
        self.id: str = data['id']
        self.title: Optional[str] = data.get('title')
        self.description: Optional[str] = data.get('description')
        self.categories: List = data['categories']
        self.namespace: str = data['namespace']
        self.status: Optional[str] = data.get('status')
        self.created_at: Optional[datetime.datetime] = (
            from_iso(data['creationDate']) if data.get('creationDate') else None
        )
        self.last_modified_at: Optional[datetime.datetime] = (
            from_iso(data['lastModifiedDate']) if data.get('lastModifiedDate') else None
        )
        self.custom_attributes: Optional[dict] = data.get('customAttributes')
        self.entitlement_name: Optional[str] = data.get('entitlementName')
        self.entitlement_type: Optional[str] = data.get('entitlementType')
        self.item_type: Optional[str] = data.get('itemType')
        self.release_info: Optional[List] = data.get('releaseInfo')
        self.developer: Optional[str] = data.get('developer')
        self.developer_id: Optional[str] = data.get('developerId')
        self.use_count: Optional[int] = data.get('useCount')
        self.eula_ids: Optional[List] = data.get('eulaIds')
        self.end_of_support: Optional[bool] = data.get('endOfSupport')
        self.ns_major_items: Optional[List] = data.get('nsMajorItems')
        self.ns_depends_on_dlc_items: Optional[List] = data.get('nsDependsOnDlcItems')
        self.age_gatings: Optional[dict] = data.get('ageGatings')
        self.application_id: Optional[str] = data.get('applicationId')
        self.requires_secure_account: Optional[bool] = data.get('requiresSecureAccount')
        self.unsearchable: bool = data['unsearchable']
        self.raw_data: dict = data


class CatalogEntrySeller:

    def __init__(self, data: dict) -> None:
        self.id: str = data['id']
        self.name: str = data['name']


@dataclass
class ItemPurchase:
    offer_id: str
    currency_type: str
    currency_sub_type: str
    expected_price: int
    quantity: int = 1

    def to_payload(self) -> dict:
        return {
            'offerId': self.offer_id,
            'purchaseQuantity': self.quantity,
            'currency': self.currency_type,
            'currencySubType': self.currency_sub_type,
            'expectedTotalPrice': self.expected_price,
            'gameContext': 'GameContext: Frontend.CatabaScreen'
        }

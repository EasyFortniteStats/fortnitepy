import datetime
from typing import Dict, Any, List, Optional


class WebShop:

    def __init__(self, data: Dict[str, Any]):
        self.categories: List[WebShopCategory] = [WebShopCategory(category) for category in data.get('categories', [])]

class WebShopCategory:

    def __init__(self, data: Dict[str, Any]):
        self.nav_label: str = data['navLabel']
        self.sections: List[WebShopSection] = [WebShopSection(section) for section in data.get('sections', [])]


class WebShopSection:

    def __init__(self, data: Dict[str, Any]):
        self.id = data['sectionID']
        self.stack_rank: int = data['stackRank']
        self.display_name: str = data['displayName']
        self.section_id: str = data['sectionId']
        self.category_name: str = data['categoryName']
        self.offer_groups: List[WebShopOfferGroup] = [WebShopOfferGroup(offer_group) for offer_group in data.get('offerGroups', [])]

class WebShopOfferGroup:

    def __init__(self, data: Dict[str, Any]):
        self.id = data['offerGroupId']
        self.display_type: str = data['displayType']
        self.items: List[WebShopItem] = [WebShopItem(item) for item in data.get('items', [])]

class WebShopItem:

    def __init__(self, data: Dict[str, Any]):
        self.asset_type: str = data['assetType']
        self.has_variants: bool = data['hasVariants']
        self.has_tags: bool = data['hasTags']
        self.offer_id: Optional[str] = data.get('offerId')
        self.image: WebShopItemImage = WebShopItemImage(data['image'])
        self.title: str = data['title']
        self.artist: Optional[str] = data.get('artist')
        self.english_title: str = data['englishTitle']
        self.url_name: str = data['urlName']
        self.callout: Optional[WebShopItemCallout] = WebShopItemCallout(data['callout']) if data.get('callout') else None
        self.size: WebShopItemSize = WebShopItemSize(data['size'])
        self.color1: Optional[str] = data.get('color1')
        self.color2: Optional[str] = data.get('color2')
        self.color3: Optional[str] = data.get('color3')
        self.text_background_color: Optional[str] = data.get('textBackgroundColor')
        self.layout_id: str = data['layoutId']
        self.pricing: WebShopItemPricing = WebShopItemPricing(data['pricing'])
        self.ownership_calculation: WebShopItemOwnershipCalculation = WebShopItemOwnershipCalculation(data['ownershipCalculationData'])
        self.app_store_ids: List[str] = data.get('appStoreId', [])
        self.in_date: datetime.datetime = datetime.datetime.fromtimestamp(data['inDate'])
        self.out_date: datetime.datetime = datetime.datetime.fromtimestamp(data['outDate'])
        self.new_until: Optional[datetime.datetime] = datetime.datetime.fromtimestamp(data['newUntil']) if data.get('newUntil') else None


class WebShopItemImage:

    def __init__(self, data: Dict[str, Any]):
        self.small: str = data['sm']
        self.medium: str = data['md']
        self.large: str = data['lg']
        self.tall: str = data['tall']
        self.wide: str = data['wide']

class WebShopItemCallout:

        def __init__(self, data: Dict[str, Any]):
            self.text: str = data['text']
            self.intensity: str = data['intensity']

class WebShopItemSize:

        def __init__(self, data: Dict[str, Any]):
            self.rows: int = data['rows']
            self.columns: int = data['columns']

class WebShopItemPricing:

    def __init__(self, data: Dict[str, Any]):
        self.final_price: int = data['finalPrice']
        self.base_price: int = data['basePrice']
        self.amount_off: int = data['amountOff']
        self.currency_type: Optional[str] = data.get('currencyType')
        self.currency_code: Optional[str] = data.get('currencyCode')
        self.currency_decimals: Optional[int] = data.get('currencyDecimals')

class WebShopItemOwnershipCalculation:

    def __init__(self, data: Dict[str, Any]):
        self.item_grant_template_ids: List[str] = data['itemGrantTemplateIds']
        self.dynamic_bundle_pricing: Optional[WebShopItemDynamicBundlePricing] = WebShopItemDynamicBundlePricing(data['dynamicBundlePricingData']) if data.get('dynamicBundlePricingData') else None


class WebShopItemDynamicBundlePricing:

    def __init__(self, data: Dict[str, Any]):
        self.item_grant_template_ids: List[str] = data['itemGrantTemplateIds']
        self.floor_price: int = data['floorPrice']
        self.discounted_base_price: int = data['discountedBasePrice']
        self.currency_type: str = data['currencyType']
        self.bundle_items: List[WebShopItemDynamicBundlePricingItem] = [WebShopItemDynamicBundlePricingItem(item) for item in data['bundleItems']]

class WebShopItemDynamicBundlePricingItem:

    def __init__(self, data: Dict[str, Any]):
        self.regular_price: int = data['regularPrice']
        self.already_owned_price_reduction: int = data['alreadyOwnedPriceReduction']
        self.item: str = data['item']['templateId']
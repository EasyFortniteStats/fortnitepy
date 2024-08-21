# -*- coding: utf-8 -*-
# flake8: noqa

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

import random
import types

from typing import Optional, Any
from enum import Enum as OriginalEnum


class Enum(OriginalEnum):
    @classmethod
    def get_random_member(cls) -> Optional[Any]:
        try:
            return cls[random.choice(cls._member_names_)]
        except IndexError:
            pass

    @classmethod
    def get_random_name(cls) -> Optional[Any]:
        member = cls.get_random_member()
        if member is not None:
            return member.name

    @classmethod
    def get_random_value(cls) -> Optional[Any]:
        member = cls.get_random_member()
        if member is not None:
            return member.value


class PartyPrivacy(Enum):
    PUBLIC = {
        'partyType': 'Public',
        'inviteRestriction': 'AnyMember',
        'onlyLeaderFriendsCanJoin': False,
        'presencePermission': 'Anyone',
        'invitePermission': 'Anyone',
        'acceptingMembers': True,
    }
    FRIENDS_ALLOW_FRIENDS_OF_FRIENDS = {
        'partyType': 'FriendsOnly',
        'inviteRestriction': 'AnyMember',
        'onlyLeaderFriendsCanJoin': False,
        'presencePermission': 'Anyone',
        'invitePermission': 'AnyMember',
        'acceptingMembers': True,
    }
    FRIENDS = {
        'partyType': 'FriendsOnly',
        'inviteRestriction': 'LeaderOnly',
        'onlyLeaderFriendsCanJoin': True,
        'presencePermission': 'Leader',
        'invitePermission': 'Leader',
        'acceptingMembers': False,
    }
    PRIVATE_ALLOW_FRIENDS_OF_FRIENDS = {
        'partyType': 'Private',
        'inviteRestriction': 'AnyMember',
        'onlyLeaderFriendsCanJoin': False,
        'presencePermission': 'Noone',
        'invitePermission': 'AnyMember',
        'acceptingMembers': False,
    }
    PRIVATE = {
        'partyType': 'Private',
        'inviteRestriction': 'LeaderOnly',
        'onlyLeaderFriendsCanJoin': True,
        'presencePermission': 'Noone',
        'invitePermission': 'Leader',
        'acceptingMembers': False,
    }


class PartyDiscoverability(Enum):
    ALL = 'ALL'
    INVITED_ONLY = 'INVITED_ONLY'


class PartyJoinability(Enum):
    OPEN = 'OPEN'
    INVITE_ONLY = 'INVITE_ONLY'
    INVITE_AND_FORMER = 'INVITE_AND_FORMER'


class DefaultCharactersChapter1(Enum):
    CID_001_Athena_Commando_F_Default = 1
    CID_002_Athena_Commando_F_Default = 2
    CID_003_Athena_Commando_F_Default = 3
    CID_004_Athena_Commando_F_Default = 4
    CID_005_Athena_Commando_M_Default = 5
    CID_006_Athena_Commando_M_Default = 6
    CID_007_Athena_Commando_M_Default = 7
    CID_008_Athena_Commando_M_Default = 8


class DefaultCharactersChapter2(Enum):
    CID_556_Athena_Commando_F_RebirthDefaultA = 1
    CID_557_Athena_Commando_F_RebirthDefaultB = 2
    CID_558_Athena_Commando_F_RebirthDefaultC = 3
    CID_559_Athena_Commando_F_RebirthDefaultD = 4
    CID_560_Athena_Commando_M_RebirthDefaultA = 5
    CID_561_Athena_Commando_M_RebirthDefaultB = 6
    CID_562_Athena_Commando_M_RebirthDefaultC = 7
    CID_563_Athena_Commando_M_RebirthDefaultD = 8


class V1Gamemode(Enum):
    SOLO = 'p2'
    DUO = 'p10'
    SQUAD = 'p9'


class V1Platform(Enum):
    PC = 'pc'
    XBOX = 'xb1'
    PS4 = 'ps4'


class V1Window(Enum):
    ALLTIME = 'alltime'
    WEEKLY = 'weekly'


class V2Input(Enum):
    KEYBOARDANDMOUSE = 'keyboardmouse'
    GAMEPAD = 'gamepad'
    TOUCH = 'touch'


class Region(Enum):
    NAEAST = 'NAE'
    NAWEST = 'NAW'
    EUROPE = 'EU'
    BRAZIL = 'BR'
    OCEANIA = 'OCE'
    ASIA = 'ASIA'
    MIDDLEEAST = 'ME'


class Platform(Enum):
    WINDOWS = 'WIN'
    MAC = 'MAC'
    PLAYSTATION = 'PSN'
    PLAYSTATION_4 = 'PSN'
    PLAYSTATION_5 = 'PS5'
    XBOX = 'XBL'
    XBOX_ONE = 'XBL'
    XBOX_X = 'XSX'
    SWITCH = 'SWT'
    IOS = 'IOS'
    ANDROID = 'AND'


class UserSearchPlatform(Enum):
    EPIC_GAMES = 'epic'
    PLAYSTATION = 'psn'
    XBOX = 'xbl'
    STEAM = 'steam'


class UserSearchMatchType(Enum):
    EXACT = 'exact'
    PREFIX = 'prefix'


class ReadyState(Enum):
    READY = 'Ready'
    NOT_READY = 'NotReady'
    SITTING_OUT = 'SittingOut'


class AwayStatus(Enum):
    ONLINE = None
    AWAY = 'away'
    EXTENDED_AWAY = 'xa'


class SeasonStartTimestamp(Enum):
    SEASON_1 = 1508889601
    SEASON_2 = 1513209601
    SEASON_3 = 1519257601
    SEASON_4 = 1525132801
    SEASON_5 = 1531353601
    SEASON_6 = 1538006401
    SEASON_7 = 1544054401
    SEASON_8 = 1551312001
    SEASON_9 = 1557360001
    SEASON_10 = 1564617601
    SEASON_11 = 1571097601
    SEASON_12 = 1582156801
    SEASON_13 = 1592352001
    SEASON_14 = 1598486401
    SEASON_15 = 1606867201
    SEASON_16 = 1615852801
    SEASON_17 = 1623110401
    SEASON_18 = 1631491201


class SeasonEndTimestamp(Enum):
    SEASON_1 = 1513123200
    SEASON_2 = 1519171200
    SEASON_3 = 1525046400
    SEASON_4 = 1531353600
    SEASON_5 = 1538006400
    SEASON_6 = 1544054400
    SEASON_7 = 1551312000
    SEASON_8 = 1557360000
    SEASON_9 = 1564617600
    SEASON_10 = 1570924800
    SEASON_11 = 1582156800
    SEASON_12 = 1592352000
    SEASON_13 = 1598486400
    SEASON_14 = 1606867200
    SEASON_15 = 1615852800
    SEASON_16 = 1623110400
    SEASON_17 = 1631491200


class BattlePassStat(Enum):
    SEASON_11 = ('s11_social_bp_level', SeasonEndTimestamp.SEASON_11.value)
    SEASON_12 = ('s11_social_bp_level', SeasonEndTimestamp.SEASON_12.value)
    SEASON_13 = (('s13_social_bp_level', 's11_social_bp_level'), SeasonEndTimestamp.SEASON_13.value)
    SEASON_14 = ('s14_social_bp_level', SeasonEndTimestamp.SEASON_14.value)
    SEASON_15 = ('s15_social_bp_level', SeasonEndTimestamp.SEASON_15.value)
    SEASON_16 = ('s16_social_bp_level', SeasonEndTimestamp.SEASON_16.value)
    SEASON_17 = ('s17_social_bp_level', SeasonEndTimestamp.SEASON_17.value)
    SEASON_18 = ('s18_social_bp_level', None)


class RankingType(Enum):
    BATTLE_ROYALE = 'ranked-br'
    ZERO_BUILD = 'ranked-zb'
    ROCKET_RACING = 'delmar-competitive'


class StatsCollectionType(Enum):
    FISH = 'collection_fish'


class Profile(Enum):
    BATTLE_ROYALE = 'athena'
    SAVE_THE_WORLD = 'campaign'
    COMMON = 'common_core'
    COMMON_PUBLIC = 'common_public'


class VBucksPlatform(Enum):
    EPIC = 'Epic'
    PC = 'EpicPC'
    ANDROID = 'EpicAndroid'
    IOS = 'EpicIOS'
    PLAYSTATION = 'PSN'
    XBOX = 'Live'
    NINTENDO = 'Nintendo'
    SAMSUNG = 'Samsung'
    WE_GAME = 'WeGame'
    PC_KOREA = 'EpicPCKorea'
    GOOGLE_PLAY = 'GooglePlay'
    APP_STORE = 'IOSAppStore'
    SHARED = 'Shared'


class CosmeticType(Enum):
    OUTFIT = 'AthenaCharacter'
    BACKPACK = 'AthenaBackpack'
    PET = 'AthenaPet'
    PET_CARRIER = 'AthenaPetCarrier'
    PICKAXE = 'AthenaPickaxe'
    GLIDER = 'AthenaGlider'
    CONTRAIL = 'AthenaSkyDiveContrail'
    AURA = 'SparksAura'

    EMOTE = 'AthenaDance'
    EMOTICON = 'AthenaEmoji'
    SPRAY = 'AthenaSpray'
    TOY = 'AthenaToy'

    WRAP = 'AthenaItemWrap'

    #  BANNER = 'BannerToken'
    LOBBY_MUSIC = 'AthenaMusicPack'
    LOADING_SCREEN = 'AthenaLoadingScreen'

    GUITAR = 'SparksGuitar'
    BASS = 'SparksBass'
    DRUMS = 'SparksDrums'
    MICROPHONE = 'SparksMicrophone'
    KEYTAR = 'SparksKeyboard'

    CAR_BODY = 'VehicleCosmetics_Body'
    DECAL = 'VehicleCosmetics_Skin'
    WHEEL = 'VehicleCosmetics_Wheel'
    TRAIL = 'VehicleCosmetics_DriftTrail'
    BOOST = 'VehicleCosmetics_Booster'

    JAM_TRACK = 'SparksSong'

    LEGO_BUILD = 'JunoBuildingSet'
    LEGO_DECOR_BUNDLE = 'JunoBuildingProp'


class SaveTheWorldFounderPack(Enum):
    STANDARD = 1
    DELUXE = 2
    SUPER_DELUXE = 3
    LIMITED = 4
    ULTIMATE = 5


class DiscoverySurface(Enum):
    MAIN = 'CreativeDiscoverySurface_Frontend'
    BROWSE = 'CreativeDiscoverySurface_Browse'
    LIBRARY = 'CreativeDiscoverySurface_Library'
    ROCKET_RACING = 'CreativeDiscoverySurface_DelMar_TrackAndExperience'


class DiscoverySearchOrderType(Enum):
    PLAYER_COUNT = 'globalCCU'


class _RatingAuthorityRating(Enum):
    @staticmethod
    def get_authority():
        raise NotImplementedError


class ACBRating(_RatingAuthorityRating):
    AGE_R18 = 'ACB_AGE_R18'
    AGE_MA15 = 'ACB_AGE_MA15'
    AGE_M = 'ACB_AGE_M'
    AGE_PG = 'ACB_AGE_PG'
    AGE_G = 'ACB_AGE_G'
    AGE_NA = 'ACB_AGE_NA'

    @staticmethod
    def get_authority():
        return 'ACB'


class PEGIRating(_RatingAuthorityRating):
    AGE_18 = 'PEGI_AGE_18'
    AGE_16 = 'PEGI_AGE_16'
    AGE_12 = 'PEGI_AGE_12'
    AGE_7 = 'PEGI_AGE_7'
    AGE_3 = 'PEGI_AGE_3'
    AGE_PG = 'PEGI_AGE_PG'

    @staticmethod
    def get_authority():
        return 'PEGI'


class GenericRating(_RatingAuthorityRating):
    # AGE_18 = 'GEN_AGE_18'
    # AGE_16 = 'GEN_AGE_16'
    AGE_12 = 'GEN_AGE_12'
    AGE_7 = 'GEN_AGE_7'
    AGE_3 = 'GEN_AGE_3'

    @staticmethod
    def get_authority():
        return 'Generic'


class ClassIndRating(_RatingAuthorityRating):
    # AGE_18 = 'CLASSIND_AGE_18'
    # AGE_16 = 'CLASSIND_AGE_16'
    AGE_14 = 'CLASSIND_AGE_14'
    AGE_12 = 'CLASSIND_AGE_12'
    AGE_10 = 'CLASSIND_AGE_10'
    AGE_LIVRE = 'CLASSIND_AGE_LIVRE'

    @staticmethod
    def get_authority():
        return 'ClassInd'


class USKRating(_RatingAuthorityRating):
    AGE_18 = 'USK_AGE_18'
    AGE_16 = 'USK_AGE_16'
    AGE_12 = 'USK_AGE_12'
    AGE_6 = 'USK_AGE_6'
    AGE_0 = 'USK_AGE_0'

    @staticmethod
    def get_authority():
        return 'USK'


class GRACRating(_RatingAuthorityRating):
    # AGE_18 = 'GRAC_AGE_18'
    AGE_15 = 'GRAC_AGE_15'
    AGE_12 = 'GRAC_AGE_12'
    AGE_RC = 'GRAC_AGE_RC'
    AGE_ALL = 'GRAC_AGE_ALL'
    AGE_NA = 'GRAC_AGE_NA'

    @staticmethod
    def get_authority():
        return 'GRAC'


class ESRBRating(_RatingAuthorityRating):
    # Age 18 missing (A or AO)
    AGE_M = 'ESRB_AGE_M'
    AGE_T = 'ESRB_AGE_T'
    AGE_E10 = 'ESRB_AGE_E10'
    AGE_E = 'ESRB_AGE_E'

    @staticmethod
    def get_authority():
        return 'ESRB'


class RussiaRating(_RatingAuthorityRating):
    AGE_18 = 'RUSSIA_AGE_18'
    AGE_16 = 'RUSSIA_AGE_16'
    AGE_12 = 'RUSSIA_AGE_12'
    AGE_6 = 'RUSSIA_AGE_6'
    AGE_0 = 'RUSSIA_AGE_0'

    @staticmethod
    def get_authority():
        return 'Russia'


class CERORating(_RatingAuthorityRating):
    AGE_0 = 'CERO_AGE_0'
    AGE_15 = 'CERO_AGE_15'

    @staticmethod
    def get_authority():
        return 'CERO'


class PurchaseRefreshType(Enum):
    DEFAULT = 'Default'
    UPDATE_OFFLINE_AUTH = 'UpdateOfflineAuth'
    FORCE_ALL = 'ForceAll'
    FORCE_CURRENT = 'ForceCurrent'


class VerifierModeOverride(Enum):
    OCCURRENCE_PRIMARY = 'OccurrencePrimary'
    RECEIPT_ONLY = 'ReceiptOnly'
    RECEIPT_PRIMARY = 'ReceiptPrimary'
    DEFAULT_TOLAP_VERSION = 'DefaultToIapVersion'
    OCCURRENCE_ONLY = 'OccurrenceOnly'
    DEFAULT_TO_CONFIG = 'DefaultToConfig'
    OCCURRENCE_ONLY_REMOVE_RECEIPTS = 'OccurrenceOnlyRemoveReceipts'


class LegoWorldMode(Enum):
    COZY = 'Cozy'
    SURVIVAL = 'Survival'
    SANDBOX = 'Sandbox'
    HARDCORE = 'Hardcore'

class LegoWorldDifficulty(Enum):
    EASY = 'Easy'
    NORMAL = 'Normal'
    HARDCORE = 'Hardcore'

class LegoWorldDeathType(Enum):
    ON = 'On'
    OFF = 'Off'
    PERMANENT = 'Permanent'


class LegoWorldMetadataConstraint(Enum):
    DEFAULT = 'juno_default'
    NO_METADATA = 'nometadata'


class LegoWorldGrantRole(Enum):
    WORLD_OWNER = 'world_owner'
    KEYHOLDER = 'juno_keyholder'


class LegoWorldGrantType(Enum):
    PERSISTENT = 'PERSISTENT'

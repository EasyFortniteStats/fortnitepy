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


class StatsCollectionType(Enum):
    FISH = 'collection_fish'


class Profile(Enum):
    BATTLE_ROYALE = 'athena'
    SAVE_THE_WORLD = 'campaign'
    COMMON = 'common_core'
    COMMON_PUBLIC = 'common_public'


class VBucksPlatform(Enum):
    PC = 'EpicPC'
    ANDROID = 'EpicAndroid'
    PLAYSTATION = 'PSN'
    XBOX = 'Live'
    IOS = 'IOSAppStore'
    NINTENDO = 'Nintendo'
    SAMSUNG = 'Samsung'
    EPIC = 'Epic'
    WE_GAME = 'WeGame'
    PC_KOREA = 'EpicPCKorea'
    GOOGLE_PLAY = 'GooglePlay'
    SHARED = 'Shared'


class CosmeticType(Enum):
    OUTFIT = 'AthenaCharacter'
    BACKPACK = 'AthenaBackpack'
    PICKAXE = 'AthenaPickaxe'
    GLIDER = 'AthenaGlider'
    CONTRAIL = 'AthenaSkyDiveContrail'
    DANCE = 'AthenaDance'
    WRAP = 'AthenaItemWrap'
    MUSIC = 'AthenaMusicPack'
    LOADING_SCREEN = 'AthenaLoadingScreen'


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


class DiscoverySearchOrderType(Enum):
    PLAYER_COUNT = 'globalCCU'


class _RatingAuthorityRating(Enum):
    @staticmethod
    def get_authority():
        raise NotImplementedError


class ACBRating(_RatingAuthorityRating):
    AGE_M = 'ACB_AGE_M'
    AGE_G = 'ACB_AGE_G'
    AGE_NA = 'ACB_AGE_NA'

    @staticmethod
    def get_authority():
        return 'ACB'


class PEGIRating(_RatingAuthorityRating):
    AGE_12 = 'PEGI_AGE_12'
    AGE_PG = 'PEGI_AGE_PG'

    @staticmethod
    def get_authority():
        return 'PEGI'


class GenericRating(_RatingAuthorityRating):
    AGE_12 = 'GEN_AGE_12'

    @staticmethod
    def get_authority():
        return 'Generic'


class ClassIndRating(_RatingAuthorityRating):
    AGE_12 = 'CLASSIND_AGE_12'
    AGE_10 = 'CLASSIND_AGE_10'
    AGE_LIVRE = 'CLASSIND_AGE_LIVRE'

    @staticmethod
    def get_authority():
        return 'ClassInd'


class USKRating(_RatingAuthorityRating):
    AGE_12 = 'USK_AGE_12'
    AGE_6 = 'USK_AGE_6'

    @staticmethod
    def get_authority():
        return 'USK'


class GRACRating(_RatingAuthorityRating):
    AGE_12 = 'GRAC_AGE_12'
    AGE_RC = 'GRAC_AGE_RC'
    AGE_NA = 'GRAC_AGE_NA'

    @staticmethod
    def get_authority():
        return 'GRAC'


class ESRBRating(_RatingAuthorityRating):
    AGE_T = 'ESRB_AGE_T'
    AGE_E10 = 'ESRB_AGE_E10'

    @staticmethod
    def get_authority():
        return 'ESRB'


class RussiaRating(_RatingAuthorityRating):
    AGE_12 = 'RUSSIA_AGE_12'

    @staticmethod
    def get_authority():
        return 'Russia'

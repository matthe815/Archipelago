from typing import Dict, NamedTuple, Optional, Tuple

from ..enums import ZorkGrandInquisitorItems, ZorkGrandInquisitorLocations


class ZorkGrandInquisitorMissableLocationGrantConditionsData(NamedTuple):
    location_condition: ZorkGrandInquisitorLocations
    item_conditions: Optional[Tuple[ZorkGrandInquisitorItems, ...]]


missable_location_grant_conditions_data: Dict[
    ZorkGrandInquisitorLocations, ZorkGrandInquisitorMissableLocationGrantConditionsData
] = {
    ZorkGrandInquisitorLocations.BOING_BOING_BOING:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.FLYING_SNAPDRAGON,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.BONK:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.PROZORKED,
            item_conditions=(ZorkGrandInquisitorItems.HAMMER,),
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_ARRESTED_WITH_JACK:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.ARREST_THE_VANDAL,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_ATTACKED_THE_QUELBEES:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.OUTSMART_THE_QUELBEES,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_EATEN_BY_A_GRUE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.MAGIC_FOREVER,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_LOST_GAME_OF_STRIP_GRUE_FIRE_WATER:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.STRIP_GRUE_FIRE_WATER,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_LOST_SOUL_TO_OLD_SCRATCH:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.OLD_SCRATCH_WINNER,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_OUTSMARTED_BY_THE_QUELBEES:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.OUTSMART_THE_QUELBEES,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_SLICED_UP_BY_THE_INVISIBLE_GUARD:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.YOU_GAINED_86_EXPERIENCE_POINTS,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_STEPPED_INTO_THE_INFINITE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.A_SMALLWAY,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_SWALLOWED_BY_A_DRAGON:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.THAR_SHE_BLOWS,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_YOURE_NOT_CHARON:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.OPEN_THE_GATES_OF_HELL,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_ZORK_ROCKS_EXPLODED:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.CRISIS_AVERTED,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DENIED_BY_THE_LAKE_MONSTER:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.WOW_IVE_NEVER_GONE_INSIDE_HIM_BEFORE,
            item_conditions=(ZorkGrandInquisitorItems.SPELL_GOLGATEM,),
        )
    ,
    ZorkGrandInquisitorLocations.EMERGENCY_MAGICATRONIC_MESSAGE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.ARTIFACTS_EXPLAINED,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.FAT_LOT_OF_GOOD_THATLL_DO_YA:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.YOU_GAINED_86_EXPERIENCE_POINTS,
            item_conditions=(ZorkGrandInquisitorItems.SPELL_IGRAM,),
        )
    ,
    ZorkGrandInquisitorLocations.I_DONT_THINK_YOU_WOULDVE_WANTED_THAT_TO_WORK_ANYWAY:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.PROZORKED,
            item_conditions=(ZorkGrandInquisitorItems.SPELL_THROCK,),
        )
    ,
    ZorkGrandInquisitorLocations.I_SPIT_ON_YOUR_FILTHY_COINAGE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.YOU_GAINED_86_EXPERIENCE_POINTS,
            item_conditions=(ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,),
        )
    ,
    ZorkGrandInquisitorLocations.MEAD_LIGHT:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.FIRE_FIRE,
            item_conditions=(ZorkGrandInquisitorItems.MEAD_LIGHT,),
        )
    ,
    ZorkGrandInquisitorLocations.MUSHROOM_HAMMERED:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.THROCKED_MUSHROOM_HAMMERED,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.NO_AUTOGRAPHS:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.FIRE_FIRE,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.NO_BONDAGE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.HELP_ME_CANT_BREATHE,
            item_conditions=(ZorkGrandInquisitorItems.ROPE,),
        )
    ,
    ZorkGrandInquisitorLocations.TALK_TO_ME_GRAND_INQUISITOR:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.FIRE_FIRE,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.THATS_A_ROPE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.FIRE_FIRE,
            item_conditions=(ZorkGrandInquisitorItems.ROPE,),
        )
    ,
    ZorkGrandInquisitorLocations.THATS_IT_JUST_KEEP_HITTING_THOSE_BUTTONS:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.ENJOY_YOUR_TRIP,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.THATS_STILL_A_ROPE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.YOU_GAINED_86_EXPERIENCE_POINTS,
            item_conditions=(ZorkGrandInquisitorItems.SPELL_GLORF,),
        )
    ,
    ZorkGrandInquisitorLocations.WHAT_ARE_YOU_STUPID:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.FIRE_FIRE,
            item_conditions=(ZorkGrandInquisitorItems.PLASTIC_SIX_PACK_HOLDER,),
        )
    ,
    ZorkGrandInquisitorLocations.YAD_GOHDNUORGREDNU_3_YRAUBORF:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.REASSEMBLE_SNAVIG,
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.YOUR_PUNY_WEAPONS_DONT_PHASE_ME_BABY:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.WANT_SOME_RYE_COURSE_YA_DO,
            item_conditions=(ZorkGrandInquisitorItems.SWORD, ZorkGrandInquisitorItems.HOTSPOT_HARRY),
        )
    ,
    ZorkGrandInquisitorLocations.YOU_DONT_GO_MESSING_WITH_A_MANS_ZIPPER:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.YOU_GAINED_86_EXPERIENCE_POINTS,
            item_conditions=(ZorkGrandInquisitorItems.SPELL_REZROV,),
        )
    ,
    ZorkGrandInquisitorLocations.YOU_WANT_A_PIECE_OF_ME_DOCK_BOY:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            location_condition=ZorkGrandInquisitorLocations.HELP_ME_CANT_BREATHE,
            item_conditions=None,
        )
    ,
}

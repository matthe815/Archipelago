from typing import List, TypedDict


class LocationDict(TypedDict):
    name: str
    game_id: str
    room: str


location_table: List[LocationDict] = [
    # Albero
    {'name': "Albero: Tirso's house, top floor",
        'game_id': "RB01",
        'room': "D01Z02S02"},
    {'name': "Albero: Outside Ossuary",
        'game_id': "CO43",
        'room': "D01Z02S04"},
    {'name': "Albero: Graveyard",
        'game_id': "CO16",
        'room': "D01Z02S05"},
    {'name': "Albero: Gate of Travel room",
        'game_id': "QI65",
        'room': "D01Z02S07"},
    {'name': "Albero: Child of Moonlight",
        'game_id': "RESCUED_CHERUB_08",
        'room': "D01Z02S03"},
    {'name': "Albero: Bless Linen Cloth",
        'game_id': "RE04",
        'room': "D01Z02S01"},
    {'name': "Albero: Bless Hatched Egg",
        'game_id': "RE10",
        'room': "D01Z02S01"},
    {'name': "Albero: Bless Severed Hand",
        'game_id': "RE02",
        'room': "D01Z02S01"},
    {'name': "Albero: First gift for Cleofas",
        'game_id': "QI01",
        'room': "D01Z02S03"},
    {'name': "Albero: Final gift for Cleofas",
        'game_id': "PR11",
        'room': "D01BZ04S01"},
    {'name': "Albero: Tirso's 1st reward",
        'game_id': "QI66",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso's 2nd reward",
        'game_id': "Tirso[500]",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso's 3rd reward",
        'game_id': "Tirso[1000]",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso's 4th reward",
        'game_id': "Tirso[2000]",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso's 5th reward",
        'game_id': "Tirso[5000]",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso's 6th reward",
        'game_id': "Tirso[10000]",
        'room': "D01Z02S02"},
    {'name': "Albero: Tirso's final reward",
        'game_id': "QI56",
        'room': "D01Z02S02"},
    {'name': "Albero: Lvdovico's 1st reward",
        'game_id': "Lvdovico[500]",
        'room': "D01Z02S03"},
    {'name': "Albero: Lvdovico's 2nd reward",
        'game_id': "Lvdovico[1000]",
        'room': "D01Z02S03"},
    {'name': "Albero: Lvdovico's 3rd reward",
        'game_id': "PR03",
        'room': "D01Z02S03"},
    {'name': "Ossuary: Isidora, Voice of the Dead",
        'game_id': "QI201",
        'room': "D01BZ08S01"},
    {'name': "Albero: Mea Culpa altar",
        'game_id': "Sword[D01Z02S06]",
        'room': "D01Z02S06"},
    {'name': "Albero: Donate 5000 Tears",
        'game_id': "RB104",
        'room': "D01BZ04S01"},
    {'name': "Albero: Donate 50000 Tears",
        'game_id': "RB105",
        'room': "D01BZ04S01"},
    {'name': "Ossuary: 1st reward",
        'game_id': "Undertaker[250]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: 2nd reward",
        'game_id': "Undertaker[500]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: 3rd reward",
        'game_id': "Undertaker[750]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: 4th reward",
        'game_id': "Undertaker[1000]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: 5th reward",
        'game_id': "Undertaker[1250]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: 6th reward",
        'game_id': "Undertaker[1500]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: 7th reward",
        'game_id': "Undertaker[1750]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: 8th reward",
        'game_id': "Undertaker[2000]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: 9th reward",
        'game_id': "Undertaker[2500]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: 10th reward",
        'game_id': "Undertaker[3000]",
        'room': "D01BZ06S01"},
    {'name': "Ossuary: 11th reward",
        'game_id': "Undertaker[5000]",
        'room': "D01BZ06S01"},
    
    # All the Tears of the Sea
    {'name': "AtTotS: Miriam's gift",
        'game_id': "PR201",
        'room': "D04Z04S01"},

    # Archcathedral Rooftops
    {'name': "AR: First soldier fight",
        'game_id': "QI02",
        'room': "D06Z01S03"},
    {'name': "AR: Second soldier fight",
        'game_id': "QI03",
        'room': "D06Z01S06"},
    {'name': "AR: Third soldier fight",
        'game_id': "QI04",
        'room': "D06Z01S21"},
    {'name': "AR: Upper west shaft ledge",
        'game_id': "CO06",
        'room': "D06Z01S12"},
    {'name': "AR: Upper west shaft Child of Moonlight",
        'game_id': "RESCUED_CHERUB_36",
        'room': "D06Z01S12"},
    {'name': "AR: Upper west shaft chest",
        'game_id': "PR12",
        'room': "D06Z01S12"},
    {'name': "AR: Statue near MoM",
        'game_id': "HE04",
        'room': "D06Z01S22"},
    {'name': "AR: Lady of the Six Sorrows",
        'game_id': "Lady[D06Z01S24]",
        'room': "D06Z01S24"},
    {'name': "AR: Upper east shaft ledge",
        'game_id': "CO40",
        'room': "D06Z01S15"},
    {'name': "AR: Mea Culpa altar",
        'game_id': "Sword[D06Z01S11]",
        'room': "D06Z01S11"},
    {'name': "AR: Crisanta of the Wrapped Agony",
        'game_id': "BS16",
        'room': "D06Z01S25"},

    # Bridge of the Three Cavalries
    {'name': "BotTC: Esdras, of the Anointed Legion",
        'game_id': "BS12",
        'room': "D08Z01S01"},
    {'name': "BotTC: Esdras' gift",
        'game_id': "PR09",
        'room': "D08Z01S01"},
    {'name': "BotTC: Inside giant statue",
        'game_id': "HE101",
        'room': "D08Z01S02"},

    # Brotherhood of the Silent Sorrow
    {'name': "BotSS: Starting room Child of Moonlight",
        'game_id': "RESCUED_CHERUB_06",
        'room': "D17Z01S01"},
    {'name': "BotSS: Starting room ledge",
        'game_id': "RB204",
        'room': "D17Z01S01"},
    {'name': "BotSS: Chamber of the Eldest Brother",
        'game_id': "RE01",
        'room': "D17BZ01S01"},
    {'name': "BotSS: Mea Culpa altar",
        'game_id': "Sword[D17Z01S08]",
        'room': "D17Z01S08"},
    {'name': "BotSS: Platforming gauntlet",
        'game_id': "CO25",
        'room': "D17BZ02S01"},
    {'name': "BotSS: Outside church",
        'game_id': "PR203",
        'room': "D17Z01S14"},
    {'name': "BotSS: Esdras' final gift",
        'game_id': "QI204",
        'room': "D17Z01S15"},
    {'name': "BotSS: Crisanta's gift",
        'game_id': "QI301",
        'room': "D17Z01S15"},
    {'name': "BotSS: Warden of the Silent Sorrow",
        'game_id': "BS13",
        'room': "D17Z01S11"},
    
    # Convent of Our Lady of the Charred Visage
    {'name': "CoOLotCV: Snowy window ledge",
        'game_id': "CO05",
        'room': "D02Z03S03"},
    {'name': "CoOLotCV: Center enemy lineup",
        'game_id': "CO15",
        'room': "D02Z03S07"},
    {'name': "CoOLotCV: Center miasma room",
        'game_id': "RB08",
        'room': "D02Z03S05"},
    {'name': "CoOLotCV: Lower west statue",
        'game_id': "HE03",
        'room': "D02Z03S12"},
    {'name': "CoOLotCV: Lady of the Six Sorrows",
        'game_id': "Lady[D02Z03S15]",
        'room': "D02Z03S15"},
    {'name': "CoOLotCV: Mea Culpa altar",
        'game_id': "Sword[D02Z03S13]",
        'room': "D02Z03S13"},
    {'name': "CoOLotCV: First blue candle",
        'game_id': "RB24",
        'room': "D02Z03S17"},
    {'name': "CoOLotCV: Outside pathway",
        'game_id': "RB107",
        'room': "D02Z03S23"},
    {'name': "CoOLotCV: Fountain of burning oil",
        'game_id': "QI57",
        'room': "D02Z03S21"},
    {'name': "CoOLotCV: Our Lady of the Charred Visage",
        'game_id': "BS03",
        'room': "D02Z03S20"},
    {'name': "CoOLotCV: Visage of Compunction",
        'game_id': "QI40",
        'room': "D02Z03S21"},
    {'name': "CoOLotCV: Mask room",
        'game_id': "QI61",
        'room': "D02Z03S19"},

    # Deambulatory of His Holiness
    {'name': "DoHH: Viridiana's gift",
        'game_id': "PR08",
        'room': "D07Z01S01"},

    # Desecrated Cistern
    {'name': "DC: Lady of the Six Sorrows, from MD",
        'game_id': "Lady[D01Z05S22]",
        'room': "D01Z05S22"},
    {'name': "DC: Behind sewage drips",
        'game_id': "CO41",
        'room': "D01Z05S15"},
    {'name': "DC: Child of Moonlight, above water",
        'game_id': "RESCUED_CHERUB_11",
        'room': "D01Z05S14"},
    {'name': "DC: Lower east tunnel chest",
        'game_id': "QI45",
        'room': "D01Z05S11"},
    {'name': "DC: Upper east tunnel chest",
        'game_id': "PR16",
        'room': "D01Z05S06"},
    {'name': "DC: Upper east Child of Moonlight",
        'game_id': "RESCUED_CHERUB_13",
        'room': "D01Z05S06"},
    {'name': "DC: Hidden alcove near fountain",
        'game_id': "QI67",
        'room': "D01Z05S05"},
    {'name': "DC: Shortcut to WotBC",
        'game_id': "CO09",
        'room': "D01Z05S05"},
    {'name': "DC: Oil of the Pilgrims",
        'game_id': "Oil[D01Z05S07]",
        'room': "D01Z05S07"},
    {'name': "DC: Child of Moonlight, miasma room",
        'game_id': "RESCUED_CHERUB_14",
        'room': "D01Z05S08"},
    {'name': "DC: Behind gate in miasma room",
        'game_id': "QI12",
        'room': "D01Z05S08"},
    {'name': "DC: Child of Moonlight, behind pillar",
        'game_id': "RESCUED_CHERUB_12",
        'room': "D01Z05S13"},
    {'name': "DC: High ledge near elevator shaft",
        'game_id': "CO32",
        'room': "D01Z05S17"},
    {'name': "DC: Shroud puzzle",
        'game_id': "RB03",
        'room': "D01BZ05S01"},
    {'name': "DC: Chalice room",
        'game_id': "QI75",
        'room': "D01Z05S23"},
    {'name': "DC: Mea Culpa altar",
        'game_id': "Sword[D01Z05S24]",
        'room': "D01Z05S24"},
    {'name': "DC: Lady of the Six Sorrows, elevator shaft",
        'game_id': "Lady[D01Z05S26]",
        'room': "D01Z05S26"},
    {'name': "DC: Top of elevator Child of Moonlight",
        'game_id': "RESCUED_CHERUB_15",
        'room': "D01Z05S20"},
    {'name': "DC: Elevator shaft Child of Moonlight",
        'game_id': "RESCUED_CHERUB_22",
        'room': "D01Z05S25"},
    {'name': "DC: Elevator shaft ledge",
        'game_id': "CO44",
        'room': "D01Z05S25"},

    # Echoes of Salt
    {'name': "EoS: Lantern jump near MotED",
        'game_id': "RB108",
        'room': "D20Z01S02"},
    {'name': "EoS: Lantern jump near elevator",
        'game_id': "RB202",
        'room': "D20Z01S09"},
    
    # Graveyard of the Peaks
    {'name': "GotP: Shop cave Child of Moonlight",
        'game_id': "RESCUED_CHERUB_31",
        'room': "D02Z02S08"},
    {'name': "GotP: Shop cave hidden hole",
        'game_id': "CO42",
        'room': "D02Z02S08"},
    {'name': "GotP: Shop item 1",
        'game_id': "QI11",
        'room': "D02BZ02S01"},
    {'name': "GotP: Shop item 2",
        'game_id': "RB37",
        'room': "D02BZ02S01"},
    {'name': "GotP: Shop item 3",
        'game_id': "RB02",
        'room': "D02BZ02S01"},
    {'name': "GotP: Confessor Dungeon room",
        'game_id': "RB38",
        'room': "D02Z02S06"},
    {'name': "GotP: Elevator shaft Child of Moonlight",
        'game_id': "RESCUED_CHERUB_26",
        'room': "D02Z02S11"},
    {'name': "GotP: Elevator shaft ledge",
        'game_id': "QI53",
        'room': "D02Z02S11"},
    {'name': "GotP: Lady of the Six Sorrows",
        'game_id': "Lady[D02Z02S12]",
        'room': "D02Z02S12"},
    {'name': "GotP: Self sacrifice statue",
        'game_id': "HE11",
        'room': "D02Z02S13"},
    {'name': "GotP: Lower east shaft",
        'game_id': "QI46",
        'room': "D02Z02S03"},
    {'name': "GotP: Center east shaft",
        'game_id': "CO29",
        'room': "D02Z02S03"},
    {'name': "GotP: Upper east shaft",
        'game_id': "QI08",
        'room': "D02Z02S03"},
    {'name': "GotP: East cliffside",
        'game_id': "RB106",
        'room': "D02Z02S14"},
    {'name': "GotP: West shaft Child of Moonlight",
        'game_id': "RESCUED_CHERUB_25",
        'room': "D02Z02S04"},
    {'name': "GotP: Lower west shaft",
        'game_id': "RB32",
        'room': "D02Z02S04"},
    {'name': "GotP: Upper west shaft",
        'game_id': "CO01",
        'room': "D02Z02S04"},
    {'name': "GotP: Center shaft Child of Moonlight",
        'game_id': "RESCUED_CHERUB_24",
        'room': "D02Z02S02"},
    {'name': "GotP: Center shaft ledge",
        'game_id': "RB15",
        'room': "D02Z02S05"},
    {'name': "GotP: Oil of the Pilgrims",
        'game_id': "Oil[D02Z02S10]",
        'room': "D02Z02S10"},
    {'name': "GotP: Amanecida of the Bejeweled Arrow",
        'game_id': "Amanecida[D02Z02S14]",
        'room': "D02Z02S14"},
    
    # Grievance Ascends
    {'name': "GA: Lower west ledge",
        'game_id': "QI44",
        'room': "D03Z03S02"},
    {'name': "GA: Miasma room treasure",
        'game_id': "RE07",
        'room': "D03Z03S06"},
    {'name': "GA: Miasma room Child of Moonlight",
        'game_id': "RESCUED_CHERUB_19",
        'room': "D03Z03S06"},
    {'name': "GA: Miasma room floor",
        'game_id': "CO12",
        'room': "D03Z03S06"},
    {'name': "GA: Oil of the Pilgrims",
        'game_id': "Oil[D03Z03S13]",
        'room': "D03Z03S13"},
    {'name': "GA: End of blood bridge",
        'game_id': "QI10",
        'room': "D03Z03S08"},
    {'name': "GA: Blood bridge Child of Moonlight",
        'game_id': "RESCUED_CHERUB_21",
        'room': "D03Z03S08"},
    {'name': "GA: Lower east Child of Moonlight",
        'game_id': "RESCUED_CHERUB_20",
        'room': "D03Z03S09"},
    {'name': "GA: Altasgracias' gift",
        'game_id': "QI13",
        'room': "D03Z03S10"},
    {'name': "GA: Empty giant egg",
        'game_id': "RB06",
        'room': "D03Z03S10"},
    {'name': "GA: Tres Angustias",
        'game_id': "BS04",
        'room': "D03Z03S15"},
    {'name': "GA: Visage of Contrition",
        'game_id': "QI39",
        'room': "D03Z03S16"},
    
    # Hall of the Dawning
    {'name': "HotD: Mirror room",
        'game_id': "QI105",
        'room': "D08Z03S01"},
    {'name': "HotD: Laudes, the First of the Amanecidas",
        'game_id': "LaudesBossTrigger[30000]",
        'room': "D08Z03S03"},
    
    # Jondo
    {'name': "Jondo: Upper east ledge",
        'game_id': "CO08",
        'room': "D03Z02S01"},
    {'name': "Jondo: Upper east chest",
        'game_id': "PR10",
        'room': "D03Z02S01"},
    {'name': "Jondo: Lower east under chargers",
        'game_id': "CO33",
        'room': "D03Z02S04"},
    {'name': "Jondo: Lower east bell trap",
        'game_id': "QI19",
        'room': "D03Z02S06"},
    {'name': "Jondo: Upper east Child of Moonlight",
        'game_id': "RESCUED_CHERUB_18",
        'room': "D03Z02S05"},
    {'name': "Jondo: Spike tunnel Child of Moonlight",
        'game_id': "RESCUED_CHERUB_37",
        'room': "D03Z02S11"},
    {'name': "Jondo: Spike tunnel statue",
        'game_id': "HE06",
        'room': "D03Z02S11"},
    {'name': "Jondo: Spike tunnel cave",
        'game_id': "QI103",
        'room': "D03Z02S15"},
    {'name': "Jondo: Lower west lift alcove",
        'game_id': "CO07",
        'room': "D03Z02S07"},
    {'name': "Jondo: Lower west bell alcove",
        'game_id': "QI41",
        'room': "D03Z02S08"},
    {'name': "Jondo: Upper west bell puzzle",
        'game_id': "QI52",
        'room': "D03Z02S12"},
    {'name': "Jondo: Upper west tree root",
        'game_id': "RB28",
        'room': "D03Z02S13"},
    {'name': "Jondo: Upper west Child of Moonlight",
        'game_id': "RESCUED_CHERUB_17",
        'room': "D03Z02S10"},
    
    # Knot of the Three Words
    {'name': "KotTW: Gift from the Traitor",
        'game_id': "HE201",
        'room': "D04Z03S02"},
    
    # Library of the Negated Words
    {'name': "LotNW: Platform room Child of Moonlight",
        'game_id': "RESCUED_CHERUB_01",
        'room': "D05Z01S04"},
    {'name': "LotNW: Platform room ledge",
        'game_id': "CO18",
        'room': "D05Z01S04"},
    {'name': "LotNW: Root ceiling platform",
        'game_id': "CO22",
        'room': "D05Z01S05"},
    {'name': "LotNW: Hidden floor",
        'game_id': "QI50",
        'room': "D05Z01S05"},
    {'name': "LotNW: Miasma hallway chest",
        'game_id': "RB31",
        'room': "D05Z01S06"},
    {'name': "LotNW: Lady of the Six Sorrows",
        'game_id': "Lady[D05Z01S14]",
        'room': "D05Z01S14"},
    {'name': "LotNW: Bone puzzle",
        'game_id': "PR15",
        'room': "D05Z01S18"},
    {'name': "LotNW: Lowest west upper ledge",
        'game_id': "CO28",
        'room': "D05Z01S11"},
    {'name': "LotNW: Platform puzzle chest",
        'game_id': "PR07",
        'room': "D05Z01S10"},
    {'name': "LotNW: Lowest west center ledge",
        'game_id': "RB30",
        'room': "D05Z01S11"},
    {'name': "LotNW: Lowest west Child of Moonlight",
        'game_id': "RESCUED_CHERUB_02",
        'room': "D05Z01S11"},
    {'name': "LotNW: Oil of the Pilgrims",
        'game_id': "Oil[D05Z01S19]",
        'room': "D05Z01S19"},
    {'name': "LotNW: Elevator Child of Moonlight",
        'game_id': "RESCUED_CHERUB_32",
        'room': "D05Z01S21"},
    {'name': "LotNW: Mask room",
        'game_id': "QI62",
        'room': "D05Z01S15"},
    {'name': "LotNW: Mea Culpa altar",
        'game_id': "Sword[D05Z01S13]",
        'room': "D05Z01S13"},
    {'name': "LotNW: Silence for Diosdado",
        'game_id': "RB203",
        'room': "D05Z01S11"},
    {'name': "LotNW: Twisted wood hidden wall",
        'game_id': "RB301",
        'room': "D05BZ01S01"},

    # Mercy Dreams
    {'name': "MD: First area hidden wall",
        'game_id': "CO30",
        'room': "D01Z04S05"},
    {'name': "MD: Second area trapped chest",
        'game_id': "PR01",
        'room': "D01Z04S07"},
    {'name': "MD: Second area ledge",
        'game_id': "CO03",
        'room': "D01Z04S06"},
    {'name': "MD: Second area Child of Moonlight",
        'game_id': "RESCUED_CHERUB_09",
        'room': "D01Z04S06"},
    {'name': "MD: First red candle",
        'game_id': "RB17",
        'room': "D01Z04S08"},
    {'name': "MD: Shop item 1",
        'game_id': "QI58",
        'room': "D01BZ02S01"},
    {'name': "MD: Shop item 2",
        'game_id': "RB05",
        'room': "D01BZ02S01"},
    {'name': "MD: Shop item 3",
        'game_id': "RB09",
        'room': "D01BZ02S01"},
    {'name': "MD: Third area hidden room",
        'game_id': "QI48",
        'room': "D01Z04S11"},
    {'name': "MD: Sliding challenge",
        'game_id': "CO38",
        'room': "D01Z04S14"},
    {'name': "MD: Ten Piedad",
        'game_id': "BS01",
        'room': "D01Z04S18"},
    {'name': "MD: Visage of Attrition",
        'game_id': "QI38",
        'room': "D01Z04S19"},
    {'name': "MD: Cave Child of Moonlight",
        'game_id': "RESCUED_CHERUB_33",
        'room': "D01Z04S16"}, 
    {'name': "MD: Behind gate to TSC",
        'game_id': "CO21",
        'room': "D01Z04S13"},

    # Mother of Mothers
    {'name': "MoM: Oil of the Pilgrims",
        'game_id': "Oil[D04Z02S14]",
        'room': "D04Z02S14"},
    {'name': "MoM: Upper east ledge",
        'game_id': "RB33",
        'room': "D04Z02S07"},
    {'name': "MoM: East chandelier platform",
        'game_id': "CO35",
        'room': "D04Z02S07"},
    {'name': "MoM: Lower west Child of Moonlight",
        'game_id': "RESCUED_CHERUB_30",
        'room': "D04Z02S01"},
    {'name': "MoM: Upper west floor",
        'game_id': "CO17",
        'room': "D04Z02S02"},
    {'name': "MoM: Redento's treasure",
        'game_id': "RE03",
        'room': "D04BZ02S01"},
    {'name': "MoM: Final meeting with Redento",
        'game_id': "QI54",
        'room': "D04BZ02S01"},
    {'name': "MoM: Giant chandelier statue",
        'game_id': "HE01",
        'room': "D04Z02S16"},
    {'name': "MoM: Outside Cleofas' room",
        'game_id': "CO34",
        'room': "D04Z02S06"},
    {'name': "MoM: Upper center floor",
        'game_id': "CO20",
        'room': "D04Z02S11"},
    {'name': "MoM: Upper center Child of Moonlight",
        'game_id': "RESCUED_CHERUB_29",
        'room': "D04Z02S11"},
    {'name': "MoM: Mea Culpa altar",
        'game_id': "Sword[D04Z02S12]",
        'room': "D04Z02S12"},
    {'name': "MoM: Melquiades, The Exhumed Archbishop",
        'game_id': "BS05",
        'room': "D04Z02S22"},
    {'name': "MoM: Mask room",
        'game_id': "QI60",
        'room': "D04Z02S15"},

    # Mountains of the Endless Dusk
    {'name': "MotED: Under entrance to DC",
        'game_id': "CO13",
        'room': "D03Z01S01"},
    {'name': "MotED: Perpetva",
        'game_id': "RB13",
        'room': "D03Z01S06"},
    {'name': "MotED: Child of Moonlight, above chasm",
        'game_id': "RESCUED_CHERUB_16",
        'room': "D03Z01S03"},
    {'name': "MotED: Platform above chasm",
        'game_id': "QI47",
        'room': "D03Z01S03"},
    {'name': "MotED: 1st meeting with Redento",
        'game_id': "RB22",
        'room': "D03Z01S03"},
    {'name': "MotED: Blood platform alcove",
        'game_id': "QI63",
        'room': "D03Z01S04"},
    {'name': "MotED: Egg hatching",
        'game_id': "QI14",
        'room': "D03Z01S06"},
    {'name': "MotED: Amanecida of the Golden Blades",
        'game_id': "Amanecida[D03Z01S03]",
        'room': "D03Z01S03"},

    # Mourning and Havoc
    {'name': "MaH: West chest",
        'game_id': "PR202",
        'room': "D20Z02S11"},
    {'name': "MaH: Upper east chest",
        'game_id': "RB201",
        'room': "D20Z02S02"},
    {'name': "MaH: Sierpes' eye",
        'game_id': "QI202",
        'room': "D20Z02S08"},
    {'name': "MaH: Sierpes",
        'game_id': "BossTrigger[5000]",
        'room': "D20Z02S08"},
    
    # Patio of the Silent Steps
    {'name': "PotSS: First area Child of Moonlight",
        'game_id': "RESCUED_CHERUB_35",
        'room': "D04Z01S01"},
    {'name': "PotSS: First area ledge",
        'game_id': "CO23",
        'room': "D04Z01S01"},
    {'name': "PotSS: Second area ledge",
        'game_id': "RB14",
        'room': "D04Z01S02"},
    {'name': "PotSS: Third area Child of Moonlight",
        'game_id': "RESCUED_CHERUB_28",
        'room': "D04Z01S03"},
    {'name': "PotSS: Third area lower ledge",
        'game_id': "QI37",
        'room': "D04Z01S03"},
    {'name': "PotSS: Third area upper ledge",
        'game_id': "CO39",
        'room': "D04Z01S03"},
    {'name': "PotSS: Climb to WotHP",
        'game_id': "QI102",
        'room': "D04Z01S06"},
    {'name': "PotSS: 4th meeting with Redento",
        'game_id': "RB21",
        'room': "D04Z01S04"},
    {'name': "PotSS: Amanecida of the Chiselled Steel",
        'game_id': "Amanecida[D04Z01S04]",
        'room': "D04Z01S04"},

    # Petrous
    {'name': "Petrous: Temple entrance",
        'game_id': "QI101",
        'room': "D01Z06S01"},

    # The Resting Place of the Sister
    {'name': "TRPotS: Perpetva's shrine",
        'game_id': "QI203",
        'room': "D20Z03S01"},
    
    # The Sleeping Canvases
    {'name': "TSC: Painting ladder ledge",
        'game_id': "QI64",
        'room': "D05Z02S02"},
    {'name': "TSC: Candle wax puzzle",
        'game_id': "HE07",
        'room': "D05Z02S08"},
    {'name': "TSC: Shop item 1",
        'game_id': "RB12",
        'room': "D05BZ02S01"},
    {'name': "TSC: Shop item 2",
        'game_id': "QI49",
        'room': "D05BZ02S01"},
    {'name': "TSC: Shop item 3",
        'game_id': "QI71",
        'room': "D05BZ02S01"},
    {'name': "TSC: Swinging blade tunnel",
        'game_id': "QI104",
        'room': "D05Z02S15"},
    {'name': "TSC: Exposito, Scion of Abjuration",
        'game_id': "BS06",
        'room': "D05Z02S14"},
    {'name': "TSC: Under elevator shaft",
        'game_id': "CO31",
        'room': "D05Z02S11"},
    {'name': "TSC: Jocinero's 1st reward",
        'game_id': "RE05",
        'room': "D05Z02S10"},
    {'name': "TSC: Jocinero's final reward",
        'game_id': "PR05",
        'room': "D05Z02S10"},

    # The Holy Line
    {'name': "THL: Deogracias' gift",
        'game_id': "QI31",
        'room': "D01Z01S07"},
    {'name': "THL: Hanging skeleton",
        'game_id': "PR14",
        'room': "D01Z01S02"},
    {'name': "THL: Across blood platforms",
        'game_id': "RB07",
        'room': "D01Z01S02"},
    {'name': "THL: Child of Moonlight",
        'game_id': "RESCUED_CHERUB_07",
        'room': "D01Z01S03"},
    {'name': "THL: Underground ledge",
        'game_id': "CO04",
        'room': "D01Z01S03"},
    {'name': "THL: Underground chest",
        'game_id': "QI55",
        'room': "D01Z01S03"},

    # Wall of the Holy Prohibitions
    {'name': "WotHP: Upper east room, lift puzzle",
        'game_id': "RB11",
        'room': "D09Z01S02"},
    {'name': "WotHP: Upper east room, center cell ledge",
        'game_id': "CO10",
        'room': "D09BZ01S01"},
    {'name': "WotHP: Upper east room, center cell floor",
        'game_id': "QI69",
        'room': "D09BZ01S01"},
    {'name': "WotHP: Upper east room, top bronze cell",
        'game_id': "RESCUED_CHERUB_03",
        'room': "D09BZ01S01"},
    {'name': "WotHP: Upper east room, top silver cell",
        'game_id': "CO24",
        'room': "D09BZ01S01"},
    {'name': "WotHP: Upper east room, center gold cell",
        'game_id': "QI51",
        'room': "D09Z01S02"},
    {'name': "WotHP: Upper west room, center gold cell",
        'game_id': "CO26",
        'room': "D09BZ01S01"},
    {'name': "WotHP: Lower west room, bottom gold cell",
        'game_id': "CO02",
        'room': "D09BZ01S01"},
    {'name': "WotHP: Upper west room, top silver cell",
        'game_id': "RESCUED_CHERUB_34",
        'room': "D09BZ01S01"},
    {'name': "WotHP: Lower west room, top ledge",
        'game_id': "RB16",
        'room': "D09Z01S09"},
    {'name': "WotHP: Lower east room, hidden ledge",
        'game_id': "CO27",
        'room': "D09Z01S10"},
    {'name': "WotHP: Lower east room, bottom silver cell",
        'game_id': "RESCUED_CHERUB_04",
        'room': "D09BZ01S01"},
    {'name': "WotHP: Lower east room, top bronze cell",
        'game_id': "QI70",
        'room': "D09Z01S10"},
    {'name': "WotHP: Lower east room, top silver cell",
        'game_id': "CO37",
        'room': "D09BZ01S01"},
    {'name': "WotHP: Outside Child of Moonlight",
        'game_id': "RESCUED_CHERUB_05",
        'room': "D09Z01S06"},
    {'name': "WotHP: Oil of the Pilgrims",
        'game_id': "Oil[D09Z01S12]",
        'room': "D09Z01S12"},
    {'name': "WotHP: Quirce, Returned By The Flames",
        'game_id': "BS14",
        'room': "D09Z01S03"},
    {'name': "WotHP: Collapsing floor ledge",
        'game_id': "QI72",
        'room': "D09Z01S08"},
    {'name': "WotHP: Amanecida of the Molten Thorn",
        'game_id': "Amanecida[D09Z01S01]",
        'room': "D09Z01S01"},

    # Wasteland of the Buried Churches
    {'name': "WotBC: Lower log path",
        'game_id': "RB04",
        'room': "D01Z03S01"},
    {'name': "WotBC: Hidden alcove",
        'game_id': "CO14",
        'room': "D01Z03S02"},
    {'name': "WotBC: Outside ledge",
        'game_id': "CO36",
        'room': "D01Z03S03"},
    {'name': "WotBC: Outside Child of Moonlight",
        'game_id': "RESCUED_CHERUB_10",
        'room': "D01Z03S03"},
    {'name': "WotBC: Under broken bridge",
        'game_id': "QI06",
        'room': "D01Z03S05"},
    {'name': "WotBC: Cliffside statue",
        'game_id': "HE02",
        'room': "D01Z03S07"},
    {'name': "WotBC: Cliffside Child of Moonlight",
        'game_id': "RESCUED_CHERUB_38",
        'room': "D01Z03S07"},
    {'name': "WotBC: 3rd meeting with Redento",
        'game_id': "RB20",
        'room': "D01Z03S06"},
    
    # Where Olive Trees Wither
    {'name': "WOTW: Below Prie Dieu",
        'game_id': "CO11",
        'room': "D02Z01S01"},
    {'name': "WOTW: Entrance to tomb",
        'game_id': "QI20",
        'room': "D02Z01S04"},
    {'name': "WOTW: Gift for the tomb",
        'game_id': "QI68",
        'room': "D02Z01S04"},
    {'name': "WOTW: Underground tomb",
        'game_id': "PR04",
        'room': "D02Z01S08"},
    {'name': "WOTW: Underground Child of Moonlight",
        'game_id': "RESCUED_CHERUB_27",
        'room': "D02Z01S06"},
    {'name': "WOTW: Underground ledge",
        'game_id': "CO19",
        'room': "D02Z01S06"},
    {'name': "WOTW: Upper east Child of Moonlight",
        'game_id': "RESCUED_CHERUB_23",
        'room': "D02Z01S02"},
    {'name': "WOTW: Upper east statue",
        'game_id': "HE05",
        'room': "D02Z01S09"},
    {'name': "WOTW: Death run",
        'game_id': "QI07",
        'room': "D02Z01S05"},
    {'name': "WOTW: Gemino's gift",
        'game_id': "QI59",
        'room': "D02Z01S01"},
    {'name': "WOTW: Gemino's reward",
        'game_id': "RB10",
        'room': "D02Z01S01"},

    # Various
    {'name': "Beginning gift",
        'game_id': "QI106",
        'room': "Misc"},
    {'name': "Second red candle",
        'game_id': "RB18",
        'room': "Misc"},
    {'name': "Third red candle",
        'game_id': "RB19",
        'room': "Misc"},
    {'name': "Second blue candle",
        'game_id': "RB25",
        'room': "Misc"},
    {'name': "Third blue candle",
        'game_id': "RB26",
        'room': "Misc"},
    {'name': "Confessor Dungeon 1 extra",
        'game_id': "Arena_NailManager[1000]",
        'room': "Misc"},
    {'name': "Confessor Dungeon 1 main",
        'game_id': "QI32",
        'room': "Misc"},
    {'name': "Confessor Dungeon 2 extra",
        'game_id': "HE10",
        'room': "Misc"},
    {'name': "Confessor Dungeon 2 main",
        'game_id': "QI33",
        'room': "Misc"},
    {'name': "Confessor Dungeon 3 extra",
        'game_id': "Arena_NailManager[3000]",
        'room': "Misc"},
    {'name': "Confessor Dungeon 3 main",
        'game_id': "QI34",
        'room': "Misc"},
    {'name': "Confessor Dungeon 4 extra",
        'game_id': "RB34",
        'room': "Misc"},
    {'name': "Confessor Dungeon 4 main",
        'game_id': "QI35",
        'room': "Misc"},
    {'name': "Confessor Dungeon 5 extra",
        'game_id': "Arena_NailManager[5000]",
        'room': "Misc"},
    {'name': "Confessor Dungeon 5 main",
        'game_id': "QI79",
        'room': "Misc"},
    {'name': "Confessor Dungeon 6 extra",
        'game_id': "RB35",
        'room': "Misc"},
    {'name': "Confessor Dungeon 6 main",
        'game_id': "QI80",
        'room': "Misc"},
    {'name': "Confessor Dungeon 7 extra",
        'game_id': "RB36",
        'room': "Misc"},
    {'name': "Confessor Dungeon 7 main",
        'game_id': "QI81",
        'room': "Misc"},
    {'name': "Defeat 1 Amanecida",
        'game_id': "QI107",
        'room': "Misc"},
    {'name': "Defeat 2 Amanecidas",
        'game_id': "QI108",
        'room': "Misc"},
    {'name': "Defeat 3 Amanecidas",
        'game_id': "QI109",
        'room': "Misc"},
    {'name': "Defeat 4 Amanecidas",
        'game_id': "QI110",
        'room': "Misc"},
    {'name': "Defeat all Amanecidas",
        'game_id': "PR101",
        'room': "Misc"},
    {'name': "Skill 1, Tier 1",
        'game_id': "COMBO_1",
        'room': "Misc"},
    {'name': "Skill 1, Tier 2",
        'game_id': "COMBO_2",
        'room': "Misc"},
    {'name': "Skill 1, Tier 3",
        'game_id': "COMBO_3",
        'room': "Misc"},
    {'name': "Skill 2, Tier 1",
        'game_id': "CHARGED_1",
        'room': "Misc"},
    {'name': "Skill 2, Tier 2",
        'game_id': "CHARGED_2",
        'room': "Misc"},
    {'name': "Skill 2, Tier 3",
        'game_id': "CHARGED_3",
        'room': "Misc"},
    {'name': "Skill 3, Tier 1",
        'game_id': "RANGED_1",
        'room': "Misc"},
    {'name': "Skill 3, Tier 2",
        'game_id': "RANGED_2",
        'room': "Misc"},
    {'name': "Skill 3, Tier 3",
        'game_id': "RANGED_3",
        'room': "Misc"},
    {'name': "Skill 4, Tier 1",
        'game_id': "VERTICAL_1",
        'room': "Misc"},
    {'name': "Skill 4, Tier 2",
        'game_id': "VERTICAL_2",
        'room': "Misc"},
    {'name': "Skill 4, Tier 3",
        'game_id': "VERTICAL_3",
        'room': "Misc"},
    {'name': "Skill 5, Tier 1",
        'game_id': "LUNGE_1",
        'room': "Misc"},
    {'name': "Skill 5, Tier 2",
        'game_id': "LUNGE_2",
        'room': "Misc"},
    {'name': "Skill 5, Tier 3",
        'game_id': "LUNGE_3",
        'room': "Misc"},

    # Custom Items
    {'name': "BotSS: 2nd meeting with Redento",
        'game_id': "RE401",
        'room': "D17Z01S04"},
    {'name': "MoM: Western room ledge",
        'game_id': "RE402",
        'room': "D04Z02S01"}
]
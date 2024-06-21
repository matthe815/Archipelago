"""
Author: Louis M
Date: Thu, 18 Apr 2024 18:45:56 +0000
Description: Unit test used to test accessibility of locations with and without the bind song (without the location
             under rock needing bind song option)
"""

from worlds.aquaria.test import AquariaTestBase, after_home_water_locations


class BindSongAccessTest(AquariaTestBase):
    """Unit test used to test accessibility of locations with and without the bind song"""
    options = {
        "bind_song_needed_to_get_under_rock_bulb": False,
    }

    def test_bind_song_location(self) -> None:
        """Test locations that require Bind song"""
        locations = [
            "Verse Cave right area, Big Seed",
            "Home Water, bulb in the path below Nautilus Prime",
            "Home Water, bulb in the bottom left room",
            "Home Water, Nautilus Egg",
            "Song Cave, Verse Egg",
            "Energy Temple first area, beating the Energy Statue",
            "Energy Temple first area, bulb in the bottom room blocked by a rock",
            "Energy Temple first area, Energy Idol",
            "Energy Temple second area, bulb under the rock",
            "Energy Temple bottom entrance, Krotite Armor",
            "Energy Temple third area, bulb in the bottom path",
            "Energy Temple boss area, Fallen God Tooth",
            "Energy Temple blaster room, Blaster Egg",
            *after_home_water_locations
        ]
        items = [["Bind song"]]
        self.assertAccessDependency(locations, items)

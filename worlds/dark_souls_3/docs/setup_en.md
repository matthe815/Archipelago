# Dark Souls III Randomizer Setup Guide

## Required Software

- [Dark Souls III](https://store.steampowered.com/app/374320/DARK_SOULS_III/)
- [Dark Souls III AP Client](https://github.com/Marechal-L/Dark-Souls-III-Archipelago-client/releases)

## Optional Software

- [Dark Souls III Maptracker Pack](https://github.com/Br00ty/DS3_AP_Maptracker/releases/latest), for use with [Poptracker](https://github.com/black-sliver/PopTracker/releases)

## General Concept

<span style="color:#ff7800">
**This mod can ban you permanently from the FromSoftware servers if used online.** 
</span>
The Dark Souls III AP Client is a dinput8.dll triggered when launching Dark Souls III. This .dll file will launch a command 
prompt where you can read information about your run and write any command to interact with the Archipelago server.

This client has only been tested with the Official Steam version of the game at version 1.15. It does not matter which DLCs are installed. However, you will have to downpatch your Dark Souls III installation from current patch.

## Downpatching Dark Souls III

To downpatch DS3 for use with Archipelago, use the following instructions from the speedsouls wiki database. 

1. Launch Steam (in online mode).
2. Press the Windows Key + R. This will open the Run window.
3. Open the Steam console by typing the following string: `steam://open/console`. Steam should now open in Console Mode.
4. Insert the string of the depot you wish to download. For the AP-supported v1.15, you will want to use: `download_depot 374320 374321 4471176929659548333`.
5. Steam will now download the depot. Note: There is no progress bar for the download in Steam, but it is still downloading in the background.
6. Back up your existing game executable (`DarkSoulsIII.exe`) found in `\Steam\steamapps\common\DARK SOULS III\Game`. Easiest way to do this is to move it to another directory. If you have file extensions enabled, you can instead rename the executable to `DarkSoulsIII.exe.bak`.
7. Return to the Steam console. Once the download is complete, it should say so along with the temporary local directory in which the depot has been stored. This is usually something like `\Steam\steamapps\content\app_XXXXXX\depot_XXXXXX`.
8. Take the `DarkSoulsIII.exe` from that folder and place it in `\Steam\steamapps\common\DARK SOULS III\Game`.
9. Back up and delete your save file (`DS30000.sl2`) in AppData. AppData is hidden by default. To locate it, press Windows Key + R, type `%appdata%` and hit enter. Alternatively: open File Explorer > View > Hidden Items and follow `C:\Users\<your_username>\AppData\Roaming\DarkSoulsIII\<numbers>`.
10. If you did all these steps correctly, you should be able to confirm your game version in the upper-left corner after launching Dark Souls III.


## Installing the Archipelago mod

Get the `dinput8.dll` from the [Dark Souls III AP Client](https://github.com/Marechal-L/Dark-Souls-III-Archipelago-client/releases) and 
add it at the root folder of your game (e.g. `SteamLibrary\steamapps\common\DARK SOULS III\Game`)

## Joining a MultiWorld Game

1. Run Steam in offline mode to avoid being banned.
2. Launch Dark Souls III.
3. Type in `/connect {SERVER_IP}:{SERVER_PORT} {SLOT_NAME} password:{PASSWORD}` in the "Windows Command Prompt" that opened. For example: `/connect archipelago.gg:38281 "Example Name" password:"Example Password"`. The password parameter is only necessary if your game requires one.
4. Once connected, create a new game, choose a class and wait for the others before starting.
5. You can quit and launch at anytime during a game.

## Where do I get a config file?

The [Player Options](/games/Dark%20Souls%20III/player-options) page on the website allows you to
configure your personal options and export them into a config file.

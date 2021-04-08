# API Docs

## /api/v1

### URL Arguments

 - url: A paste.gg/pastebin.com URL.

### Response

```json
{
  "plugins": [
    "BlockParticles v1.11.1-RELEASE",
    "LuckPerms v5.1.26",
    "WorldEdit v6.1.9;caf0ad9",
    "PlaceholderAPI v2.10.9",
    "BedWarsFireballFix v0.2",
    "ImageOnMap v3.1",
    "ViaVersion v3.2.1",
    "CraftingStore v2.6.4",
    "Vault v1.7.3-b131",
    "ViaBackwards v3.2.0",
    "ViaRewind v1.5.3",
    "Essentials v2.19.0-dev+99-1e0d7fb",
    "ProtocolLib v4.5.1",
    "Spartan vBuild 386",
    "SkinsRestorer v14.0.2",
    "Citizens v2.0.27-SNAPSHOT (build 2084)",
    "OldCombatMechanics v1.9.0",
    "DeluxeMenus v1.13.3-Release",
    "BedWars1058 vgit-e3ad6f83-21.1-SNAPSHOT",
    "BedWars1058-PopUpTowers v0.5",
    "TAB v2.8.3",
    "BedWars1058-GenSplit v0.3",
    "CommandNPC v1.9.1",
    "BedWars1058-TeamSelector v0.5.2",
    "GadgetsMenu v4.4.7",
    "BedWars1058-Cmds v1.4.1",
    "HolographicDisplays v2.4.6",
    "LiteBans v2.6.7",
    "BlockCommandTab v2.0.3",
    "BedWars1058-Map v0.6",
    "HolographicExtension v1.10.9"
  ],
  "plugins_altver": [
    "BlockParticles",
    "LuckPerms",
    "WorldEdit",
    "PlaceholderAPI",
    "BedWarsFireballFix",
    "ImageOnMap",
    "ViaVersion",
    "CraftingStore",
    "Vault",
    "ViaBackwards",
    "ViaRewind",
    "Essentials",
    "ProtocolLib",
    "Spartan",
    "SkinsRestorer",
    "Citizens",
    "OldCombatMechanics",
    "DeluxeMenus",
    "BedWars1058",
    "BedWars1058-PopUpTowers",
    "TAB",
    "BedWars1058-GenSplit",
    "CommandNPC",
    "BedWars1058-TeamSelector",
    "GadgetsMenu",
    "BedWars1058-Cmds",
    "HolographicDisplays",
    "LiteBans",
    "BlockCommandTab",
    "BedWars1058-Map",
    "HolographicExtension"
  ],
  "errors": [
    "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram 'spawn' was in the world 'BedWars' but it wasn't loaded.",
    "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram 'solo' was in the world 'BedWars' but it wasn't loaded.",
    "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram 'doubles' was in the world 'BedWars' but it wasn't loaded.",
    "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram '3v3v3v3' was in the world 'BedWars' but it wasn't loaded.",
    "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram '4v4v4v4' was in the world 'BedWars' but it wasn't loaded.",
    "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram 'stats' was in the world 'BedWars' but it wasn't loaded.",
    "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram 'credits' was in the world 'BedWars' but it wasn't loaded.",
    "[10:42:04] [Craft Scheduler Thread - 32/WARN]: java.sql.SQLException: no such column: 'Pet_Name'",
    "[10:42:04] [Craft Scheduler Thread - 32/WARN]: at org.sqlite.jdbc3.JDBC3ResultSet.findColumn(JDBC3ResultSet.java:48)",
    "[10:42:04] [Craft Scheduler Thread - 32/WARN]: at org.sqlite.jdbc3.JDBC3ResultSet.getString(JDBC3ResultSet.java:443)",
    "[10:42:04] [Craft Scheduler Thread - 32/WARN]: at com.yapzhenyie.GadgetsMenu.database.sqlite.SQLiteUtils.initPlayerStats(SQLiteUtils.java:63)",
    "[10:42:04] [Craft Scheduler Thread - 32/WARN]: at com.yapzhenyie.GadgetsMenu.player.GPlayer.initPlayer(GPlayer.java:91)",
    "[10:42:04] [Craft Scheduler Thread - 32/WARN]: at com.yapzhenyie.GadgetsMenu.listeners.PlayerListener.lambda$0(PlayerListener.java:35)",
    "[10:42:04] [Craft Scheduler Thread - 32/WARN]: at org.bukkit.craftbukkit.v1_12_R1.scheduler.CraftTask.run(CraftTask.java:64)",
    "[10:42:04] [Craft Scheduler Thread - 32/WARN]: at org.bukkit.craftbukkit.v1_12_R1.scheduler.CraftAsyncTask.run(CraftAsyncTask.java:52)"
  ],
  "classified_errors": {
    "BlockParticles": null,
    "LuckPerms": null,
    "WorldEdit": null,
    "PlaceholderAPI": null,
    "BedWarsFireballFix": null,
    "ImageOnMap": null,
    "ViaVersion": null,
    "CraftingStore": null,
    "Vault": null,
    "ViaBackwards": null,
    "ViaRewind": null,
    "Essentials": null,
    "ProtocolLib": null,
    "Spartan": null,
    "SkinsRestorer": null,
    "Citizens": null,
    "OldCombatMechanics": null,
    "DeluxeMenus": null,
    "BedWars1058": null,
    "BedWars1058-PopUpTowers": null,
    "TAB": null,
    "BedWars1058-GenSplit": null,
    "CommandNPC": null,
    "BedWars1058-TeamSelector": null,
    "GadgetsMenu": [
      "[10:42:04] [Craft Scheduler Thread - 32/WARN]: at com.yapzhenyie.GadgetsMenu.database.sqlite.SQLiteUtils.initPlayerStats(SQLiteUtils.java:63)",
      "[10:42:04] [Craft Scheduler Thread - 32/WARN]: at com.yapzhenyie.GadgetsMenu.player.GPlayer.initPlayer(GPlayer.java:91)",
      "[10:42:04] [Craft Scheduler Thread - 32/WARN]: at com.yapzhenyie.GadgetsMenu.listeners.PlayerListener.lambda$0(PlayerListener.java:35)"
    ],
    "BedWars1058-Cmds": null,
    "HolographicDisplays": [
      "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram 'spawn' was in the world 'BedWars' but it wasn't loaded.",
      "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram 'solo' was in the world 'BedWars' but it wasn't loaded.",
      "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram 'doubles' was in the world 'BedWars' but it wasn't loaded.",
      "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram '3v3v3v3' was in the world 'BedWars' but it wasn't loaded.",
      "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram '4v4v4v4' was in the world 'BedWars' but it wasn't loaded.",
      "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram 'stats' was in the world 'BedWars' but it wasn't loaded.",
      "[10:41:52] [Server thread/WARN]: [HolographicDisplays] Hologram 'credits' was in the world 'BedWars' but it wasn't loaded."
    ],
    "LiteBans": null,
    "BlockCommandTab": null,
    "BedWars1058-Map": null,
    "HolographicExtension": null
  },
  "minecraft_version": "1.12.2",
  "server_software": "git-Paper-1611",
  "needs_newer_java": false,
  "reload": false,
  "sbw_wrongshop": false
}
```

 - plugins: A list of plugins **with** versions, can be empty
 - plugins_altver: A list of plugins **without** versions, can be empty
 - errors: A list of identified errors, can be empty
 - classified_errors: A object with the errors sorted by plugins, plugin name has null instead of an array if there are no errors, can be empty (experimental)
 - minecraft_version: A string with the identified Minecraft version, can be null
 - server_software: A string with the identified server software details, usually in the form "git-serversoftware-buildnumber", can be null
 - needs_newer_java: A boolean, stating if a UnsupportedClassVersionError was found, indicating outdated Java, can be true or false
 - reload: A boolean, indicating if the server has been reloaded, can be true or false
 - sbw_wrongshop: A boolean exclusive to ScreamingBedWars, indicating if the shop.yml is configured wrongly, can be true of false
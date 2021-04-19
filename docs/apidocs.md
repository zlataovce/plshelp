# API Docs

## /api/v1

### URL Arguments

 - url: A paste.gg/pastebin.com URL.

### Response

```json
{
  "plugins": [
    "LuckPerms v5.3.3",
    "VoidGenerator v1.7.0",
    "PlaceholderAPI v2.10.9",
    "AmkMcAuth v1.5.1",
    "HolographicDisplays v2.4.6",
    "Vault v1.7.3-b131",
    "ServersNPC v3.1",
    "LPC v3.2.0",
    "WorldEdit v7.2.4+5723-e3bfc64",
    "OldCombatMechanics v1.9.0",
    "TNTRun_reloaded v9.9",
    "Scoreboard-revision vR4 1.1 RELEASE",
    "Essentials v2.18.2.0",
    "PlotSquared v4.4.495",
    "EssentialsSpawn v2.18.2.0",
    "Multiverse-Core v4.2.2-b812",
    "WorldGuard v7.0.4+f7ff984",
    "TheBridge v2.4",
    "Essentials_WarpGUI v2.2.2",
    "Multiverse-Inventories v4.2.2-b500",
    "IridiumSkyblock v2.6.7",
    "BedWars v0.2.15",
    "PaintballBattle v1.5.1",
    "SBAHypixelify v1.4.3"
  ],
  "plugins_altver": [
    "LuckPerms",
    "VoidGenerator",
    "PlaceholderAPI",
    "AmkMcAuth",
    "HolographicDisplays",
    "Vault",
    "ServersNPC",
    "LPC",
    "WorldEdit",
    "OldCombatMechanics",
    "TNTRun_reloaded",
    "Scoreboard-revision",
    "Essentials",
    "PlotSquared",
    "EssentialsSpawn",
    "Multiverse-Core",
    "WorldGuard",
    "TheBridge",
    "Essentials_WarpGUI",
    "Multiverse-Inventories",
    "IridiumSkyblock",
    "BedWars",
    "PaintballBattle",
    "SBAHypixelify"
  ],
  "errors": [
    "[12:55:53] [Server thread/ERROR]: [Essentials] You are running an unsupported server version!",
    "[12:55:57] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:56:01] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:56:02] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:56:05] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:56:05] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:56:06] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:57:45] [Server thread/ERROR]: Could not pass event BedwarsGameStartedEvent to SBAHypixelify v1.4.3",
    "java.lang.NullPointerException: null",
    "at io.pronze.hypixelify.game.Arena.lambda$initalizeGenerators$3(Arena.java:100) ~[?:?]",
    "at java.util.ArrayList.forEach(ArrayList.java:1541) ~[?:?]",
    "at io.pronze.hypixelify.game.Arena.initalizeGenerators(Arena.java:99) ~[?:?]",
    "at io.pronze.hypixelify.game.Arena.onGameStarted(Arena.java:92) ~[?:?]",
    "at io.pronze.hypixelify.listener.BedwarsListener.onStarted(BedwarsListener.java:37) ~[?:?]",
    "at com.destroystokyo.paper.event.executor.asm.generated.GeneratedEventExecutor594.execute(Unknown Source) ~[?:?]",
    "[12:57:47] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
    "java.lang.NullPointerException: null",
    "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
    "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]",
    "[12:57:48] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
    "java.lang.NullPointerException: null",
    "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
    "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]",
    "[12:57:49] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
    "java.lang.NullPointerException: null",
    "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
    "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]",
    "[12:57:51] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
    "java.lang.NullPointerException: null",
    "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
    "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]"
  ],
  "classified_errors": {
    "VoidGenerator": [
      "[12:55:57] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
      "[12:56:01] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
      "[12:56:02] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
      "[12:56:05] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
      "[12:56:05] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
      "[12:56:06] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\"."
    ],
    "Essentials": [
      "[12:55:53] [Server thread/ERROR]: [Essentials] You are running an unsupported server version!"
    ],
    "BedWars": [
      "[12:57:47] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
      "java.lang.NullPointerException: null",
      "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
      "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]",
      "[12:57:49] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
      "java.lang.NullPointerException: null",
      "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
      "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]"
    ],
    "SBAHypixelify": [
      "[12:57:45] [Server thread/ERROR]: Could not pass event BedwarsGameStartedEvent to SBAHypixelify v1.4.3",
      "java.lang.NullPointerException: null",
      "at io.pronze.hypixelify.game.Arena.lambda$initalizeGenerators$3(Arena.java:100) ~[?:?]",
      "at java.util.ArrayList.forEach(ArrayList.java:1541) ~[?:?]",
      "at io.pronze.hypixelify.game.Arena.initalizeGenerators(Arena.java:99) ~[?:?]",
      "at io.pronze.hypixelify.game.Arena.onGameStarted(Arena.java:92) ~[?:?]",
      "at io.pronze.hypixelify.listener.BedwarsListener.onStarted(BedwarsListener.java:37) ~[?:?]",
      "at com.destroystokyo.paper.event.executor.asm.generated.GeneratedEventExecutor594.execute(Unknown Source) ~[?:?]"
    ]
  },
  "minecraft_version": "1.16.5",
  "server_software": "git-Paper-575",
  "reload": true,
  "needs_newer_java": false,
  "sbw_wrongshop": false,
  "cracked_plugins": false
}
```

 - plugins: A list of plugins **with** versions, can be empty
 - plugins_altver: A list of plugins **without** versions, can be empty
 - errors: A list of identified errors, can be empty
 - classified_errors: A object with the errors sorted by plugins, can be empty (experimental)
 - minecraft_version: A string with the identified Minecraft version, can be null
 - server_software: A string with the identified server software details, usually in the form "git-serversoftware-buildnumber", can be null
 - needs_newer_java: A boolean, stating if a UnsupportedClassVersionError was found, indicating outdated Java, can be true or false
 - reload: A boolean, indicating if the server has been reloaded, can be true or false
 - sbw_wrongshop: A boolean exclusive to ScreamingBedWars, indicating if the shop.yml is configured wrongly, can be true of false
 - cracked_plugins: A boolean indicating if the server is running cracked plugins


## /api/v2

### URL Arguments

- url: A paste.gg/pastebin.com URL.

### Response

```json
{
  "plugins": [
    "LuckPerms v5.3.3",
    "VoidGenerator v1.7.0",
    "PlaceholderAPI v2.10.9",
    "AmkMcAuth v1.5.1",
    "HolographicDisplays v2.4.6",
    "Vault v1.7.3-b131",
    "ServersNPC v3.1",
    "LPC v3.2.0",
    "WorldEdit v7.2.4+5723-e3bfc64",
    "OldCombatMechanics v1.9.0",
    "TNTRun_reloaded v9.9",
    "Scoreboard-revision vR4 1.1 RELEASE",
    "Essentials v2.18.2.0",
    "PlotSquared v4.4.495",
    "EssentialsSpawn v2.18.2.0",
    "Multiverse-Core v4.2.2-b812",
    "WorldGuard v7.0.4+f7ff984",
    "TheBridge v2.4",
    "Essentials_WarpGUI v2.2.2",
    "Multiverse-Inventories v4.2.2-b500",
    "IridiumSkyblock v2.6.7",
    "BedWars v0.2.15",
    "PaintballBattle v1.5.1",
    "SBAHypixelify v1.4.3"
  ],
  "plugins_altver": [
    "LuckPerms",
    "VoidGenerator",
    "PlaceholderAPI",
    "AmkMcAuth",
    "HolographicDisplays",
    "Vault",
    "ServersNPC",
    "LPC",
    "WorldEdit",
    "OldCombatMechanics",
    "TNTRun_reloaded",
    "Scoreboard-revision",
    "Essentials",
    "PlotSquared",
    "EssentialsSpawn",
    "Multiverse-Core",
    "WorldGuard",
    "TheBridge",
    "Essentials_WarpGUI",
    "Multiverse-Inventories",
    "IridiumSkyblock",
    "BedWars",
    "PaintballBattle",
    "SBAHypixelify"
  ],
  "errors": [
    "[12:55:53] [Server thread/ERROR]: [Essentials] You are running an unsupported server version!",
    "[12:55:57] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:56:01] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:56:02] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:56:05] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:56:05] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:56:06] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
    "[12:57:45] [Server thread/ERROR]: Could not pass event BedwarsGameStartedEvent to SBAHypixelify v1.4.3",
    "java.lang.NullPointerException: null",
    "at io.pronze.hypixelify.game.Arena.lambda$initalizeGenerators$3(Arena.java:100) ~[?:?]",
    "at java.util.ArrayList.forEach(ArrayList.java:1541) ~[?:?]",
    "at io.pronze.hypixelify.game.Arena.initalizeGenerators(Arena.java:99) ~[?:?]",
    "at io.pronze.hypixelify.game.Arena.onGameStarted(Arena.java:92) ~[?:?]",
    "at io.pronze.hypixelify.listener.BedwarsListener.onStarted(BedwarsListener.java:37) ~[?:?]",
    "at com.destroystokyo.paper.event.executor.asm.generated.GeneratedEventExecutor594.execute(Unknown Source) ~[?:?]",
    "[12:57:47] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
    "java.lang.NullPointerException: null",
    "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
    "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]",
    "[12:57:48] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
    "java.lang.NullPointerException: null",
    "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
    "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]",
    "[12:57:49] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
    "java.lang.NullPointerException: null",
    "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
    "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
    "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
    "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]"
  ],
  "classified_errors": {
    "VoidGenerator": [
      "[12:55:57] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
      "[12:56:01] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
      "[12:56:02] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
      "[12:56:05] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
      "[12:56:05] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\".",
      "[12:56:06] [Server thread/ERROR]: [VoidGenerator] The BiomeID: \"void\" is invalid. The biome defaulted to \"THE_VOID\"."
    ],
    "Essentials": [
      "[12:55:53] [Server thread/ERROR]: [Essentials] You are running an unsupported server version!"
    ],
    "BedWars": [
      "[12:57:47] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
      "java.lang.NullPointerException: null",
      "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
      "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]",
      "[12:57:49] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
      "java.lang.NullPointerException: null",
      "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
      "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]",
      "[12:57:52] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
      "java.lang.NullPointerException: null",
      "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
      "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]",
      "[12:57:54] [Server thread/WARN]: [BedWars] Task #3006 for BedWars v0.2.15 generated an exception",
      "java.lang.NullPointerException: null",
      "at org.screamingsandals.bedwars.game.Game.run(Game.java:1995) ~[?:?]",
      "at org.screamingsandals.bedwars.game.Game$7.run(Game.java:2254) ~[?:?]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftTask.run(CraftTask.java:100) ~[minecraft_server.jar:git-Paper-575]",
      "at org.bukkit.craftbukkit.v1_16_R3.scheduler.CraftScheduler.mainThreadHeartbeat(CraftScheduler.java:468) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.MinecraftServer.b(MinecraftServer.java:1413) ~[minecraft_server.jar:git-Paper-575]",
      "at net.minecraft.server.v1_16_R3.DedicatedServer.b(DedicatedServer.java:418) ~[minecraft_server.jar:git-Paper-575]"
    ],
    "SBAHypixelify": [
      "[12:57:45] [Server thread/ERROR]: Could not pass event BedwarsGameStartedEvent to SBAHypixelify v1.4.3",
      "java.lang.NullPointerException: null",
      "at io.pronze.hypixelify.game.Arena.lambda$initalizeGenerators$3(Arena.java:100) ~[?:?]",
      "at java.util.ArrayList.forEach(ArrayList.java:1541) ~[?:?]",
      "at io.pronze.hypixelify.game.Arena.initalizeGenerators(Arena.java:99) ~[?:?]",
      "at io.pronze.hypixelify.game.Arena.onGameStarted(Arena.java:92) ~[?:?]",
      "at io.pronze.hypixelify.listener.BedwarsListener.onStarted(BedwarsListener.java:37) ~[?:?]",
      "at com.destroystokyo.paper.event.executor.asm.generated.GeneratedEventExecutor594.execute(Unknown Source) ~[?:?]"
    ]
  },
  "minecraft_version": "1.16.5",
  "server_software": "git-Paper-575",
  "reload": true,
  "needs_newer_java": false,
  "sbw_wrongshop": false,
  "cracked_plugins": false,
  "gravity_classified_plugins": {
    "BedWars": {
      "latest_build": 786,
      "attributes": [
        "This plugin needs Java 11 or higher to function. (java11)",
        "This plugin is known to have broken snapshots/dev builds. (risksnapshots)"
      ]
    },
    "SBAHypixelify": {
      "latest_build": 160,
      "attributes": [
        "This plugin needs Java 11 or higher to function. (java11)",
        "This plugin is known to have broken snapshots/dev builds. (risksnapshots)"
      ]
    },
    "Essentials": {
      "latest_build": "2.18.2",
      "attributes": null
    },
    "LuckPerms": {
      "latest_build": "5.3.25",
      "attributes": null
    },
    "PlaceholderAPI": {
      "latest_build": "2.10.9",
      "attributes": null
    },
    "Multiverse-Core": {
      "latest_build": 837,
      "attributes": null
    },
    "Multiverse-Inventories": {
      "latest_build": 511,
      "attributes": null
    }
  },
  "paper_build": 599,
  "error_causing_plugins": ["VoidGenerator", "Essentials", "BedWars", "SBAHypixelify"]
}
```

- plugins: A list of plugins **with** versions, can be empty
- plugins_altver: A list of plugins **without** versions, can be empty
- errors: A list of identified errors, can be empty
- classified_errors: A object with the errors sorted by plugins, can be empty (experimental)
- minecraft_version: A string with the identified Minecraft version, can be null
- server_software: A string with the identified server software details, usually in the form "git-serversoftware-buildnumber", can be null
- needs_newer_java: A boolean, stating if a UnsupportedClassVersionError was found, indicating outdated Java, can be true or false
- reload: A boolean, indicating if the server has been reloaded, can be true or false
- sbw_wrongshop: A boolean exclusive to ScreamingBedWars, indicating if the shop.yml is configured wrongly, can be true of false
- cracked_plugins: A boolean indicating if the server is running cracked plugins
- gravity_classified_plugins: A list of plugins classified by plshelp gravity
  - latest_build: A string/integer showing the latest build of the indicated plugin, can be null if it cannot be determined
  - attributes: An array with warnings from plshelp gravity for this plugin, can be null if there are no warnings
- paper_build: An integer showing the latest build of Paper (can be null if the server software isn't Paper)
- current_paper_build: An integer showing the build of Paper that is installed on the server (can be null if the server software isn't Paper)
- outdated_paper: An integer showing by how many builds is the installed Paper behind the latest, the result is 0 if Paper is up-to-date (can be null if the server software isn't Paper)
- error_causing_plugins: An array containing the troublesome plugin names
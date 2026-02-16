# Villager Voices+ Resource Pack (Minecraft 1.20.1)

This is a **ready-to-use resource pack** for Minecraft Java **1.20.1**.

## Important (why packs sometimes do not appear)

A Minecraft resource pack is only detected when **`pack.mcmeta` is at the top level** of the pack.

Correct:

- `resourcepacks/VillagerVoicesPlus_1.20.1.zip`
  - `pack.mcmeta`
  - `pack.png`
  - `assets/...`

Incorrect (won't appear):

- `resourcepacks/VillagerVoicesPlus_1.20.1.zip`
  - `VillagerVoicesPlus_1.20.1/`
    - `pack.mcmeta`

To make this easy, this repo includes both:

- **`VillagerVoicesPlus_1.20.1/`** (ready-to-copy folder)
- **`VillagerVoicesPlus_1.20.1.zip`** (ready-to-copy zip)

Copy either one directly into your `resourcepacks` folder.

## What it does

It replaces villager sounds with your own audio files:

- `yes1.ogg` to `yes3.ogg`
- `no1.ogg` to `no3.ogg`
- `hit1.ogg` to `hit10.ogg`
- `haggle1.ogg` to `haggle3.ogg`
- `idle1.ogg` to `idle20.ogg`

It also makes villager voice playback:

- **quieter** (`volume: 0.65`)
- **shorter draw distance** (`attenuation_distance: 8`)

These values are in `assets/minecraft/sounds.json` and are configurable.

## Where to put your audio files

Put your `.ogg` files into these folders:

- `assets/minecraft/sounds/villager_custom/yes/`
- `assets/minecraft/sounds/villager_custom/no/`
- `assets/minecraft/sounds/villager_custom/hit/`
- `assets/minecraft/sounds/villager_custom/haggle/`
- `assets/minecraft/sounds/villager_custom/idle/`

## Install

1. Copy either **`VillagerVoicesPlus_1.20.1/`** or **`VillagerVoicesPlus_1.20.1.zip`** into your Minecraft `resourcepacks` folder.
2. If you use the folder version, paste your `.ogg` files into its matching `assets/minecraft/sounds/villager_custom/...` folders.
3. Open Minecraft → Options → Resource Packs → enable **Villager Voices+**.

## Expanding idle sounds beyond 20 (optional)

Minecraft requires listed entries in `sounds.json`.

If you add files like `idle21.ogg`, `idle22.ogg`, etc., run:

```bash
python scripts/build_sounds_json.py
```

That script scans your folders and rewrites `assets/minecraft/sounds.json` automatically.

Then rebuild the zip with:

```bash
python scripts/build_pack_zip.py
```

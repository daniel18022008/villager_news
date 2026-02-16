# Villager Voices+ Resource Pack (Minecraft 1.20.1)

This repository is a **ready-to-use resource pack** for Minecraft Java **1.20.1**.

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

These values are in `assets/minecraft/sounds.json` and can be edited.

## Folder layout for your audio files

Put your `.ogg` files into these folders:

- `assets/minecraft/sounds/villager_custom/yes/`
- `assets/minecraft/sounds/villager_custom/no/`
- `assets/minecraft/sounds/villager_custom/hit/`
- `assets/minecraft/sounds/villager_custom/haggle/`
- `assets/minecraft/sounds/villager_custom/idle/`

## Use it (no extra setup)

1. Copy this whole folder as a zip (or folder) into your Minecraft `resourcepacks` directory.
2. Drop your `.ogg` files into the folders above, following the exact names.
3. Enable the pack in Minecraft.

With the required filenames above, it works immediately.

## Expanding idle sounds beyond 20

Minecraft resource packs require each sound entry to be listed in `sounds.json`.

To automatically include extra files (example: `idle21.ogg`, `idle22.ogg`, etc.), this pack includes:

- `scripts/build_sounds_json.py`

Run:

```bash
python scripts/build_sounds_json.py
```

That script scans your audio folders and rewrites `assets/minecraft/sounds.json` with every detected file.

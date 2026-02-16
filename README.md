# Villager News Voice Pack (Minecraft 1.20.1)

This repo contains a **resource pack + generator script** for Minecraft **1.20.1** (works in Forge packs too), replacing villager sounds with your own `.ogg` files.

## What this does

- Replaces villager events:
  - `entity.villager.yes` (yes sounds)
  - `entity.villager.no` (no sounds)
  - `entity.villager.hurt` (hit sounds)
  - `entity.villager.trade` (haggle sounds)
  - `entity.villager.ambient` (idle sounds)
- Makes villager talking **quieter** and **shorter draw distance** by default.
- Is easy to expand: add more files (for example `idle21.ogg`) and re-run one command.

## Folder layout

Put audio files in:

- `resourcepack/assets/minecraft/sounds/entity/villager/custom/yes`
- `resourcepack/assets/minecraft/sounds/entity/villager/custom/no`
- `resourcepack/assets/minecraft/sounds/entity/villager/custom/hit`
- `resourcepack/assets/minecraft/sounds/entity/villager/custom/haggle`
- `resourcepack/assets/minecraft/sounds/entity/villager/custom/idle`

Expected naming examples:

- `yes1.ogg`, `yes2.ogg`, `yes3.ogg`
- `no1.ogg`, `no2.ogg`, `no3.ogg`
- `hit1.ogg` ... `hit10.ogg`
- `haggle1.ogg`, `haggle2.ogg`, `haggle3.ogg`
- `idle1.ogg` ... `idle20.ogg`, and expandable (`idle21.ogg`, etc.)

## Configure volume and distance

Edit `config/audio_config.json`.

Each event has:

- `volume` (lower = quieter)
- `attenuation_distance` (lower = shorter audible range)

## Build the pack metadata

After adding/changing `.ogg` files:

```bash
python3 tools/generate_sounds.py
```

This regenerates:

- `resourcepack/assets/minecraft/sounds.json`

## Install in Minecraft / Forge 1.20.1

1. Run generator script.
2. Zip the **contents** of `resourcepack/` (not the parent folder).
3. Place zip in Minecraft `resourcepacks` folder.
4. Enable the pack in-game.

## Notes

- Minecraft does not auto-detect brand new sound files without updating `sounds.json`.
- This repo solves that with a script, so expansion is still easy.

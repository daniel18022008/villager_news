# Villager Voice Refresh (Minecraft 1.20.1 resource pack)

This is a **resource pack** (Forge-compatible) that replaces villager voice sounds.

## What this pack changes
- Replaces villager `yes`, `no`, `hurt`, `trade` (haggle), and `ambient` (idle) sounds.
- Makes villager speaking quieter and with shorter hearing distance by default.
- Keeps settings editable in `sound_settings.json`.

## Audio files to add
Put your `.ogg` files into these folders:

- `assets/minecraft/sounds/villager/yes/`
  - `yes1.ogg`, `yes2.ogg`, `yes3.ogg`
- `assets/minecraft/sounds/villager/no/`
  - `no1.ogg`, `no2.ogg`, `no3.ogg`
- `assets/minecraft/sounds/villager/hit/`
  - `hit1.ogg` ... `hit10.ogg`
- `assets/minecraft/sounds/villager/haggle/`
  - `haggle1.ogg`, `haggle2.ogg`, `haggle3.ogg`
- `assets/minecraft/sounds/villager/idle/`
  - `idle1.ogg` ... `idle20.ogg`

Once those files are in place, the pack works directly in-game.

## Expanding idle (or any category)
To add more clips (example: `idle21.ogg`), add the file and run:

```bash
python3 scripts/generate_sounds_json.py
```

The script auto-detects numbered files and updates `assets/minecraft/sounds.json`.

## Tuning loudness and distance
Edit `sound_settings.json` and regenerate `sounds.json` with the script above.

- `volume`: lower = quieter
- `attenuation_distance`: lower = shorter audible distance

## Install
1. Zip this `villager_voice_pack` folder, or keep it as a folder.
2. Put it in your Minecraft `resourcepacks` directory.
3. Enable it in **Options → Resource Packs**.

> Note: `pack.png` is intentionally not included.

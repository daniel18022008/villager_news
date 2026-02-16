#!/usr/bin/env python3
"""Generate assets/minecraft/sounds.json for villager replacement sounds.

This scans custom folders and updates Minecraft's built-in villager events:
- entity.villager.yes
- entity.villager.no
- entity.villager.hurt
- entity.villager.trade
- entity.villager.ambient
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "audio_config.json"
SOUNDS_ROOT = ROOT / "resourcepack" / "assets" / "minecraft" / "sounds" / "entity" / "villager" / "custom"
OUTPUT_PATH = ROOT / "resourcepack" / "assets" / "minecraft" / "sounds.json"

CATEGORIES = {
    "yes": "entity.villager.yes",
    "no": "entity.villager.no",
    "hit": "entity.villager.hurt",
    "haggle": "entity.villager.trade",
    "idle": "entity.villager.ambient",
}


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise RuntimeError(f"Missing config file: {CONFIG_PATH}")
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def find_ogg_files(category: str) -> list[Path]:
    folder = SOUNDS_ROOT / category
    if not folder.exists():
        return []
    return sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() == ".ogg")


def build_sound_entry(category: str, config: dict) -> dict | None:
    files = find_ogg_files(category)
    if not files:
        return None

    event_cfg = config.get("events", {}).get(category, {})
    volume = float(event_cfg.get("volume", 1.0))
    attenuation_distance = int(event_cfg.get("attenuation_distance", 16))

    sounds = []
    for file_path in files:
        sound_name = file_path.stem
        sounds.append(
            {
                "name": f"entity/villager/custom/{category}/{sound_name}",
                "stream": False,
                "volume": volume,
                "attenuation_distance": attenuation_distance,
            }
        )

    return {
        "replace": True,
        "sounds": sounds,
    }


def generate() -> None:
    config = load_config()

    output_data = {}
    for category, event_name in CATEGORIES.items():
        entry = build_sound_entry(category, config)
        if entry is not None:
            output_data[event_name] = entry

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)
        f.write("\n")

    print(f"Generated {OUTPUT_PATH}")
    for category, event_name in CATEGORIES.items():
        count = len(find_ogg_files(category))
        if count:
            print(f"- {event_name}: {count} file(s)")
        else:
            print(f"- {event_name}: no files (vanilla sound kept)")


if __name__ == "__main__":
    generate()

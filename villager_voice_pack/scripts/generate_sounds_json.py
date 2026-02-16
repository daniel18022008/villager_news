#!/usr/bin/env python3
"""Generate assets/minecraft/sounds.json from files in assets/minecraft/sounds/villager.

Default numbered slots are always included so the pack works immediately with the
expected base files. Extra files (example: idle21.ogg) are auto-detected.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

PACK_ROOT = Path(__file__).resolve().parents[1]
SOUNDS_ROOT = PACK_ROOT / "assets" / "minecraft" / "sounds" / "villager"
SETTINGS_PATH = PACK_ROOT / "sound_settings.json"
OUTPUT_PATH = PACK_ROOT / "assets" / "minecraft" / "sounds.json"

SOUND_GROUPS = {
    "yes": "entity.villager.yes",
    "no": "entity.villager.no",
    "hit": "entity.villager.hurt",
    "haggle": "entity.villager.trade",
    "idle": "entity.villager.ambient",
}

DEFAULT_COUNTS = {
    "yes": 3,
    "no": 3,
    "hit": 10,
    "haggle": 3,
    "idle": 20,
}


def list_sounds(group: str) -> list[str]:
    folder = SOUNDS_ROOT / group
    pattern = re.compile(rf"^{re.escape(group)}(\d+)\.ogg$")

    found_numbers: set[int] = set()
    for file in folder.glob("*.ogg"):
        match = pattern.match(file.name)
        if match:
            found_numbers.add(int(match.group(1)))

    # Always include the baseline expected count.
    found_numbers.update(range(1, DEFAULT_COUNTS[group] + 1))

    return [f"villager/{group}/{group}{index}" for index in sorted(found_numbers)]


def main() -> None:
    settings = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    volumes = settings["volume"]
    distances = settings["attenuation_distance"]

    sounds_json: dict[str, dict[str, object]] = {}

    for group, event in SOUND_GROUPS.items():
        sounds = [
            {
                "name": sound_name,
                "volume": volumes[group],
                "attenuation_distance": distances[group],
            }
            for sound_name in list_sounds(group)
        ]

        sounds_json[event] = {
            "replace": True,
            "sounds": sounds,
        }

    OUTPUT_PATH.write_text(json.dumps(sounds_json, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

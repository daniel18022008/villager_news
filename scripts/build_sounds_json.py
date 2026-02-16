#!/usr/bin/env python3
"""Generate assets/minecraft/sounds.json for Villager Voices+.

This scans assets/minecraft/sounds/villager_custom/* folders and automatically
includes all matching .ogg files. Add files like idle21.ogg and re-run this
script to include them.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOUNDS_ROOT = ROOT / "assets" / "minecraft" / "sounds" / "villager_custom"
OUTPUT = ROOT / "assets" / "minecraft" / "sounds.json"

# Tunables (resource-pack side)
VOLUME = 0.65
PITCH = 1.0
ATTENUATION_DISTANCE = 8

GROUPS = {
    "yes": r"^yes(\d+)\.ogg$",
    "no": r"^no(\d+)\.ogg$",
    "hit": r"^hit(\d+)\.ogg$",
    "haggle": r"^haggle(\d+)\.ogg$",
    "idle": r"^idle(\d+)\.ogg$",
}


def collect(group: str) -> list[dict]:
    pattern = re.compile(GROUPS[group], re.IGNORECASE)
    folder = SOUNDS_ROOT / group
    found: list[tuple[int, str]] = []

    if folder.exists():
        for path in folder.iterdir():
            if not path.is_file():
                continue
            match = pattern.match(path.name)
            if not match:
                continue
            idx = int(match.group(1))
            found.append((idx, f"villager_custom/{group}/{path.stem}"))

    found.sort(key=lambda t: t[0])
    return [
        {
            "name": name,
            "volume": VOLUME,
            "pitch": PITCH,
            "attenuation_distance": ATTENUATION_DISTANCE,
        }
        for _, name in found
    ]


def main() -> None:
    yes = collect("yes")
    no = collect("no")
    hit = collect("hit")
    haggle = collect("haggle")
    idle = collect("idle")

    data = {
        "entity.villager.yes": {"replace": True, "sounds": yes},
        "entity.villager.no": {"replace": True, "sounds": no},
        "entity.villager.hurt": {"replace": True, "sounds": hit},
        "entity.villager.death": {"replace": True, "sounds": hit},
        "entity.villager.ambient": {"replace": True, "sounds": idle},
        "entity.villager.trade": {"replace": True, "sounds": haggle},
        "entity.villager.celebrate": {"replace": True, "sounds": haggle},
    }

    OUTPUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    print("Detected counts:")
    print(f"  yes={len(yes)}, no={len(no)}, hit={len(hit)}, haggle={len(haggle)}, idle={len(idle)}")


if __name__ == "__main__":
    main()

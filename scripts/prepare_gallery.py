#!/usr/bin/env python3
"""Turn image-generated transparent contact sheets into centered square gallery files.

Run after editing each sheet with an image generation tool to remove its background:
    python3 scripts/prepare_gallery.py /path/to/source-map.json

The JSON maps style names to local transparent PNG sheets. This script only handles
mechanical isolation, centering, and export; it does not generate artwork.
"""

from pathlib import Path
import json
import sys

import numpy as np
from PIL import Image
from scipy import ndimage


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site" / "assets" / "icons"
SIZE = 512
SAFE_FRACTION = 0.36


def export_sheet(name, source):
    image = Image.open(source).convert("RGBA")
    columns, rows = (3, 2) if name == "clover" else (4, 3)
    width, height = image.size
    if abs(width / height - columns / rows) > 0.02:
        raise ValueError(f"{name}: sheet ratio does not match {columns}x{rows} grid")

    alpha = np.asarray(image.getchannel("A"))
    if alpha.min() != 0:
        raise ValueError(f"{name}: source has no genuinely transparent pixels")
    threshold = 228 if name == "clover" else 128
    labels, count = ndimage.label(alpha >= threshold, structure=np.ones((3, 3)))
    objects = ndimage.find_objects(labels)
    cell_width, cell_height = width / columns, height / rows
    members = [[] for _ in range(columns * rows)]
    minimum_area = 10 if name == "concept" else 30

    for label, slices in enumerate(objects, start=1):
        if slices is None:
            continue
        area = np.count_nonzero(labels[slices] == label)
        if area < minimum_area:
            continue
        ys, xs = slices
        center_x = (xs.start + xs.stop) / 2
        center_y = (ys.start + ys.stop) / 2
        column = min(columns - 1, int(center_x / cell_width))
        row = min(rows - 1, int(center_y / cell_height))
        members[row * columns + column].append((label, area))

    folder = OUTPUT / name
    folder.mkdir(parents=True, exist_ok=True)
    for index, components in enumerate(members, start=1):
        if not components:
            raise ValueError(f"{name}: no artwork found for cell {index}")
        largest = max(area for _, area in components)
        kept = [label for label, area in components if area >= max(minimum_area, largest * 0.001)]
        mask = np.isin(labels, kept)
        mask = ndimage.binary_dilation(mask, iterations=2)
        ys, xs = np.where(mask)
        left, top, right, bottom = xs.min(), ys.min(), xs.max() + 1, ys.max() + 1
        crop = image.crop((left, top, right, bottom))
        cropped_alpha = np.asarray(crop.getchannel("A")).copy()
        cropped_alpha[~mask[top:bottom, left:right]] = 0
        crop.putalpha(Image.fromarray(cropped_alpha))
        scale = min((SIZE * SAFE_FRACTION) / crop.width, (SIZE * SAFE_FRACTION) / crop.height)
        resized = crop.resize((round(crop.width * scale), round(crop.height * scale)), Image.Resampling.LANCZOS)
        square = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
        square.alpha_composite(resized, ((SIZE - resized.width) // 2, (SIZE - resized.height) // 2))
        square.save(folder / f"{index:02}.png", optimize=True)


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: prepare_gallery.py source-map.json")
    sources = json.loads(Path(sys.argv[1]).read_text())
    for name, source in sources.items():
        export_sheet(name, source)
        print(f"Prepared {name}")


if __name__ == "__main__":
    main()

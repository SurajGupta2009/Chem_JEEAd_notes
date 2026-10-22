"""Consolidated sheets 1 to 18 for d- and f-Block Elements."""
import sys
from pathlib import Path

content_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(content_dir))

from sheets_part1 import SHEETS_PART1
from sheets_part2 import SHEETS_PART2

SHEETS = SHEETS_PART1 + SHEETS_PART2

if __name__ == "__main__":
    print(f"Total sheets loaded: {len(SHEETS)}")
    for s in SHEETS:
        print(f"  [{s['num']:02d}] {s['title']} ({len(s['boxes'])} boxes, fig={s.get('figure')})")

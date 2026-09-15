#!/usr/bin/env python3
"""Build the Aha release ZIP from tracked source using only Python's standard library."""

from hashlib import sha256
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    skill = root / "skills" / "aha"
    instructions = (skill / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = instructions.split("---", 2)[1]
    match = re.search(
        r'''(?m)^  version:\s*["']?(\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)["']?\s*$''',
        frontmatter,
    )
    if match is None:
        raise SystemExit("Set metadata.version in skills/aha/SKILL.md before packaging.")
    version = match.group(1)
    if (root / "LICENSE").read_bytes() != (skill / "LICENSE").read_bytes():
        raise SystemExit("Root LICENSE and skills/aha/LICENSE must match.")

    output = root / "dist" / f"aha-v{version}.zip"
    output.parent.mkdir(exist_ok=True)
    members = ("LICENSE", "SKILL.md", "agents/openai.yaml")
    contents = {name: (skill / name).read_bytes() for name in members}
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for name, content in contents.items():
            entry = ZipInfo(f"aha/{name}", date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            entry.compress_type = ZIP_DEFLATED
            archive.writestr(entry, content)

    print(output.relative_to(root))
    print(f"SHA-256: {sha256(output.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()

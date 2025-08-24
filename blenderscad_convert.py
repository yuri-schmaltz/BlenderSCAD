#!/usr/bin/env python3
"""Utilities to convert OpenSCAD sources to BlenderSCAD friendly Python."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


def braces_decode(text: str) -> str:
    """Return indentation based Python code from a brace based language."""
    current_depth = 0
    indent_width = 4
    if not text:
        return ""
    lines = text.splitlines()
    acc = []
    for line in [x.strip().replace("++", "+=1") for x in lines]:
        if line.endswith(";"):
            line = line[:-1]
        if line.endswith("{"):
            acc.append(" " * current_depth + line[:-1].strip())
            current_depth += indent_width
        elif line.endswith("}"):
            current_depth -= indent_width
        else:
            acc.append(" " * current_depth + line)
    return "\n".join(acc) + "\n"


def convert_openscad(filename_scad: Path) -> Path:
    """Convert a single ``.scad`` file to a Python script."""
    source = braces_decode(filename_scad.read_text())
    source = re.sub(r"module(.*)\)$", r"def\1):", source, flags=re.MULTILINE)
    target = filename_scad.with_suffix(filename_scad.suffix + ".py")
    target.write_text(source)
    return target


def bulk_convert(start_dir: Path) -> None:
    """Walk ``start_dir`` recursively converting all ``.scad`` files."""
    for scad in start_dir.rglob("*.scad"):
        convert_openscad(scad)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="SCAD file or directory to convert")
    args = parser.parse_args()
    if args.path.is_dir():
        bulk_convert(args.path)
    else:
        convert_openscad(args.path)


if __name__ == "__main__":
    main()

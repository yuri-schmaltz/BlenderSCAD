import sys
import types

sys.modules.setdefault("bpy", types.ModuleType("bpy"))

import blenderscad.math as bmath
import blenderscad.colors as colors


def test_rands_repeatable():
    assert bmath.rands(0, 1, 3, seed_value=42) == bmath.rands(0, 1, 3, seed_value=42)


def test_lookup_exact_match():
    data = [[0, 0], [5, 5], [10, 10]]
    assert bmath.lookup(5, data) == 5


def test_color_constant():
    assert colors.red == (1.0, 0.0, 0.0, 0)

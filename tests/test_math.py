import sys
import types

import pytest

sys.modules.setdefault("bpy", types.ModuleType("bpy"))
import blenderscad.math as bmath  # noqa: E402,I001
import blenderscad.colors as colors  # noqa: E402,I001


def test_rands_repeatable():
    assert bmath.rands(0, 1, 3, seed_value=42) == bmath.rands(0, 1, 3, seed_value=42)


def test_lookup_exact_match():
    data = [[0, 0], [5, 5], [10, 10]]
    assert bmath.lookup(5, data) == 5


def test_color_constant():
    assert colors.red == (1.0, 0.0, 0.0, 0)


def test_inverse_trig_functions():
    assert bmath.acos(1) == 0
    assert bmath.asin(0) == 0
    assert bmath.atan(1) == pytest.approx(45)
    assert bmath.atan2(1, 1) == pytest.approx(45)

# BlenderSCAD

BlenderSCAD bridges the gap between [Blender](https://www.blender.org/) and the parametric approach of [OpenSCAD](https://openscad.org/). It provides a small Python library and optional Blender add-ons that allow OpenSCAD style modeling directly inside Blender.

## Features
- OpenSCAD style primitives and operators (cube, sphere, union, difference, etc.).
- Convenience helpers such as color utilities and math functions implemented in degrees.
- Optional Blender toolbar with quick access buttons for common Boolean operations.

## Installation

1. Clone the repository and install the package in editable mode:
   ```bash
   pip install -e .[dev]
   ```
2. Launch Blender and ensure the `blenderscad` package is on the Python path.
3. Enable the optional toolbar add-on by copying the contents of `addons` into Blender's `scripts/addons` directory.

## Usage
Create a simple object using the library:
```python
from blenderscad.primitives import cube
from blenderscad.core import color
from blenderscad.colors import red

obj = color(red, cube(10))
```
See the [examples](examples) directory for more demonstrations.

## Development

- Source code lives in the `src` directory and follows [PEP 8](https://peps.python.org/pep-0008/) style.
- Format and lint the code using [black](https://black.readthedocs.io/) and [ruff](https://docs.astral.sh/ruff/):
  ```bash
  black .
  ruff .
  ```
- Tests use [pytest](https://pytest.org/). Run them with:
  ```bash
  pytest
  ```

Contributions and pull requests are welcome.

## License

This project is licensed under the terms of the [GPL v2 or later](LICENSE.md).

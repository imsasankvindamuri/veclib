# veclib

**The `pathlib` of vector mathematics.**  
A clean, object-oriented, and Pythonic interface for vector algebra and vector calculus.

---

## Features

- Generic `Vector` class for n-dimensional vector math
- Elegant interface using Python operators (`+`, `-`, `*`, etc.)
- Support for dot product, scaling, projections, angles, distance
- Strict dimension checks with custom exceptions
- Extensible via subclassing (e.g., `Vector2D`, `Vector3D`, etc.)
- Planned: `VectorField` class for defining vector fields via Python functions

---

## Example Usage

```python
from veclib import Vector

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)               # Vector(5.0, 7.0, 9.0)
print(v1 * v2)               # Dot product -> 32.0
print(v1.scale(2))           # Vector(2.0, 4.0, 6.0)
print(v1.unit)               # Unit vector
print(v1.distance_to(v2))    # Euclidean distance
````

---

## Philosophy

`veclib` is inspired by the elegance and minimalism of `pathlib`. Instead of writing low-level
vector operations over and over again, this library lets you express vector math clearly and naturally.

You don’t have to worry about dimensionality errors — those are caught and raised as meaningful exceptions.

---

## Roadmap

* [x] Core `Vector` class with basic operations
* [ ] `Vector2D`, `Vector3D` with dimension-specific methods (e.g. cross product)
* [ ] `VectorField` class (e.g. `gravitational = VectorField(lambda r: (-G * m / r.magnitude_squared ) * r.unit)`)
* [ ] Higher-dimensional operations (wedge product, generalized cross product)

---

## Installation

```bash
pip install veclib
```

(Currently under development — not published yet.)

---

## License

This project is licensed under the **LGPL-2.1** license. See the [LICENSE](./LICENSE) file
for further details.

from collections.abc import Generator, Iterable
import math
from typing import SupportsFloat
from veclib.exceptions.exceptions import DimensionError

class Vector:
    """
    A generic n-dimensional vector supporting basic vector algebra operations.
    """

    def __init__(self, *args: SupportsFloat) -> None:
        """
        Initialize a new n-dimensional vector.
        Raises DimensionError if zero arguments are passed.
        """
        if len(args) == 0:
            raise DimensionError("Cannot have 0D vector.")
        self.__coords: tuple[float, ...] = tuple(float(arg) for arg in args)

    def __repr__(self) -> str:
        """Return the string representation of the vector."""
        return f"Vector{self.__coords}"

    def __iter__(self) -> Generator[float, None, None]:
        """Iterate over vector components."""
        yield from self.__coords

    def __hash__(self) -> int:
        """Return the hash of the vector."""
        return hash(self.__coords)

    def __len__(self) -> int:
        """Return the number of dimensions."""
        return len(self.__coords)

    def __neg__(self) -> 'Vector':
        """Return the negation of the vector."""
        return Vector(*(-arg for arg in self))

    def __abs__(self) -> float:
        """Return the magnitude of the vector."""
        return self.magnitude

    def __eq__(self, value: object, /) -> bool:
        """Return whether two vectors are equal."""
        if isinstance(value, Vector):
            if len(self) != len(value):
                return False
            return all(math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-12) for a, b in zip(self, value))
        return False

    def __add__(self, value: object, /) -> 'Vector':
        """Return the vector sum."""
        if not isinstance(value, Vector):
            return NotImplemented
        if not len(self) == len(value):
            raise DimensionError(f"Cannot add {len(value)}D vector to {len(self)}D vector.")
        return Vector(*(a + b for a, b in zip(self, value)))

    def __sub__(self, value: object, /) -> 'Vector':
        """Return the vector difference."""
        if not isinstance(value, Vector):
            return NotImplemented
        if not len(self) == len(value):
            raise DimensionError(f"Cannot subtract {len(value)}D vector from {len(self)}D vector.")
        return Vector(*(a - b for a, b in zip(self, value)))

    def __mul__(self, value: object, /) -> 'Vector | float':
        """
        Return the dot product or scalar multiplication.
        For another Vector, returns the dot product.
        For a scalar, returns a scaled Vector.
        """
        if isinstance(value, Vector):
            return self.dot(value)
        if isinstance(value, SupportsFloat) and not isinstance(value, bool):
            return self.scale(float(value))
        return NotImplemented

    def __rmul__(self, value: object, /) -> 'Vector | float':
        """Support right-hand side multiplication."""
        return self.__mul__(value)

    def __getitem__(self, value: int, /) -> float:
        """Access the component at the given index."""
        if not 0 <= value < len(self):
            raise IndexError(f"Invalid coordinate '{value}' requested for {len(self)}D vector.")
        return self.__coords[value]

    def dot(self, value: 'Vector') -> float:
        """Return the dot product with another vector."""
        if not len(self) == len(value):
            raise DimensionError(f"Cannot take dot product of {len(self)}D and {len(value)}D vectors.")
        return sum(a * b for a, b in zip(self, value))

    def scale(self, value: float) -> 'Vector':
        """Return a new vector scaled by a scalar."""
        return Vector(*(arg * value for arg in self))

    def as_tuple(self) -> tuple[float, ...]:
        """Return the components as a tuple."""
        return self.__coords

    def component_along(self, value: 'Vector') -> 'Vector':
        """Return the component of this vector along another."""
        scaling = self.dot(value) / value.magnitude_squared
        return value.scale(scaling)

    def distance_to(self, value: 'Vector') -> float:
        """Return the Euclidean distance to another vector."""
        return (self - value).magnitude

    def cos(self, value: 'Vector') -> float:
        """Return the cosine of the angle to another vector."""
        return self.dot(value) / (self.magnitude * value.magnitude)

    def sin(self, value: 'Vector') -> float:
        """Return the sine of the angle to another vector."""
        return math.sqrt(1 - self.cos(value) ** 2)

    def angle_to(self, value: 'Vector') -> float:
        """Return the angle (in radians) to another vector."""
        return math.acos(self.cos(value))

    def is_parallel(self, value: 'Vector') -> bool:
        """Return whether this vector is parallel to another."""
        return math.isclose(self.unit.dot(value.unit), 1, rel_tol=1e-9, abs_tol=1e-12)

    def is_orthogonal(self, value: 'Vector') -> bool:
        """Return whether this vector is orthogonal to another."""
        return math.isclose(self.dot(value), 0, rel_tol=1e-9, abs_tol=1e-12)

    def clone(self) -> 'Vector':
        """Return a copy of the vector."""
        return Vector(*(arg for arg in self))

    @property
    def unit(self) -> 'Vector':
        """Return the unit vector in the same direction."""
        if self.magnitude == 0:
            raise ZeroDivisionError("Normalization for zero vector is undefined.")
        return Vector(*(arg / self.magnitude for arg in self))

    @property
    def magnitude(self) -> float:
        """Return the magnitude (Euclidean norm) of the vector."""
        return math.sqrt(self.magnitude_squared)

    @property
    def magnitude_squared(self) -> float:
        """Return the squared magnitude of the vector."""
        return sum(arg ** 2 for arg in self)

    @classmethod
    def zero(cls, dimensions: int) -> 'Vector':
        """Return a zero vector of given dimensions."""
        return cls(*(0.0 for _ in range(dimensions)))

    @classmethod
    def from_iter(cls, iterable: Iterable[SupportsFloat]) -> 'Vector':
        """Create a vector from any iterable of floats."""
        return cls(*(float(arg) for arg in iterable))

# tests/test_vector.py

import pytest
from veclib.vector.vector import Vector
from veclib.exceptions.exceptions import DimensionError
import math

def test_vector_init():
    v = Vector(1, 2, 3)
    assert v.as_tuple() == (1.0, 2.0, 3.0)

def test_vector_zero_dimension():
    with pytest.raises(DimensionError):
        Vector()

def test_vector_addition():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    assert v1 + v2 == Vector(4, 6)

def test_vector_subtraction():
    v1 = Vector(5, 6)
    v2 = Vector(2, 1)
    assert v1 - v2 == Vector(3, 5)

def test_vector_dot_product():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, -5, 6)
    assert math.isclose(v1.dot(v2), 12)

def test_vector_scaling():
    v = Vector(1, -2, 3)
    scaled = v * 2
    assert scaled == Vector(2, -4, 6)

def test_vector_unit():
    v = Vector(3, 4)
    unit = v.unit
    assert math.isclose(unit.magnitude, 1.0)
    assert unit == Vector(0.6, 0.8)

def test_vector_angle_parallel():
    v1 = Vector(2, 0)
    v2 = Vector(4, 0)
    assert v1.is_parallel(v2)
    assert not v1.is_orthogonal(v2)

def test_vector_angle_orthogonal():
    v1 = Vector(1, 0)
    v2 = Vector(0, 5)
    assert v1.is_orthogonal(v2)
    assert not v1.is_parallel(v2)

def test_vector_clone():
    v = Vector(7, 8)
    clone = v.clone()
    assert clone == v
    assert clone is not v

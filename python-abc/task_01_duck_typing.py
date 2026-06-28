#!/usr/bin/python3
"""Module that defines Shape, Circle, Rectangle, and shape_info."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        raise NotImplementedError


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

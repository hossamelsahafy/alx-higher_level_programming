#!/usr/bin/python
"""Define square class"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Define square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Return size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of square"""
        super().__setattr__("width", value)
        super().__setattr__("height", value)

    def update(self, *args, **kwargs):
        """Update function for square"""
        attr = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for attr, value in zip(attr, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square object"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }

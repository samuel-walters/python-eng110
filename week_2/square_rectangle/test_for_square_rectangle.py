from rectangle_square_classes import Rectangle, Square
import unittest
import pytest

class SquareTests(unittest.TestCase):
    @pytest.fixture
    def example_square(self):
        s = Square(5)
        return s
    def test_width_height(example_square):
        assert example_square.width == 5
        rect = Rectangle(9, 2)
        assert rect.width == 9
        assert rect.height == 2
        square = Square(20)
        assert square.width == 20
        assert square.height == 20
    def test_value_checks(self):
        rect = Rectangle(4, 2)
        assert rect.get_area() == 8
        assert rect.get_perimeter() == 12
        square = Square(4)
        assert square.get_area() == 16
        assert square.get_perimeter() == 16
    def test_check_not_0(self):
        rect = Rectangle(-2, 0)
        square = Square(0)
        self.assertNotEqual(rect.height, 0)
        self.assertNotEqual(square.width, 0)
        square = Square(-5)
        self.assertNotEqual(square.height, -5)
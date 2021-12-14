import unittest
import shapes

class TestShapes(unittest.TestCase):

    def test_shapes_rectangle(self):
        with self.assertRaises(ValueError):
            bad_shape = shapes.Rectangle(-1,2)
        with self.assertRaises(TypeError):
            bad_shape = shapes.Rectangle(1,"a")
        testing_rec = shapes.Rectangle(2,4)
        self.assertEqual(8, testing_rec.area())

    def test_shapes_square(self):
        with self.assertRaises(ValueError):
            bad_shape = shapes.Square(-1)
        with self.assertRaises(TypeError):
            bad_shape = shapes.Square("a")
        testing_sq = shapes.Square(8)
        self.assertEqual(64, testing_sq.area())

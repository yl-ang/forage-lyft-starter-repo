import unittest

from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires_wear_values = [0.5, 0.9, 0.6, 0.7]
        tires = CarriganTires(tires_wear_values)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires_wear_values = [0.5, 0.3, 0.3, 0.4]
        tires = CarriganTires(tires_wear_values)
        self.assertFalse(tires.needs_service())
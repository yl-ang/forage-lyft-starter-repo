import unittest

from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        current_mileage = 30001
        last_mileage = 0
        engine = CapuletEngine(current_mileage, last_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 29999
        last_mileage = 0
        engine = CapuletEngine(current_mileage, last_mileage)
        self.assertFalse(engine.needs_service())
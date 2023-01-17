import unittest
from datetime import date, datetime

from battery.SpindlerBattery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-02")
        last_service_date = date.fromisoformat("2015-10-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

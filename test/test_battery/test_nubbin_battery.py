import unittest
from datetime import date, datetime

from battery.NubbinBattery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-02")
        last_service_date = date.fromisoformat("2015-10-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

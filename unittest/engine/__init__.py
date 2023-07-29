import unittest
from datetime import datetime
from capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_find_difference(self):
        engine = CapuletEngine("2023-01-01", 50000, 30000)
        difference = engine.find_difference()
        self.assertEqual(difference, 20000)

    def test_needs_service_true(self):
        engine = CapuletEngine("2023-01-01", 80000, 50000)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = CapuletEngine("2023-01-01", 50000, 30000)
        self.assertFalse(engine.needs_service())

from sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_should_be_serviced_warning_light_on(self):
        # Test when the warning light is on (True)
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = True

        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertTrue(engine.should_be_serviced())

    def test_should_be_serviced_warning_light_off(self):
        # Test when the warning light is off (False)
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertFalse(engine.should_be_serviced())

from willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_should_be_serviced_true(self):
        # Test when the mileage difference is greater than 60000
        last_service_date = datetime.today().date()
        current_mileage = 100000
        last_service_mileage = 30000

        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.should_be_serviced())

    def test_should_be_serviced_false(self):
        # Test when the mileage difference is less than or equal to 60000
        last_service_date = datetime.today().date()
        current_mileage = 80000
        last_service_mileage = 30000

        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.should_be_serviced())

if __name__ == '__main__':
    unittest.main()

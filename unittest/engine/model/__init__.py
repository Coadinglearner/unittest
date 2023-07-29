import unittest
from datetime import datetime, timedelta
from engine.capulet_engine import CapuletEngine
from engine.model.calliope import Calliope

class TestCalliope(unittest.TestCase):
    def setUp(self):
        # Set up a base CapuletEngine object with common data for testing
        last_service_date = datetime(2022, 1, 15)
        current_mileage = 45000
        last_service_mileage = 15000
        self.calliope_car = Calliope(last_service_date, current_mileage, last_service_mileage)

    def test_needs_service_with_last_service_date_threshold_exceeded(self):
        # Test when the threshold date (2 years after last service) is exceeded
        today = datetime.today().date()
        last_service_date = today - timedelta(days=2*365 + 1)  # Exceed the threshold by one day
        self.calliope_car.last_service_date = last_service_date
        self.assertTrue(self.calliope_car.needs_service())

    def test_needs_service_with_last_service_date_within_threshold(self):
        # Test when the threshold date (2 years after last service) is not exceeded
        today = datetime.today().date()
        last_service_date = today - timedelta(days=2*365 - 1)  # Within the threshold by one day
        self.calliope_car.last_service_date = last_service_date
        self.assertFalse(self.calliope_car.needs_service())

    def test_needs_service_with_engine_should_be_serviced(self):
        # Test when the engine_should_be_serviced() method returns True
        self.calliope_car.current_mileage = 60001  # Exceed the service mileage threshold
        self.assertTrue(self.calliope_car.needs_service())

    def test_needs_service_without_engine_should_be_serviced(self):
        # Test when the engine_should_be_serviced() method returns False
        self.calliope_car.current_mileage = 30000  # Within the service mileage threshold
        self.assertFalse(self.calliope_car.needs_service())

from engine.willoughby_engine import WilloughbyEngine
from engine.model.glissade import Glissade

class TestGlissade(unittest.TestCase):
    def setUp(self):
        # Set up a base WilloughbyEngine object with common data for testing
        last_service_date = datetime(2022, 1, 15)
        current_mileage = 60000
        last_service_mileage = 30000
        self.glissade_car = Glissade(last_service_date, current_mileage, last_service_mileage)

    def test_needs_service_with_last_service_date_threshold_exceeded(self):
        # Test when the threshold date (2 years after last service) is exceeded
        today = datetime.today().date()
        last_service_date = today - timedelta(days=2*365 + 1)  # Exceed the threshold by one day
        self.glissade_car.last_service_date = last_service_date
        self.assertTrue(self.glissade_car.needs_service())

    def test_needs_service_with_last_service_date_within_threshold(self):
        # Test when the threshold date (2 years after last service) is not exceeded
        today = datetime.today().date()
        last_service_date = today - timedelta(days=2*365 - 1)  # Within the threshold by one day
        self.glissade_car.last_service_date = last_service_date
        self.assertFalse(self.glissade_car.needs_service())

    def test_needs_service_with_engine_should_be_serviced(self):
        # Test when the engine_should_be_serviced() method returns True
        self.glissade_car.current_mileage = 90000  # Exceed the service mileage threshold
        self.assertTrue(self.glissade_car.needs_service())

    def test_needs_service_without_engine_should_be_serviced(self):
        # Test when the engine_should_be_serviced() method returns False
        self.glissade_car.current_mileage = 40000  # Within the service mileage threshold
        self.assertFalse(self.glissade_car.needs_service())

from engine.sternman_engine import SternmanEngine
from engine.model.palindrome import Palindrome

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        # Set up a base SternmanEngine object with common data for testing
        last_service_date = datetime(2022, 1, 15)
        warning_light_is_on = True
        self.palindrome_car = Palindrome(last_service_date, warning_light_is_on)

    def test_needs_service_with_last_service_date_threshold_exceeded(self):
        # Test when the threshold date (4 years after last service) is exceeded
        today = datetime.today().date()
        last_service_date = today - timedelta(days=4*365 + 1)  # Exceed the threshold by one day
        self.palindrome_car.last_service_date = last_service_date
        self.assertTrue(self.palindrome_car.needs_service())

    def test_needs_service_with_last_service_date_within_threshold(self):
        # Test when the threshold date (4 years after last service) is not exceeded
        today = datetime.today().date()
        last_service_date = today - timedelta(days=4*365 - 1)  # Within the threshold by one day
        self.palindrome_car.last_service_date = last_service_date
        self.assertFalse(self.palindrome_car.needs_service())

    def test_needs_service_with_engine_should_be_serviced(self):
        # Test when the engine_should_be_serviced() method returns True
        self.palindrome_car.warning_light_is_on = True
        self.assertTrue(self.palindrome_car.needs_service())

    def test_needs_service_without_engine_should_be_serviced(self):
        # Test when the engine_should_be_serviced() method returns False
        self.palindrome_car.warning_light_is_on = False
        self.assertFalse(self.palindrome_car.needs_service())

from engine.willoughby_engine import WilloughbyEngine
from engine.model.rorschach import Rorschach

class TestRorschach(unittest.TestCase):
    def setUp(self):
        # Set up a base WilloughbyEngine object with common data for testing
        last_service_date = datetime(2022, 1, 15)
        current_mileage = 60000
        last_service_mileage = 30000
        self.rorschach_car = Rorschach(last_service_date, current_mileage, last_service_mileage)

    def test_needs_service_with_last_service_date_threshold_exceeded(self):
        # Test when the threshold date (4 years after last service) is exceeded
        today = datetime.today().date()
        last_service_date = today - timedelta(days=4*365 + 1)  # Exceed the threshold by one day
        self.rorschach_car.last_service_date = last_service_date
        self.assertTrue(self.rorschach_car.needs_service())

    def test_needs_service_with_last_service_date_within_threshold(self):
        # Test when the threshold date (4 years after last service) is not exceeded
        today = datetime.today().date()
        last_service_date = today - timedelta(days=4*365 - 1)  # Within the threshold by one day
        self.rorschach_car.last_service_date = last_service_date
        self.assertFalse(self.rorschach_car.needs_service())

    def test_needs_service_with_engine_should_be_serviced(self):
        # Test when the engine_should_be_serviced() method returns True
        self.rorschach_car.current_mileage = 90000  # Exceed the service mileage threshold
        self.assertTrue(self.rorschach_car.needs_service())

    def test_needs_service_without_engine_should_be_serviced(self):
        # Test when the engine_should_be_serviced() method returns False
        self.rorschach_car.current_mileage = 40000  # Within the service mileage threshold
        self.assertFalse(self.rorschach_car.needs_service())

from engine.capulet_engine import CapuletEngine
from engine.model.thovex import Thovex

class TestThovex(unittest.TestCase):
    def setUp(self):
        # Set up a base CapuletEngine object with common data for testing
        last_service_date = datetime(2022, 1, 15)
        current_mileage = 30000
        last_service_mileage = 0
        self.thovex_car = Thovex(last_service_date, current_mileage, last_service_mileage)

    def test_needs_service_with_last_service_date_threshold_exceeded(self):
        # Test when the threshold date (4 years after last service) is exceeded
        today = datetime.today().date()
        last_service_date = today - timedelta(days=4*365 + 1)  # Exceed the threshold by one day
        self.thovex_car.last_service_date = last_service_date
        self.assertTrue(self.thovex_car.needs_service())

    def test_needs_service_with_last_service_date_within_threshold(self):
        # Test when the threshold date (4 years after last service) is not exceeded
        today = datetime.today().date()
        last_service_date = today - timedelta(days=4*365 - 1)  # Within the threshold by one day
        self.thovex_car.last_service_date = last_service_date
        self.assertFalse(self.thovex_car.needs_service())

    def test_needs_service_with_engine_should_be_serviced(self):
        # Test when the engine_should_be_serviced() method returns True
        self.thovex_car.current_mileage = 60001  # Exceed the service mileage threshold
        self.assertTrue(self.thovex_car.needs_service())

    def test_needs_service_without_engine_should_be_serviced(self):
        # Test when the engine_should_be_serviced() method returns False
        self.thovex_car.current_mileage = 30000  # Within the service mileage threshold
        self.assertFalse(self.thovex_car.needs_service())

if __name__ == '__main__':
    unittest.main()


from abc import ABC, abstractmethod
from car import Car

class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date: str, current_mileage: int, last_service_mileage: int):
        """
        Initialize the CapuletEngine.
        :param last_service_date: Last service date as a string.
        :param current_mileage: Current mileage of the engine as an integer.
        :param last_service_mileage: Mileage of the engine at the time of the last service as an integer.
        """
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def find_difference(self):
        """
        Find the difference by subtracting last_service_mileage from current_mileage.
        :return: The difference in mileage as an integer.
        """
        difference = self.current_mileage - self.last_service_mileage
        return difference

    def should_be_serviced(self):
        """
        Check if the engine should be serviced based on the mileage difference.
        :return: True if the difference is greater than 30000, False otherwise.
        """
        difference = self.find_difference()
        return difference > 30000

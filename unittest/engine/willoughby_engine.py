from abc import ABC , abstractmethod

from car import Car


class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        """
              Initialize the WilloughbyEngine.
              :param last_service_date: Last service date as a string.
              :param current_mileage: Current mileage of the engine as an integer.
              :param last_service_mileage: Mileage of the engine at the time of the last service as an integer.
              """
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage


    def should_be_serviced(self):
         """
            Check if the engine should be serviced based on the mileage.
            :return: True if the engine should be serviced, False otherwise.
            """
        return self.current_mileage - self.last_service_mileage>60000

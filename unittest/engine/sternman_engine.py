from abc import ABC , abstractmethod

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date:str, warning_light_is_on:bool):
        """
        assining value to warning_light_is_on using self
        """

        """
               Initialize the SternmanEngine.
               :param last_service_date: Last service date as a string.
               :param warning_light_is_on: Whether the warning light is on (True or False).
               """
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    @abstractmethod
    def should_be_serviced(self):
        if self.warning_light_is_on:
            """occured when the warning_light_is_on is logic 1"""
            return True
        else:
            return False

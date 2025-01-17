from model.car import Car
from battery.nubbin_battery import NubbinBattery
from battery.splindler_battery import SplindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory:
    def create_calliope(
        last_service_date, current_mileage: int, last_service_mileage: int, sensors
    ):

        return Car(
            engine=CapuletEngine(current_mileage, last_service_mileage),
            battery=SplindlerBattery(last_service_date),
            sensors=CarriganTire(sensors),
        )

    def create_glissade(
        last_service_date, current_mileage: int, last_service_mileage: int, sensors
    ):
        return Car(
            engine=WilloughbyEngine(current_mileage, last_service_mileage),
            battery=SplindlerBattery(last_service_date),
            sensors=CarriganTire(sensors),
        )

    def create_palindrome(last_service_date, warning_light_on: bool, sensors):
        return Car(
            engine=SternmanEngine(warning_light_is_on),
            battery=SplindlerBattery(last_service_date),
            sensors=CarriganTire(sensors),
        )

    def create_rorschach(
        last_service_date, current_mileage: int, last_service_mileage: int, sensors
    ):
        return Car(
            engine=WilloughbyEngine(current_mileage, last_service_mileage),
            battery=NubbinBattery(last_service_date),
            sensors=OctoprimeTire(sensors),
        )

    def create_thovex(
        last_service_date, current_mileage: int, last_service_mileage: int, sensors
    ):
        return Car(
            engine=CapuletEngine(current_mileage, last_service_mileage),
            battery=NubbinBattery(last_service_date),
            sensors=OctoprimeTire(sensors),
        )

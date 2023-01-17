from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from car import Car
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_values):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tires_wear_values)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_values):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tires_wear_values)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tires_wear_values):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTires(tires_wear_values)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_values):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tires_wear_values)
        car = Car(engine, battery, tires)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires_wear_values):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tires_wear_values)
        car = Car(engine, battery, tires)
        return car
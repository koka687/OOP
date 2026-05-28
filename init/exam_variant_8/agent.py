import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv

from google.adk import Agent

load_dotenv()

class Transport(ABC):
    def __init__(self, route_number: str, departure: str):
        self.route_number = route_number
        self.departure = departure

    @abstractmethod
    def get_schedule(self) -> dict:
        pass

class Bus(Transport):
    def __init__(self, route_number: str, departure: str, stops: list[str]):
        super().__init__(route_number, departure)
        self.stops = stops

    def get_schedule(self) -> dict:
        return {
            "type": "Bus",
            "route_number": self.route_number,
            "departure": self.departure,
            "stops": self.stops
        }

class Train(Transport):
    def __init__(self, route_number: str, departure: str, stations: list[str], travel_time_min: int):
        super().__init__(route_number, departure)
        self.stations = stations
        self.travel_time_min = travel_time_min

    def get_schedule(self) -> dict:
        return {
            "type": "Train",
            "route_number": self.route_number,
            "departure": self.departure,
            "stations": self.stations,
            "travel_time_min": self.travel_time_min
        }

class Schedule:
    def __init__(self):
        self.__routes: dict[str, Transport] = {}

    def add_route(self, transport: Transport):
        self.__routes[transport.route_number] = transport

    def find_route(self, route_number: str) -> Transport | None:
        return self.__routes.get(route_number)

    def list_routes(self) -> list[dict]:
        return [transport.get_schedule() for transport in self.__routes.values()]

def get_transport_schedule(route_number: str) -> dict:
    """Отримує розклад для заданого номера маршруту (маршрутки або потяга)."""
    schedule = Schedule()
    
    bus_1 = Bus(route_number="45", departure="08:00", stops=["Центр", "Аквапарк", "ТЦ Вікторія"])
    train_1 = Train(route_number="705", departure="14:30", stations=["Київ", "Вінниця", "Львів"], travel_time_min=300)
    
    schedule.add_route(bus_1)
    schedule.add_route(train_1)
    
    found_route = schedule.find_route(route_number)
    if found_route:
        return found_route.get_schedule()
    
    return {"found": False, "message": f"Маршрут {route_number} не знайдено."}

root_agent = Agent(
    name="transport_assistant",
    instruction=(
        "Ти помічник з громадського транспорту. Надаєш інформацію про маршрути, "
        "зупинки та час у дорозі. Коли тебе питають про маршрут, використовуй "
        "інструмент get_transport_schedule. Відповідай ввічливо українською мовою."
    ),
    tools=[get_transport_schedule]
)
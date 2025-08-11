import os
import json
from typing import List
from dataclasses import dataclass, asdict
from semantic_kernel.functions.kernel_function_decorator import kernel_function

@dataclass
class FlightModel:
    Id: int
    Airline: str
    Destination: str
    DepartureDate: str
    Price: float
    IsBooked: bool = False


class FlightBookingPlugin:
    FILE_PATH = "flights.json"

    def __init__(self):
        self.flights: List[FlightModel] = self.load_flights_from_file()


    # Create a plugin function with kernel function attributes


    # Create a kernel function to book flights



    def save_flights_to_file(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([asdict(flight) for flight in self.flights], f, indent=4)

    def load_flights_from_file(self) -> List[FlightModel]:
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [FlightModel(**item) for item in data]

        raise FileNotFoundError(f"The file '{self.FILE_PATH}' was not found. Please provide a valid flights.json file.")

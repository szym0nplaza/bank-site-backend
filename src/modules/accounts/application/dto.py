from dataclasses import dataclass
from datetime import date


@dataclass
class UserDTO:
    id: int
    name: str
    surname: str
    date_of_birth: date
    email: str
    login: str

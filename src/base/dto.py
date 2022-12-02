from dataclasses import dataclass


@dataclass
class ResponseDTO:
    message: str
    status: int
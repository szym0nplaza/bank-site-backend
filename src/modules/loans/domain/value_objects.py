import enum


class LoanStatus(enum.Enum):
    ACTIVE = "active"
    COMPLETED = "completed"
    POSTPONED = "postponed"

    def __str__(self):
        return str(self.value)
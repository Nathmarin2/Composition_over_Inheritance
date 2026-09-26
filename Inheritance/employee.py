from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Employee(ABC):

    name: str
    id: int

    @abstractmethod
    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""

        
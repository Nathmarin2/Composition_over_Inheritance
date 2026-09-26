from dataclasses import dataclass
from Contract import Contract


@dataclass
class SalariedContract(Contract):

    monthly_salary: float
    percentage: float = 1

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage
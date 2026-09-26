from dataclasses import dataclass
from hourlyEmployee import HourlyEmployee

@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed
from dataclasses import dataclass
from employee import Employee

@dataclass
class Freelancer(Employee):

    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked
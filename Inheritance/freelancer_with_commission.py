from dataclasses import dataclass
from freelancer import Freelancer

@dataclass
class FreelancerWithCommission(Freelancer):

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed
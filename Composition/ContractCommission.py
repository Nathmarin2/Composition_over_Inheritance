from dataclasses import dataclass
from Commission import Commission


@dataclass
class ContractCommission(Commission):
    
    commission: float = 100
    contracts_landed: int = 0

    def get_payment(self) -> float:
        """Returns the commission to be paid out."""
        return self.commission * self.contracts_landed
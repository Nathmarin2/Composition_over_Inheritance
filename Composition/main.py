from Employee import Employee
from HourlyContract import HourlyContract
from SalariedContract import SalariedContract
from FreelancerContract import FreelancerContract
from ContractCommission import ContractCommission


def main() -> None:

    pepe_contract = HourlyContract(pay_rate=50, hours_worked=100)
    pepe = Employee(
        name="Pepe",
        id=12346,
        contract=pepe_contract
    )

    print(
        f"{pepe.name} worked for {pepe_contract.hours_worked} hours "
        f"and earned ${pepe.compute_pay()}."
    )

    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)

    sarah = Employee(
        name="Sarah",
        id=47832,
        contract=sarah_contract,
        commission=sarah_commission
    )

    print(
        f"{sarah.name} landed {sarah_commission.contracts_landed} contracts "
        f"and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()
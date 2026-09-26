from hourlyEmployee import HourlyEmployee
from salariedEmployee import SalariedEmployee
from salariedEmployee_with_commission import SalariedEmployeeWithCommission
from freelancer import Freelancer




def main() -> None:

    maria = SalariedEmployee(name="Maria", id=738612, monthly_salary=5000)
    print(
        f"{maria.name} worked for a month and earned ${maria.compute_pay()}."
    )

    pepe = Freelancer(name="Pepe", id=738615, pay_rate=100, hours_worked=20)
    print(
        f"{pepe.name} worked for a month and earned ${pepe.compute_pay()}."
    )

    sarah = SalariedEmployeeWithCommission(
        name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()
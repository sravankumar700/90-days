# Simple company database using string data types

company_db = {
    "Alice Johnson": "75000",
    "Bob Smith": "62000",
    "Carol Lee": "88000"
}


def display_database():
    print("Company Employee Database")
    print("-------------------------")
    for employee, salary in company_db.items():
        print(f"Employee: {employee}, Salary: ${salary}")
    print()


def add_employee(name, salary):
    company_db[name] = salary
    print(f"Added employee: {name} with salary ${salary}")


def update_salary(name, salary):
    if name in company_db:
        company_db[name] = salary
        print(f"Updated {name}'s salary to ${salary}")
    else:
        print(f"Employee {name} not found.")


def get_salary(name):
    salary = company_db.get(name)
    if salary:
        print(f"{name} earns ${salary}")
    else:
        print(f"Employee {name} not found.")


if __name__ == "__main__":
    display_database()
    add_employee("Dana White", "97000")
    update_salary("Bob Smith", "65000")
    get_salary("Carol Lee")
    print()
    display_database()
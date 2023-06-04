def initialize_employee():
    name = input()
    gender = input()
    salary = float(input())
    employee = {
        "name": name,
        "gender": gender,
        "salary": salary
    }
    return employee

print(initialize_employee())

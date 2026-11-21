
import sys

def employee_info(name, emp_id, department, salary):
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )

if __name__ == "__main__":
    name = sys.argv[1]
    emp_id = sys.argv[2]
    department = sys.argv[3]
    salary = sys.argv[4]

    print("Employee Details")
    print("--------------------")
    print(employee_info(name, emp_id, department, salary))

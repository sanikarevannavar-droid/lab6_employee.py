from employee import employee_info

def test_employee_details():
    result = employee_info("Krishna", "Emp200", "IT", 20000)

    expected = (
        "Employee Name: Krishna\n"
        "Employee ID: Emp200\n"
        "Department: IT\n"
        "Salary: 20000"
    )

    assert result == expected
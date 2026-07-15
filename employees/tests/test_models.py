from django.test import TestCase
from django.contrib.auth.models import User
from employees.models import (
    Employee,
    Department,
    Position,
    Status,
)


class StatusModelTest(TestCase):

    def test_create_status(self):
        status = Status.objects.create(
            name="Normal"
        )

        self.assertEqual(status.name, "Normal")

    def test_status_str(self):
        status = Status.objects.create(
            name="Resigned"
        )

        self.assertEqual(str(status), "Resigned")


class PositionModelTest(TestCase):

    def test_create_position(self):
        position = Position.objects.create(
            name="Backend Developer",
            salary=50000
        )

        self.assertEqual(position.name, "Backend Developer")
        self.assertEqual(position.salary, 50000)

    def test_position_str(self):
        position = Position.objects.create(
            name="QA Engineer",
            salary=40000
        )

        self.assertEqual(str(position), "QA Engineer")


class DepartmentModelTest(TestCase):

    def test_create_department(self):
        department = Department.objects.create(
            name="IT"
        )

        self.assertEqual(department.name, "IT")

    def test_department_str(self):
        department = Department.objects.create(
            name="HR"
        )

        self.assertEqual(str(department), "HR")


class EmployeeModelTest(TestCase):

    def setUp(self):
        self.status = Status.objects.create(
            name="Normal"
        )

        self.position = Position.objects.create(
            name="Backend Developer",
            salary=50000
        )

        self.department = Department.objects.create(
            name="IT"
        )

    def test_create_employee(self):
        employee = Employee.objects.create(
            name="John Doe",
            address="Bangkok",
            manager=True,
            status=self.status,
            position=self.position,
            department=self.department,
        )

        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.address, "Bangkok")
        self.assertTrue(employee.manager)
        self.assertEqual(employee.status.name, "Normal")
        self.assertEqual(employee.position.name, "Backend Developer")
        self.assertEqual(employee.department.name, "IT")

    def test_employee_str(self):
        employee = Employee.objects.create(
            name="Alice",
            address="Bangkok",
            manager=False,
            status=self.status,
            position=self.position,
            department=self.department,
        )

        self.assertEqual(str(employee), "Alice")
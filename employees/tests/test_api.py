from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from employees.models import (
    Employee,
    Department,
    Position,
    Status,
)


class EmployeeAPITest(APITestCase):

    def setUp(self):
        
        self.user = User.objects.create_user(
            username="admin",
            password="1234"
        )

        self.client.force_authenticate(
            user=self.user
        )

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

        self.employee = Employee.objects.create(
            name="John Doe",
            address="Bangkok",
            manager=True,
            status=self.status,
            position=self.position,
            department=self.department,
        )

        self.list_url = reverse("employee-list")
        self.detail_url = reverse(
            "employee-detail",
            args=[self.employee.id]
        )

    def test_create_employee(self):

        data = {
            "name": "Alice",
            "address": "Chiang Mai",
            "manager": False,
            "status": self.status.id,
            "position": self.position.id,
            "department": self.department.id,
        }

        response = self.client.post(
            self.list_url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Employee.objects.count(),
            2
        )

    def test_get_employee_list(self):

        response = self.client.get(self.list_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_employee_detail(self):

        response = self.client.get(self.detail_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["name"],
            "John Doe"
        )

    def test_update_employee(self):

        response = self.client.patch(
            self.detail_url,
            {
                "name": "John Smith"
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.employee.refresh_from_db()

        self.assertEqual(
            self.employee.name,
            "John Smith"
        )

    def test_delete_employee(self):

        response = self.client.delete(
            self.detail_url
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Employee.objects.count(),
            0
        )
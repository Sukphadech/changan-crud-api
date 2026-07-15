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


class EmployeeSearchTest(APITestCase):

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

        Employee.objects.create(
            name="John Doe",
            address="Bangkok",
            manager=True,
            status=self.status,
            position=self.position,
            department=self.department,
        )

        Employee.objects.create(
            name="Alice Smith",
            address="Chiang Mai",
            manager=False,
            status=self.status,
            position=self.position,
            department=self.department,
        )

        self.url = reverse("employee-list")

    def test_search_by_name(self):

        response = self.client.get(
            self.url,
            {"search": "John"}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["count"],
            1
        )

        self.assertEqual(
            response.data["results"][0]["name"],
            "John Doe"
        )

    def test_search_by_address(self):

        response = self.client.get(
            self.url,
            {"search": "Chiang"}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["count"],
            1
        )

        self.assertEqual(
            response.data["results"][0]["name"],
            "Alice Smith"
        )
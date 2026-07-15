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


class EmployeeFilterTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            password="1234"
        )

        self.client.force_authenticate(
            user=self.user
        )

        self.status = Status.objects.create(name="Normal")
        self.status2 = Status.objects.create(name="Resigned")

        self.position = Position.objects.create(
            name="Backend Developer",
            salary=50000,
        )

        self.position2 = Position.objects.create(
            name="QA Engineer",
            salary=40000,
        )

        self.department = Department.objects.create(
            name="IT"
        )

        self.department2 = Department.objects.create(
            name="HR"
        )

        Employee.objects.create(
            name="John",
            address="Bangkok",
            manager=True,
            status=self.status,
            position=self.position,
            department=self.department,
        )

        Employee.objects.create(
            name="Alice",
            address="Chiang Mai",
            manager=False,
            status=self.status2,
            position=self.position2,
            department=self.department2,
        )

        self.url = reverse("employee-list")

    def test_filter_by_department(self):

        response = self.client.get(
            self.url,
            {"department": self.department.id}
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
            "John"
        )

    def test_filter_by_position(self):

        response = self.client.get(
            self.url,
            {"position": self.position2.id}
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
            "Alice"
        )

    def test_filter_by_status(self):

        response = self.client.get(
            self.url,
            {"status": self.status.id}
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
            "John"
        )
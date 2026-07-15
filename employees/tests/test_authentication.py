from django.contrib.auth.models import User
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


class EmployeeAuthenticationTest(APITestCase):

    def setUp(self):
        

        self.user = User.objects.create_user(
            username="admin",
            password="Admin123!"
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

        self.url = reverse("employee-list")

    def test_authenticated_user_can_access_api(self):

        self.client.login(
            username="admin",
            password="Admin123!"
        )

        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_unauthenticated_user_cannot_access_api(self):

        response = self.client.get(self.url)

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ]
        )
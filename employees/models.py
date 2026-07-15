from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(
        "Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_departments",
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    manager = models.BooleanField(default=False)

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    position = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="employees",
    )

    image = models.ImageField(
        upload_to="employees/",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
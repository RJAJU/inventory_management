from django.db import models


class Inventory(models.Model):
    """
    This model will maintain the inventory related data

    `title`
        Inventory title or short description

    `description`
        Inventory description

    `remaining_count`
        Maintaining count to hide/show book and cancel features on ui

    `expiration_date`
        Inventory expiry time
    """
    title = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField()
    remaining_count = models.IntegerField(default=0)
    expiration_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Inventory"


class Member(models.Model):
    """
    This model is used to store members related data

    `name`
        First name of the member

    `surname`
        Last name of the member

    `booking_count`
        Maintaining count related to each member

    `date_joined`
        Date of joining as member
    """
    name = models.CharField(null=False, blank=False, max_length=120)
    surname = models.CharField(max_length=120)
    booking_count = models.IntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

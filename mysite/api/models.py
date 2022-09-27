from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.TextField()
    desc = models.TextField()
    uid = models.CharField(max_length=11)
    quantity = models.IntegerField()

    def __str__(self):
        return self.uid


class Role(models.Model):
    name = models.TextField()
    desc = models.TextField()
    uid = models.CharField(max_length=11)

    def __str__(self):
        return self.uid


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    uid = models.CharField(max_length=11)
    birth_date = models.DateField()
    address = models.CharField(max_length=30)
    contact = models.TextField()
    role = models.TextField()

    def __str__(self):
        return self.uid


class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    uid = models.CharField(max_length=11)
    birth_date = models.DateField()
    address = models.CharField(max_length=30)
    contact = models.TextField()

    def __str__(self):
        return self.uid

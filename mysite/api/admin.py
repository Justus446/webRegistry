from django.contrib import admin
from .models import Patient, Item, Person, Role

# Register your models here.
admin.site.register(Person)
admin.site.register(Item)
admin.site.register(Role)
admin.site.register(Patient)

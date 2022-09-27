from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetup(APITestCase):
    def setUp(self):
        self.patients_url = reverse('patients')
        self.persons_url = reverse('persons')
        self.items_url = reverse('items')

        self.submit_data = {
            'name': "name",
            'desc': "desc"
                }

    def tearDown(self):
        return super().tearDown()

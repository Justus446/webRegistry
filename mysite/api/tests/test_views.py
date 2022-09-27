from .test_setup import TestSetup


class TestView(TestSetup):
    def test_submit_empty_data(self):
        res = self.client.post(self.items_url)
        self.assertEqual(res.status_code, 400)

    def test_submit_populated_data(self):
        res = self.client.post(self.items_url, self.submit_data, fromat="json")
        self.assertEqual(res.data['name'], self.submit_data['name'])
        self.assertEqual(res.data['desc'], self.submit_data['desc'])
        self.assertEqual(res.status_code, 201)

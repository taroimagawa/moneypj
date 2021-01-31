from django.test import TestCase, Client

class MoneyTestCase(TestCase):
    def setUp(self):
        self.c = Client()

    def test_list_access(self):
        res = self.c.get('/')
        self.assertEqual(200, res.status_code)

    def test_admin_access(self):
        res = self.c.get('/admin/')
        self.assertEqual(302, res.status_code)

    def test_create_access(self):
        res = self.c.get('/create/')
        self.assertEqual(200, res.status_code)

    def test_unknown_access(self):
        res = self.c.get('/unknown/')
        self.assertEqual(404, res.status_code)


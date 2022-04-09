from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from authentication.models import User


class HomePageTestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='toto',password='toto123.')
        
    def test_basket_accessible_by_name(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)

    def test_success_accessible_by_name(self):
        response = self.client.get(reverse('success'))
        self.assertEqual(response.status_code, 200)

    def test_cancel_accessible_by_name(self):
        response = self.client.get(reverse('cancel'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_url_exists_at_desired_location(self):
        response = self.client.get('/payment/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_dashboard_view_url_exists_at_desired_location(self):
        response = self.client.get('/payment/success/')
        self.assertEqual(response.status_code, 200)

    def test_wishlist_view_url_exists_at_desired_location(self):
        response = self.client.get('/payment/cancel/')
        self.assertEqual(response.status_code, 200)

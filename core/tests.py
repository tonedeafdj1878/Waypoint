from django.test import TestCase, Client
from django.urls import reverse
from .models import Trail

class TrailModelTest(TestCase):
    def test_trail_str(self):
        trail = Trail.objects.create(
            name="Test Trail",
            distance_km=5.0,
            elevation_gain_m=200,
            difficulty="Easy"
        )
        self.assertEqual(str(trail), "Test Trail (Easy)")

class TrailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.report_url = reverse('report_trail')

    def test_home_view_status(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')

    def test_report_view_post(self):
        response = self.client.post(self.report_url, {
            'trail_name': 'New Adventure Trail',
            'distance_km': 10.5,
            'elevation_gain_m': 450,
            'difficulty': 'Moderate',
            'notes': 'Great views!'
        })
        # Check that it redirects or renders success page
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Trail.objects.filter(name='New Adventure Trail').exists())
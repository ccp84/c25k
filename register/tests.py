from django.test import TestCase
from .models import Run, User
from django.contrib.auth.models import Group


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_get_run_list(self):
        response = self.client.get('/run/list')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'run_list.html')

    def test_get_user_profile(self):
        User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_get_user_list(self):
        User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        response = self.client.get('/user/list')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_list.html')

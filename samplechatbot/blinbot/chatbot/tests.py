from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class ChatbotTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_chat_response(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('get_response'), {'message': 'Hello'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())

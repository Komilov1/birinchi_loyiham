from django.test import TestCase
from .models import Post
from django.urls import reverse
from .views import HomePageView

# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu', text='Yangiliklar')


    def test_Post(self):
        post = Post.objects.get(id=1)
        expected_title = 'Mavzu'
        expected_text = 'Yangiliklar'
        self.assertEqual(expected_title, 'Mavzu')
        self.assertEqual(expected_text, 'Yangiliklar')

class HomePageTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Mavzy2", text="Yangiliklar2")

    def test_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'home.html')

from django.test import TestCase
from .views import all_magazines
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from .models import Magazine
from accounts.models import User

# Create your tests here.

class MagazinesPageTest(TestCase):
    def setUp(self):
        super(MagazinesPageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('letmein')
        self.user.save()
        self.login = self.client.login(username='testuser',
                                       password='letmein')
        self.assertEqual(self.login, True)

    def test_magazines_page_resolves(self):
        magazines_page = resolve('/magazines/')
        self.assertEqual(magazines_page.func, all_magazines)

    def test_magazines_page_status_code_is_ok(self):
        magazines_page = self.client.get('/magazines/')
        self.assertEqual(magazines_page.status_code, 200)

    def test_check_content_is_correct(self):
        magazines_page = self.client.get('/magazines/')
        self.assertTemplateUsed(magazines_page, "magazines/magazines.html")
        magazines_page_template_output = render_to_response("magazines/magazines.html", {"magazines": Magazine.objects.all(), 'user':self.user}).content
        self.assertEqual(magazines_page.content, magazines_page_template_output)


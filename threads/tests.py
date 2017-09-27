from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Subject
from django.core.urlresolvers import resolve
from .views import forum

class SubjectPageTest(TestCase):
    def test_subject_page_resolves(self):
        subject_page = resolve('/forum/')
        self.assertEqual(subject_page.func, forum)

    def test_subject_page_status_code_is_ok(self):
        subject_page = self.client.get('/forum/')
        self.assertEqual(subject_page.status_code, 200)

    def test_check_content_is_correct(self):
        subject_page = self.client.get('/forum/')
        self.assertTemplateUsed(subject_page, "forum/forum.html")
        subject_page_template_output = render_to_response("forum/forum.html",
                                                          {'subjects':
                                                               Subject.objects.all()}).content
        self.assertEqual(subject_page.content, subject_page_template_output)


from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class QuestionIndexView(TestCase):
    def test_no_questions(self):
        '''if no question exist, an appropiate message is displayed'''
        response= self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No existen encuestas")
        self.assertQuerysetEqual(response.context["lastest_question_list"], [])
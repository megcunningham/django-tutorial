import datetime

from django.test import timezone
from django.test import TestCase

from .models import Question



class QuestionMethodTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.test_was_published_recently(), False)




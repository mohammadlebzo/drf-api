from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Game


# Create your tests here.
class GameTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test', password='test1234')
        test_user.save()
        test_game = Game.objects.create(name="api_test", purchaser=test_user, desc="api_test")
        test_game.save()

    def test_thing_model(self):
        game = Game.objects.get(pk=1)
        self.assertEqual(str(game.purchaser), 'test')
        self.assertEqual(str(game.name), 'api_test')
        self.assertEqual(str(game.desc), 'api_test')

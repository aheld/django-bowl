from django.test import TestCase

from score.models import Game

class BowlingTest(TestCase):
    def setUp(self):
        self.game = Game()

    def roll_many(self,pins,rolls=20):
        for i in range(rolls):
            self.game.roll(pins)

    def test_gutter_game(self):
        self.roll_many(0)
        self.roll_many(1)
        self.assertEqual(self.game.score(), 0)

    def test_simple_game(self):
        self.roll_many(1)
        self.assertEqual(self.game.score(), 20)

    def test_sum_game(self):
        self.roll_many(3, rolls=10)
        self.roll_many(4, rolls=10)
        self.assertEqual(self.game.score(), 70)

    def test_spare_game(self):
        self.roll_many(5, rolls=3)
        self.roll_many(0, rolls=17)
        self.assertEqual(self.game.score(), 20)

    def test_spare_2_game(self):
        self.roll_many(5, rolls=3)
        self.roll_many(0, rolls=1)
        self.roll_many(5, rolls=3)
        self.roll_many(0, rolls=13)
        self.assertEqual(self.game.score(), 40)

    def test_strike_game(self):
        self.roll_many(10, rolls=1)
        self.roll_many(3, rolls=2)
        self.roll_many(0, rolls=16)
        self.assertEqual(self.game.score(),22)

    def test_strike_2_game(self):
        self.roll_many(3, rolls=2)
        self.roll_many(10, rolls=1)
        self.roll_many(3, rolls=2)
        self.roll_many(0, rolls=16)
        self.assertEqual(self.game.score(),28)

    def test_strike_spare_game(self):
        self.roll_many(3, rolls=2)
        self.roll_many(10, rolls=1)
        self.roll_many(3, rolls=2)
        self.roll_many(5, rolls=2)
        self.roll_many(3, rolls=2)
        self.roll_many(0, rolls=10)
        self.assertEqual(self.game.score(),47)

    def test_mikey_test(self):
        self.roll_many(10,rolls=12)
        self.assertEqual(self.game.score(),300)

    def test_from_wiki(self):
        for x in [3,4,6,4,7,1,4,5,10,4,6,10,10,10,5,5,3]:
            self.game.roll(x) 
        self.assertEqual(self.game.score(),169)

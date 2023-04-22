import unittest

from card import Card
from game import Game
from hand import Hand

class TestParsing(unittest.TestCase):
  def test_input_len_assertion(self):
    with self.assertRaises(AssertionError):
      Game("2H 3D 5S 9C KD 2C 4S 8C AH")

  def test_card_value_validity(self):
    with self.assertRaisesRegex(ValueError, "invalid card value"):
      Card("0H")

  def test_card_type_validity(self):
    with self.assertRaisesRegex(ValueError, "invalid card type"):
      Card("2R")

  def test_has_to_classic_list_values(self):
    g = Game("2H 3D 5S 9C KD 2C 3H 4S 8C AH")
    self.assertEqual(
      g.p2.as_classic_numeric,
      [2, 3, 4, 8, 14]
    )

  def test_has_to_suite_list_values(self):
    g = Game("2H 3D 5S 9C KD 2C 3H 4S 8C AH")
    self.assertEqual(
      g.p2.as_suite_numeric,
      [1, 2, 3, 4, 8]
    )

class TestHandCombos(unittest.TestCase):
  def test_has_simple_suite(self):
    hand = Hand(["2S", "3S", "6S", "5H", "4S"])
    self.assertTrue(hand.has_suite())

  def test_has_suite_with_as(self):
    hand = Hand(["2S", "3S", "4S", "5H", "AS"])
    self.assertTrue(hand.has_suite())

  def test_has_not_suite(self):
    hand = Hand(["2S", "9S", "4S", "5H", "AS"])
    self.assertFalse(hand.has_suite())

  def test_has_color(self):
    hand = Hand(["2S", "3H", "5S", "9H", "KS"])
    self.assertTrue(hand.has_color())

  def test_has_not_color(self):
    hand = Hand(["2H", "3D", "5S", "9C", "KD"])
    self.assertFalse(hand.has_color())

  def test_has_flush(self):
    hand = Hand(["2S", "3S", "5S", "6H", "4S"])
    self.assertTrue(hand.has_flush())

  def test_has_not_flush(self):
    hand = Hand(["2D", "3S", "5S", "8H", "4S"])
    self.assertFalse(hand.has_flush())

  def test_has_square(self):
    hand = Hand(["5D", "5S", "5C", "6H", "5D"])
    self.assertTrue(hand.has_square())

  def test_has_not_square(self):
    hand = Hand(["2D", "3S", "5C", "8C", "4S"])
    self.assertFalse(hand.has_square())

  def test_has_pair(self):
    hand = Hand(["3D", "8S", "2C", "9H", "3D"])
    self.assertTrue(hand.has_same_card(2))

  def test_has_not_pair(self):
    hand = Hand(["AD", "8S", "2C", "9H", "3D"])
    self.assertFalse(hand.has_same_card(2))

  def test_has_brelan(self):
    hand = Hand(["3D", "3S", "2C", "9H", "3D"])
    self.assertTrue(hand.has_same_card(2))

  def test_has_not_brelan(self):
    hand = Hand(["AD", "8S", "2C", "9H", "3D"])
    self.assertFalse(hand.has_same_card(2))

  def test_has_double_pair(self):
    hand = Hand(["AD", "AS", "2C", "9H", "9D"])
    self.assertTrue(hand.has_double_pair())

  def test_has_not_double_pair(self):
    hand = Hand(["4D", "AS", "2C", "9H", "9D"])
    self.assertFalse(hand.has_double_pair())

  def test_has_full(self):
    hand = Hand(["AD", "AS", "2C", "2H", "2D"])
    self.assertTrue(hand.has_full())

  def test_has_not_full(self):
    hand = Hand(["4D", "AS", "2C", "9H", "9D"])
    self.assertFalse(hand.has_full())

  def test_simple_best_combo(self):
    hand = Hand(["4D", "AS", "9C", "2H", "4D"])
    self.assertEqual(
      hand.best_combo(),
      0 # is a pair
    )

  def test_complex_best_combo(self):
    hand = Hand(["AD", "AS", "9C", "9H", "9D"])
    self.assertEqual(
      hand.best_combo(),
      5 # is a full
    )

  def test_no_combo(self):
    hand = Hand(["9D", "AS", "8C", "7H", "2D"])
    self.assertEqual(
      hand.best_combo(),
      -1 # nothing
    )

class TestGame(unittest.TestCase):
  def test_highest_card(self):
    g = Game("2H 3D 5S 9C KD 2C 3H 4S 8C AH")
    who_won = g.who_is_the_winner_my_boy()
    self.assertEqual(
      who_won,
      1 # player 2
    )
    how_won = g.how_he_won()
    self.assertEqual(
      how_won,
      -1, # highest card
    )

  def test_full_vs_color(self):
    g = Game("2H 4S 4C 2D 4H 2S 8S AS QS 3S")
    who_won = g.who_is_the_winner_my_boy()
    self.assertEqual(
      who_won,
      0 # player 1
    )
    how_won = g.how_he_won()
    self.assertEqual(
      how_won,
      5 # full
    )

  def test_deep_highest_card(self):
    g = Game("2H 3D 5S 9C KD 2C 3H 4S 8C KH")
    who_won = g.who_is_the_winner_my_boy()
    self.assertEqual(
      who_won,
      0 # player 1
    )
    how_won = g.how_he_won()
    self.assertEqual(
      how_won,
      -1 # highest card
    )

  def test_draw(self):
    g = Game("2H 3D 5S 9C KD 2D 3H 5C 9S KH")
    who_won = g.who_is_the_winner_my_boy()
    self.assertEqual(
      who_won,
      -1 # draw
    )

import functools

from card import Card
from constant import Constant

class Hand:
  def __init__(self, raw_hand):
    self.raw_hand = raw_hand
    self.hand = [Card(rh) for rh in self.raw_hand]
    self.n_values = {x:self.as_classic_numeric.count(x) for x in set(self.as_classic_numeric)}

  @functools.cached_property
  def as_classic_numeric(self):
    return sorted([c.to_numeric(Constant.FIG_2_NUMBER_CLASSIC) for c in self.hand])

  @functools.cached_property
  def as_suite_numeric(self):
    return sorted([c.to_numeric(Constant.FIG_2_NUMBER_SUITE) for c in self.hand])

  def has_suite(self):
    if not len(self.n_values) == 5: return False
    return (max(self.as_suite_numeric) - min(self.as_suite_numeric)) == 4

  def has_color(self):
    colors = [card.color for card in self.hand]
    return all(colors[0] == c for c in colors)

  def has_flush(self):
    return self.has_suite() and self.has_color()

  def has_square(self):
    return 4 in self.n_values.values()

  def has_same_card(self, n):
    return any(x >= n for x in self.n_values.values())

  def has_double_pair(self):
    return len([x for x in self.n_values.values() if x == 2]) == 2

  def has_full(self):
    return sorted(self.n_values.values()) == [2, 3]

  def best_combo(self):
    all_combo = [
      self.has_same_card(2), # 0
      self.has_double_pair(), # 1
      self.has_same_card(3), # 2
      self.has_suite(), # 3
      self.has_color(), # 4
      self.has_full(), # 5
      self.has_square(), # 6
      self.has_flush() # 7
    ]

    return (
      max(valid_combos)
      if len(valid_combos := [idx for idx, combo in zip(range(0, 9), all_combo) if combo]) > 0
      else -1
    )

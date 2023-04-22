from hand import Hand

class Game:
  def __init__(self, input):
    assert len(input.strip()) == 29
    self.input = input.strip().split(" ")

    self.p1 = Hand(self.input[:5])
    self.p2 = Hand(self.input[5:])
    self.p_combo = [self.p1.best_combo(), self.p2.best_combo()]

  def how_he_won(self):
    return max(self.p_combo)

  def who_is_the_winner_my_boyyy(self):
    if len(set(self.p_combo)) > 1:
      return self.p_combo.index(self.how_he_won()) # crappy argmax function
    else:
      for p1_c, p2_c in zip(self.p1.as_classic_numeric[::-1], self.p2.as_classic_numeric[::-1]):
        if len(set(players := [p1_c, p2_c])) > 1 : # uuuuuh
          return players.index(max(players))

      return -1

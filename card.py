from constant import Constant

class Card:
  def __init__(self, card):
    self.value, self.type = [*card]
    self._check_validity()

    self.color = "R" if self.type in ["H", "S"] else "B"

  def _check_validity(self):
    if not self.value in Constant.VALIDE_VALUES:
      raise ValueError(f"invalid card value ({self.value})")
    elif not self.type in Constant.VALIDE_TYPES:
      raise ValueError(f"invalid card type {self.type}")

  def to_numeric(self, mapper):
    return int(
      mapper[self.value]
      if self.value in mapper.keys()
      else self.value
    )

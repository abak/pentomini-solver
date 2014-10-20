import numpy as np


class Board:
  def __init__(self):
    self._internal_array = np.zeros((8, 8))
    #center square remains empty
    self._internal_array[3,3] = 1
    self._internal_array[3,4] = 1
    self._internal_array[4,3] = 1
    self._internal_array[4,4] = 1
    self._nails = [(0, 0), (0, 2), (1, 5), (1, 7), (3, 0), (3, 5), (4, 2), (4, 7), (5, 4), (6, 0), (7, 2), (7, 6)]

  def pretty_print(self):
    tmp = self._internal_array
    for (y, x) in self._nails:
      tmp[y, x] = 42
    print str(tmp)

  def check_spot_empty(self, spot):
    if spot in self._nails:
      return False
    else:
      return self._internal_array[spot[0], spot[1]] == 0 


if __name__ == '__main__':
  board = Board()
  board.pretty_print()

  print board.check_spot_empty((0,1))
  print board.check_spot_empty((0,0))
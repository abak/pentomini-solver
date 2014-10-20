import numpy as np
from piece import Piece


class Board:
  def __init__(self, nails=[]):
    self._internal_array = np.zeros((8, 8))
    #center square remains empty
    self._internal_array[3,3] = 1
    self._internal_array[3,4] = 1
    self._internal_array[4,3] = 1
    self._internal_array[4,4] = 1
    # self._nails = [(0, 0), (0, 2), (1, 5), (1, 7), (3, 0), (3, 5), (4, 2), (4, 7), (5, 4), (6, 0), (7, 2), (7, 6)]
    for nail in nails:
      self._internal_array[nail] = 42

  def pretty_print(self):
    print str(self._internal_array)

  def check_spot_empty(self, spot):
    if spot[0] < 0 or spot[1] < 0:
      return False
    try :
      return self._internal_array[spot[0], spot[1]] == 0 
    except IndexError:
      #the piece falls out of the board
      return False

  def put_piece_in_spot(self, piece, nail, color):
    self._internal_array[nail] = color
    for y, x in piece._list:
      y += nail[0]
      x += nail[1]
      self._internal_array[y, x] = color


if __name__ == '__main__':
  board = Board()
  board.pretty_print()

  print board.check_spot_empty((0,1))
  print board.check_spot_empty((0,0))
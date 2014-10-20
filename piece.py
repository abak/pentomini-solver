import numpy as np


class Piece:
  def __init__(self, list):
    self._internal_array = np.zeros((9,9))
    #the hole
    self._internal_array[4,4] = 1
    for(y, x) in list:
      self._internal_array[y, x] = 1

  def pretty_print(self):
    print str(self._internal_array)
class Piece:
  def __init__(self, list=[]):
    self._list = list

  def pretty_print(self):
    tmp = np.zeros((9, 9))
    tmp[4, 4] = 1
    for (y, x) in self._list:
      tmp[y+4, x+4] = 1
    print str(tmp) + "\n"

  def rotate(self, orientation):
    if orientation >= 4:
      self._list = [(y, -x) for y, x in self._list]

    if orientation %4 == 0:
      return
    elif orientation %4 == 1:
      self._list = [(-x, y) for y,x in self._list]
    elif orientation %4 == 2:
      self._list = [(-y, -x) for y, x in self._list]
    elif orientation %4 == 3:
      self._list = [(x, -y) for y,x in self._list]


if __name__ == '__main__':
  p = Piece([(0, -1), (0, 1), (0, 2), (1, 1)])
  p.pretty_print()

  for i in range(0, 8):
    print i
    p = Piece([(0, -1), (0, 1), (0, 2), (1, 1)])
    p.rotate(i)
    p.pretty_print()

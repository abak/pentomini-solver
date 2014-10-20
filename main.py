import numpy as np
from board import Board
from piece import Piece

def init_pieces():
  res = []
  res.append(Piece([(4, 3), (4, 5), (4, 6), (5, 5)]))
  res.append(Piece([(4, 3), (5, 3), (6, 3), (4, 5)]))
  res.append(Piece([(4, 3), (4, 5), (4, 6), (4, 7)]))
  res.append(Piece([(5, 3), (5, 4), (5, 5), (6, 4)]))
  res.append(Piece([(5, 4), (4, 5), (4, 6), (5, 6)]))
  res.append(Piece([(4, 3), (5, 3), (4, 5), (4, 6)]))
  res.append(Piece([(5, 4), (5, 5), (5, 6), (6, 5)]))
  res.append(Piece([(5, 4), (6, 4), (5, 5), (6, 5)]))
  res.append(Piece([(4, 3), (5, 3), (5, 2), (6, 2)]))
  res.append(Piece([(4, 5), (5, 5), (6, 5), (6, 6)]))
  res.append(Piece([(5, 4), (5, 3), (6, 3), (7, 3)]))
  res.append(Piece([(4, 5), (4, 6), (5, 5), (6, 5)]))
  return res

def rotate_piece(piece, orientation):
  #probably highly ineffective
  new_piece = Piece()
  new_piece._internal_array = np.copy(piece._internal_array)

  if orientation >= 4:
    print "coucou"
    new_piece._internal_array = np.fliplr(new_piece._internal_array)

  new_piece._internal_array = np.rot90(new_piece._internal_array, orientation%4)

  return new_piece

def is_move_valid(board, piece, nail, orientation):
  piece_to_put = rotate_piece(piece, orientation)


def main():
  board = Board()
  pieces = init_pieces()

  # for p in pieces:
  #   p.pretty_print()
  #   print

  p = pieces[0]

  for i in range (0, 8):
    toto = rotate_piece(p, i)
    toto.pretty_print()

if __name__ == '__main__':
  main()
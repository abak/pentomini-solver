import numpy as np
from board import Board
from piece import Piece

def init_pieces():
  res = []
  res.append(Piece([(0, -1), (0, 1), (0, 2), (1, 1)]))
  res.append(Piece([(0, -1), (1, -1), (2, -1), (0, 1)]))
  res.append(Piece([(0, -1), (0, 1), (0, 2), (0, 3)]))
  res.append(Piece([(1, -1), (1, 0), (1, 1), (2, 0)]))
  res.append(Piece([(1, 0), (0, 1), (0, 2), (1, 2)]))
  res.append(Piece([(0, -1), (1, -1), (0, 1), (0, 2)]))
  res.append(Piece([(1, 0), (1, 1), (1, 2), (2, 1)]))
  res.append(Piece([(1, 0), (2, 0), (1, 1), (2, 1)]))
  res.append(Piece([(0, -1), (1, -1), (1, -2), (2, -2)]))
  res.append(Piece([(0, 1), (1, 1), (2, 1), (2, 2)]))
  res.append(Piece([(1, 0), (1, -1), (2, -1), (3, -1)]))
  res.append(Piece([(0, 1), (0, 2), (1, 1), (2, 1)]))
  return res

def rotate_piece(piece, orientation):
  #probably highly ineffective
  new_piece = Piece()
  new_piece._list = list(piece._list)
  new_piece.rotate(orientation)
  return new_piece

def is_move_valid(board, piece, nail, orientation):
  """
  basic assumption : that the nail is actually not occupied
  """
  piece_to_put = rotate_piece(piece, orientation)
  for y, x in piece_to_put._list :
    y += nail[0]
    x += nail[1]
    if not board.check_spot_empty((y, x)):
      return False
  return True

def main():
  board = Board()
  pieces = init_pieces()

  print is_move_valid(board, pieces[0], (0,2), 0)
  board.put_piece_in_spot(pieces[0], (0,2), 128)

  board.pretty_print()

  # for p in pieces:
  #   p.pretty_print()
  #   print

  # p = pieces[0]

  # for i in range (0, 8):
  #   toto = rotate_piece(p, i)
  #   toto.pretty_print()

if __name__ == '__main__':
  main()
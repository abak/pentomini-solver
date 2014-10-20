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
  piece_to_put = rotate_piece(piece, orientation)


def main():
  board = Board()
  pieces = init_pieces()

  for p in pieces:
    p.pretty_print()
    print

  # p = pieces[0]

  # for i in range (0, 8):
  #   toto = rotate_piece(p, i)
  #   toto.pretty_print()

if __name__ == '__main__':
  main()
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


def main():
  board = Board()
  pieces = init_pieces()

  for p in pieces:
    p.pretty_print()
    print

if __name__ == '__main__':
  main()
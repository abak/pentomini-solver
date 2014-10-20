import numpy as np
from board import Board
from piece import Piece
from random import randint

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

def put_piece(board, piece, nail, color):
  new_board = Board()
  new_board._internal_array = np.copy(board._internal_array)
  new_board.put_piece_in_spot(piece, nail, color)
  return new_board

def generate_valid_moves_for_nail(board, nail, pieces):
  moves = []
  for p in pieces:
    for orientation in range(0, 8):
      rotated = rotate_piece(p, orientation)
      if is_move_valid(board, rotated, nail):
        moves.append( (nail, rotated, [r for r in pieces if r != p]) )
  return moves

def is_move_valid(board, piece, nail):
  """
  basic assumption : that the nail is actually not occupied
  and that the piece arrives rotated
  """
  for y, x in piece._list :
    y += nail[0]
    x += nail[1]
    if not board.check_spot_empty((y, x)):
      return False
  return True

def iterate_dfs(board, nails, remaining_pieces):
  if not nails :
    print "completed, final board :"
    board.pretty_print()
    return 
  local_nails = list(nails)
  current_nail = local_nails.pop(0)
  possible_moves = generate_valid_moves_for_nail(board, current_nail, remaining_pieces)
  for move in possible_moves:
    new_board = put_piece(board, move[1], move[0], randint(0, 1000))
    iterate_dfs(new_board, local_nails, move[2])

def main():
  nails = [(0, 0), (0, 2), (1, 5), (1, 7), (3, 0), (3, 5), (4, 2), (4, 7), (5, 4), (6, 0), (7, 2), (7, 6)]
  board = Board(nails)
  pieces = init_pieces()

  # print is_move_valid(board, pieces[0], (0,2), 0)
  # new_board = put_piece(board, pieces[0], (0,2), 128)

  # board.pretty_print()
  # print "\n\n"
  # new_board.pretty_print()

  # current_nail = nails.pop(0)
  # possible_moves = generate_valid_moves_for_nail(board, current_nail, pieces)
  # for move in possible_moves:
  #   print move[1]
  #   print move[0]

  iterate_dfs(board, nails, pieces)

  # for p in pieces:
  #   p.pretty_print()
  #   print

  # p = pieces[0]

  # for i in range (0, 8):
  #   toto = rotate_piece(p, i)
  #   toto.pretty_print()

if __name__ == '__main__':
  main()
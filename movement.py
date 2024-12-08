from ChessEngine import *


def movement_piece(start_pieces, gs, current_coord, clicked_piece):
    possible_coord = []
    current_row = current_coord[0]
    current_col = current_coord[1]
    type_piece = clicked_piece[1]
    possible_rows = [0,1,2,3,4,5,6,7]
    possible_cols = [0,1,2,3,4,5,6,7]
    dummy_coord = []  # Checks for everything inside the board

    if type_piece == "p":
        possible_coord= movement_pawn(start_pieces, clicked_piece, current_row, current_col)
    elif type_piece == "R":
        possible_coord = movement_rook(start_pieces, clicked_piece, current_row, current_col)

    elif type_piece == "N":
        possible_coord = movement_knight(start_pieces, clicked_piece, current_row, current_col)

    elif type_piece == "B":
        possible_coord = movement_bishop(start_pieces, clicked_piece, current_row, current_col)
    elif type_piece == "K":
        possible_coord = movement_king(start_pieces, clicked_piece, current_row, current_col)
    elif type_piece == "Q":
        possible_coord = movement_queen(start_pieces, clicked_piece, current_row, current_col)

    for index, item in enumerate(possible_coord):
        if item != current_coord and (8 > item[0] >= 0) and (8 > item[1] >= 0):  # Coords elimineren die buiten bord liggen
            dummy_coord.append(item)
    possible_coord = dummy_coord[:]
    print(possible_coord)
    return possible_coord

def movement_rook(start_pieces, clicked_piece, current_row, current_col):
    clicked_color = start_pieces[clicked_piece].color
    possible_coord = []
    stop = 0
    for r in range(7-current_row):
        for item in start_pieces.values():
            if item.position == [current_row, current_col+r+1] and item.color == clicked_color:
                stop = 1
                break
        if stop==1:
            stop = 0
            break
        possible_coord.append([current_row, current_col+r+1])
    for r in range(current_row):
        for item in start_pieces.values():
            if item.position == [current_row, current_col-r-1] and item.color == clicked_color:
                stop = 1
                break
        if stop == 1:
            stop = 0
            break
        possible_coord.append([current_row, current_col-r-1])
    for r in range(7-current_col):
        for item in start_pieces.values():
            if item.position == [current_row+r+1, current_col] and item.color == clicked_color:
                stop = 1
                break
        if stop == 1:
            stop = 0
            break
        possible_coord.append([current_row+r+1, current_col])
    for r in range(current_col):
        for item in start_pieces.values():
            if item.position == [current_row-r-1, current_col] and item.color == clicked_color:
                stop = 1
                break
        if stop == 1:
            stop = 0
            break
        possible_coord.append([current_row-r-1, current_col])
    return possible_coord

def movement_knight(start_pieces, clicked_piece, current_row, current_col):
    possible_coord = []
    clicked_color = start_pieces[clicked_piece].color
    knight_moves = [
        (1, 2), (1, -2), (2, 1), (2, -1),
        (-1, 2), (-1, -2), (-2, 1), (-2, -1)
    ]
    possible_coord = [
        [current_row + r, current_col + c]
        for r, c in knight_moves
    ]
    for v in start_pieces.values():
        if v.position in possible_coord:
            if v.color == clicked_color:
                possible_coord.remove(v.position)
    return possible_coord

def movement_bishop(start_pieces, clicked_piece, current_row, current_col):
    possible_coord = []
    clicked_color = start_pieces[clicked_piece].color
    stop = 0
    for f in range(7):
        for item in start_pieces.values():
            if item.position == [current_row + (1 + f), current_col + (1 + f)] and item.color == clicked_color:
                stop = 1
                break
        if stop == 1:
            stop = 0
            break
        possible_coord.append([current_row + (1 + f), current_col + (1 + f)])
    for f in range(7):
        for item in start_pieces.values():
            if item.position == [current_row + (1 + f), current_col - (1 + f)] and item.color == clicked_color:
                stop = 1
                break
        if stop == 1:
            stop = 0
            break
        possible_coord.append([current_row + (1 + f), current_col - (1 + f)])
    for f in range(7):
        for item in start_pieces.values():
            if item.position == [current_row - (1 + f), current_col + (1 + f)] and item.color == clicked_color:
                stop = 1
                break
        if stop == 1:
            stop = 0
            break
        possible_coord.append([current_row - (1 + f), current_col + (1 + f)])
    for f in range(7):
        for item in start_pieces.values():
            if item.position == [current_row - (1 + f), current_col - (1 + f)] and item.color == clicked_color:
                stop = 1
                break
        if stop == 1:
            stop = 0
            break
        possible_coord.append([current_row - (1 + f), current_col - (1 + f)])
    return possible_coord

def movement_queen(start_pieces, clicked_piece, current_row, current_col):
    possible_coord = []
    clicked_color = start_pieces[clicked_piece].color
    possible_coord.extend(movement_rook(start_pieces, clicked_piece, current_row, current_col))
    possible_coord.extend(movement_bishop(start_pieces, clicked_piece, current_row, current_col))
    return possible_coord

def movement_king(start_pieces, clicked_piece, current_row, current_col):
    possible_coord = []
    clicked_color = start_pieces[clicked_piece].color
    king_moves = [
        (1, 0), (-1, 0), (1, 1), (-1, 1),
        (0, 1), (0, -1), (-1, -1), (1, -1)
    ]
    possible_coord = [
        [current_row + dr, current_col + dc]
        for dr, dc in king_moves
    ]
    for v in start_pieces.values():
        if v.position in possible_coord:
            if v.color == clicked_color:
                possible_coord.remove(v.position)

    return possible_coord

def movement_pawn(start_pieces, clicked_piece, current_row, current_col):
    possible_coord = []
    clicked_color = start_pieces[clicked_piece].color
    if start_pieces[clicked_piece].color == "w":
        for v in start_pieces.values():
            if v.position == [current_row-1, current_col -1] and v.color != clicked_color:
                possible_coord.append(v.position)
            elif v.position == [current_row-1, current_col +1] and v.color != clicked_color:
                possible_coord.append(v.position)
            elif v.position == [current_row-1,current_col]:
                possible_coord = []
                return possible_coord
            elif v.position == [current_row-2,current_col]:
                possible_coord.append([current_row-1,current_col])
                return possible_coord
        if current_row == 6:
            possible_coord.append([current_row - 1, current_col])
            possible_coord.append([current_row - 2, current_col])
        else:
            possible_coord.append([current_row - 1, current_col])
    else:
        for v in start_pieces.values():
            if v.position == [current_row+1, current_col -1] and v.color != clicked_color:
                possible_coord.append(v.position)
            elif v.position == [current_row+1, current_col +1] and v.color != clicked_color:
                possible_coord.append(v.position)
            elif v.position == [current_row+1,current_col]:
                possible_coord = []
                return possible_coord
            elif v.position == [current_row+2,current_col]:
                possible_coord.append([current_row+1,current_col])
                return possible_coord
        if current_row == 1:
            possible_coord.append([current_row + 1, current_col])
            possible_coord.append([current_row + 2, current_col])
        else:
            possible_coord.append([current_row + 1, current_col])
    return possible_coord

from ChessEngine import *


def movement_piece(start_pieces, gs,current_coord,clicked_piece):
    possible_coord = []
    current_row = current_coord[0]
    current_col = current_coord[1]
    type_piece = clicked_piece[1]
    dummy_coord = [] #Checks for everything inside the board
    if type_piece == "p":
        if clicked_piece[0:2] == "wp":
            if current_coord[0] == 6:
                possible_coord = [[current_row-1,current_col],[current_row-2,current_col]]
            else:
                possible_coord = [[current_row-1,current_col]]
        else:
            if current_row == 1:
                possible_coord = [[current_row + 1, current_col], [current_row + 2, current_col]]
            else:
                possible_coord = [[current_row + 1, current_col]]
    elif type_piece == "R":
        for r in range(8):
            possible_coord.append([current_row,r])
            possible_coord.append([r,current_col])

    elif type_piece == "N":
        possible_coord.append([current_row+1, current_col +2])
        possible_coord.append([current_row+1,current_col-2])
        possible_coord.append([current_row+2,current_col+1])
        possible_coord.append([current_row+2,current_col-1])
        possible_coord.append([current_row-1,current_col+2])
        possible_coord.append([current_row-1,current_col-2])
        possible_coord.append([current_row-2,current_col+1])
        possible_coord.append([current_row-2,current_col-1])

    elif type_piece == "B":
        for f in range(7):
            possible_coord.append([current_row+(1+f),current_col+(1+f)])
            possible_coord.append([current_row+(1+f),current_col-(1+f)])
            possible_coord.append([current_row-(1+f),current_col+(1+f)])
            possible_coord.append([current_row-(1+f),current_col-(1+f)])
    elif type_piece == "K":
        possible_coord.append([current_row+1,current_col])
        possible_coord.append([current_row-1,current_col])
        possible_coord.append([current_row+1,current_col+1])
        possible_coord.append([current_row-1,current_col+1])
        possible_coord.append([current_row,current_col+1])
        possible_coord.append([current_row,current_col-1])
        possible_coord.append([current_row-1,current_col-1])
        possible_coord.append([current_row+1,current_col-1])
    elif type_piece == "Q":
        for f in range(7):
            possible_coord.append([current_row+(1+f),current_col+(1+f)])
            possible_coord.append([current_row+(1+f),current_col-(1+f)])
            possible_coord.append([current_row-(1+f),current_col+(1+f)])
            possible_coord.append([current_row-(1+f),current_col-(1+f)])
        for r in range(8):
            possible_coord.append([current_row,r])
            possible_coord.append([r,current_col])


    for index, item in enumerate(possible_coord):
        if item != current_coord and (0 <= item[0] < 8) and (0 <= item[1] < 8): #Coords elimineren die buiten bord liggen
            dummy_coord.append(item)
    for v in start_pieces.values():
        for item in dummy_coord:
            if v.position == item:
                if clicked_piece[1] == "p": #Uitzondering schuin slaan voor pion, kan niet rechtdoor slaan
                    dummy_coord.remove(item)
                elif v.color == start_pieces[clicked_piece].color: #Coords removen waar een stuk van uw kleur op staat
                    dummy_coord.remove(item)
            else:
                continue

    possible_coord = dummy_coord[:]
    print(possible_coord)
    return possible_coord


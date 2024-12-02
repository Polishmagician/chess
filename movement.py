
def movement_piece(gs,current_coord,clicked_piece):
    possible_coord = []
    current_row = current_coord[0]
    current_col = current_coord[1]
    type_piece = clicked_piece[1]
    dummy_coord = []
    if type_piece == "p":
        if clicked_piece == "wp":
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
        for index,item in enumerate(possible_coord):
            if item != current_coord:
                dummy_coord.append(item)
        possible_coord = dummy_coord[:]
        print(possible_coord)
    return possible_coord
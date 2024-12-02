import pygame as p
import ChessEngine

width = height = 400
dimension = 8
sq_size = height/dimension
max_fps = 15 #Animations later on
images = {}
whitepieces = ["wR","wN","wB","wQ","wK","wB","wN","wR","wp"]
blackpieces = ["bR","bN","bB","bQ","bK","bB","bN","bR","bp"]
#Initialize global dict of images. This will be calles once in the main

def loadImages():
    pieces = ["bR","bN","bB","bQ","bK","bB","bN","bR","wR","wN","wB","wQ","wK","wB","wN","wR","wp","bp"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load(f"images/{piece}.svg"),(sq_size,sq_size))
    #Note we can acces an image by saying 'images['wp']

#The main driver. This will handle user input and updating graphics
def main():
    p.init()
    screen = p.display.set_mode((width,height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages() #only once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            drawGameState(screen,gs) #Show current position
            if e.type == p.QUIT: #Possibility to quit
                running = False
            if e.type == p.MOUSEBUTTONDOWN: #Piece pressed
                current_pos = p.mouse.get_pos()
                current_col_pos = int(current_pos[0]//sq_size)
                current_row_pos = int(current_pos[1]//sq_size)
                clicked_piece = gs.board[current_row_pos][current_col_pos]
                if gs.whiteToMove == True: #White to move
                    if clicked_piece not in whitepieces: #Selected piece is black
                        clicked_piece = ""
                else: #Black to move
                    if clicked_piece not in blackpieces: #Selected piece is white
                        clicked_piece = ""
            if e.type == p.MOUSEBUTTONUP:
                if clicked_piece != "":
                    if gs.whiteToMove == True: #White move
                        new_pos = p.mouse.get_pos()
                        new_col_pos = int(new_pos[0]//sq_size)
                        new_row_pos = int(new_pos[1]//sq_size)
                        possible_row = movement_piece(gs,current_col_pos,current_row_pos,clicked_piece)
                        if new_row_pos in possible_row:
                            gs.board[current_row_pos][current_col_pos] = "--"
                            gs.board[new_row_pos][new_col_pos] = clicked_piece
                            gs.whiteToMove = False
                    else: #Black move
                        new_pos = p.mouse.get_pos() #werkt iets niet
                        new_col_pos = int(new_pos[0] // sq_size)
                        new_row_pos = int(new_pos[1] // sq_size)
                        possible_row = movement_piece(gs, current_col_pos, current_row_pos, clicked_piece)
                        if new_row_pos in possible_row:
                            gs.board[current_row_pos][current_col_pos] = "--"
                            gs.board[new_row_pos][new_col_pos] = clicked_piece
                            gs.whiteToMove = True
                else:
                    continue
        clock.tick(max_fps)
        p.display.flip()

#Graphics of curent gamestate
def drawGameState(screen, gs):
    drawBoard(screen) #Draws squares on board
    drawPieces(screen, gs.board) #Draw pieces on top of squares

#Draw squares on board
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")] #Can change color schemes
    for row in range(dimension):
        for col in range(dimension):
            color = colors[(row + col) % 2]
            p.draw.rect(screen, color, p.Rect(col * sq_size, row * sq_size, sq_size, sq_size))


#Draw pieces on board
def drawPieces(screen, board):
    for row in range(dimension):
        for col in range(dimension):
            piece = board[row][col]
            if piece != "--": #not empty square
                screen.blit(images[piece], p.Rect(col*sq_size, row*sq_size, sq_size, sq_size))

def movement_piece(gs,current_col,current_row,clicked_piece):
    possible_row = [0,1,2,3,4,5,6,7]
    type_piece = clicked_piece[1]
    if type_piece == "p":
        if current_row == 6:
            possible_row = [5,4]
        else:
            possible_row = [current_row-1]
    return possible_row


main()

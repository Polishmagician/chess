import pygame as p
from ChessEngine import *
from movement import *

width = height = 400
dimension = 8
sq_size = height/dimension
max_fps = 15 #Animations later on
images = {}
start_pieces = {}
whitepieces = ["wR","wN","wB","wQ","wK","wB","wN","wR","wp"]
blackpieces = ["bR","bN","bB","bQ","bK","bB","bN","bR","bp"]
#Initialize global dict of images. This will be calles once in the main

def loadImages():
    pieces = ["bR","bN","bB","bQ","bK","bB","bN","bR","wR","wN","wB","wQ","wK","wB","wN","wR","wp","bp"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load(f"images/{piece}.svg"),(sq_size,sq_size))
    #Note we can acces an image by saying 'images['wp']
def start_position():
    white_pawns = ["wp1","wp2","wp3","wp4","wp5","wp6","wp7","wp8"]
    for index,p in enumerate(white_pawns):
        start_pieces[p] = pawn("w",[6,index])
    black_pawns = ["bp1","bp2","bp3","bp4","bp5","bp6","bp7","bp8"]
    for index,p in enumerate(black_pawns):
        start_pieces[p] = pawn("w",[1,index])
    start_pieces["wR1"] = rook("w",[7,0])
    start_pieces["bR1"] = rook("b",[0,0])
    start_pieces["wR2"] = rook("w",[7,7])
    start_pieces["bR2"] = rook("b",[0,7])
    start_pieces["wB1"] = rook("w", [7, 2])
    start_pieces["bB1"] = rook("b", [0, 2])
    start_pieces["wB2"] = rook("w", [7, 5])
    start_pieces["bB2"] = rook("b", [0, 5])
    start_pieces["wN1"] = rook("w", [7, 1])
    start_pieces["bN1"] = rook("b", [0, 1])
    start_pieces["wN2"] = rook("w", [7, 6])
    start_pieces["bN2"] = rook("b", [0, 6])
    start_pieces["wQ1"] = rook("w", [7, 3])
    start_pieces["bQ1"] = rook("b", [0, 3])
    start_pieces["wK1"] = rook("w", [7, 4])
    start_pieces["bK1"] = rook("b", [0, 4])


#The main driver. This will handle user input and updating graphics
def main():
    p.init()
    screen = p.display.set_mode((width,height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = GameState()
    loadImages() #only once, before the while loop
    start_position()
    running = True
    while running:
        for e in p.event.get():
            drawGameState(screen,gs) #Show current position
            if e.type == p.QUIT: #Possibility to quit
                running = False
            if e.type == p.MOUSEBUTTONDOWN: #Piece pressed
                current_pos = p.mouse.get_pos()
                current_coord = [int(current_pos[1]//sq_size), int(current_pos[0]//sq_size)]
                for name,item in start_pieces.items():
                    if item.position == current_coord:
                        clicked_piece = name
                        print(clicked_piece)
                        print(start_pieces[clicked_piece].position)
                    # else:
                    #     clicked_piece = ""
            if e.type == p.MOUSEBUTTONUP:
                # if clicked_piece != "":
                new_pos = p.mouse.get_pos()
                new_coord = [int(new_pos[1]//sq_size), int(new_pos[0]//sq_size)]
                start_pieces[clicked_piece].position = new_coord
                print(start_pieces[clicked_piece].position)
                    # possible_coord = movement_piece(gs,current_coord,clicked_piece)
                    # if new_coord in possible_coord:
                    #     print("ok")
                    # else:
                    #     print("false")
                # else:
                #     continue
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


main()
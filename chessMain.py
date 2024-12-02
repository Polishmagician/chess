import pygame as p
import ChessEngine
from movement import *

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
                current_coord = [int(current_pos[1]//sq_size), int(current_pos[0]//sq_size)]
                clicked_piece = gs.board[current_coord[0]][current_coord[1]]
            if e.type == p.MOUSEBUTTONUP:
                if clicked_piece != "":
                    new_pos = p.mouse.get_pos()
                    new_coord = [int(new_pos[1]//sq_size), int(new_pos[0]//sq_size)]
                    possible_coord = movement_piece(gs,current_coord,clicked_piece)
                    if new_coord in possible_coord:
                        print("ok")
                    else:
                        print("false")
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




main()

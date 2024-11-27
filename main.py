import pygame

pieces_images = {
    "white_pawn":"images/Chess_plt45.svg",
    "white_knight":"images/Chess_nlt45.svg",
    "white_bishop":"images/Chess_blt45.svg",
    "white_rook":"images/Chess_rlt45.svg",
    "white_queen":"images/Chess_qlt45.svg",
    "white_king":"images/Chess_klt45.svg",
    "black_pawn":"images/Chess_pdt45.svg",
    "black_knight":"images/Chess_ndt45.svg",
    "black_bishop":"images/Chess_bdt45.svg",
    "black_rook":"images/Chess_rdt45.svg",
    "black_queen":"images/Chess_qdt45.svg",
    "black_king":"images/Chess_kdt45.svg",
}

def draw_chessboard():

    #Initialize chessboard
    pygame.init()
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chessboard")

    square_size = width // 8
    colors = [pygame.Color("white"), pygame.Color("grey")]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color("black"))

        #Drawing the squares on the screen
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                pygame.draw.rect(screen, color, pygame.Rect(col * square_size, row * square_size, square_size, square_size))

# Loading and drawing a piece
        #Black knights
        black_knight_image = pygame.image.load(pieces_images['black_knight'])  # Replace with your image file
        black_knight_image = pygame.transform.scale(black_knight_image, (square_size, square_size))
        screen.blit(black_knight_image,(1*square_size,0*square_size))
        screen.blit(black_knight_image, (6 * square_size, 0 * square_size))

        #Black rooks
        black_rook_image = pygame.image.load(pieces_images['black_rook'])  # Replace with your image file
        black_rook_image = pygame.transform.scale(black_rook_image, (square_size, square_size))
        screen.blit(black_rook_image, (0 * square_size, 0 * square_size))
        screen.blit(black_rook_image, (7 * square_size, 0 * square_size))

        #Black bishops
        black_bishop_image = pygame.image.load(pieces_images['black_bishop'])  # Replace with your image file
        black_bishop_image = pygame.transform.scale(black_bishop_image, (square_size, square_size))
        screen.blit(black_bishop_image, (2 * square_size, 0 * square_size))
        screen.blit(black_bishop_image, (5 * square_size, 0 * square_size))

        #Black queen
        black_queen_image = pygame.image.load(pieces_images['black_queen'])  # Replace with your image file
        black_queen_image = pygame.transform.scale(black_queen_image, (square_size, square_size))
        screen.blit(black_queen_image, (3 * square_size, 0 * square_size))

        #Black king
        black_king_image = pygame.image.load(pieces_images['black_king'])  # Replace with your image file
        black_king_image = pygame.transform.scale(black_king_image, (square_size, square_size))
        screen.blit(black_king_image, (4 * square_size, 0 * square_size))

        #Black pawns
        black_pawn_image = pygame.image.load(pieces_images['black_pawn'])  # Replace with your image file
        black_pawn_image = pygame.transform.scale(black_pawn_image, (square_size, square_size))
        for f in range(8):
            screen.blit(black_pawn_image, (f * square_size, 1 * square_size))

            # white knights
            white_knight_image = pygame.image.load(pieces_images['white_knight'])  # Replace with your image file
            white_knight_image = pygame.transform.scale(white_knight_image, (square_size, square_size))
            screen.blit(white_knight_image, (1 * square_size, 7 * square_size))
            screen.blit(white_knight_image, (6 * square_size, 7 * square_size))

            # white rooks
            white_rook_image = pygame.image.load(pieces_images['white_rook'])  # Replace with your image file
            white_rook_image = pygame.transform.scale(white_rook_image, (square_size, square_size))
            screen.blit(white_rook_image, (0 * square_size, 7 * square_size))
            screen.blit(white_rook_image, (7 * square_size, 7 * square_size))

            # white bishops
            white_bishop_image = pygame.image.load(pieces_images['white_bishop'])  # Replace with your image file
            white_bishop_image = pygame.transform.scale(white_bishop_image, (square_size, square_size))
            screen.blit(white_bishop_image, (2 * square_size, 7 * square_size))
            screen.blit(white_bishop_image, (5 * square_size, 7 * square_size))

            # white queen
            white_queen_image = pygame.image.load(pieces_images['white_queen'])  # Replace with your image file
            white_queen_image = pygame.transform.scale(white_queen_image, (square_size, square_size))
            screen.blit(white_queen_image, (3 * square_size, 7 * square_size))

            # white king
            white_king_image = pygame.image.load(pieces_images['white_king'])  # Replace with your image file
            white_king_image = pygame.transform.scale(white_king_image, (square_size, square_size))
            screen.blit(white_king_image, (4 * square_size, 7 * square_size))

            # white pawns
            white_pawn_image = pygame.image.load(pieces_images['white_pawn'])  # Replace with your image file
            white_pawn_image = pygame.transform.scale(white_pawn_image, (square_size, square_size))
            for f in range(8):
                screen.blit(white_pawn_image, (f * square_size, 6 * square_size))

        pygame.display.flip() #confirming drawings

    pygame.quit()

draw_chessboard()


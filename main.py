import display

valid_fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'

game_board = display.start()

while True:
    display.update(valid_fen, game_board)

# display.terminate()

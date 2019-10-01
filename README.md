# chess-board

## What is chess-board?

chess-board is a Python chessboard package with a flexible "just a board" API for graphically representing game positions.

## What chess-board is **not**

- A chess engine
- A legal move validator
- A PGN parser

While chess-board is designed to work well with any of these, the idea behind chess-board is that the logic that controls the board should be independent of those other problems.

## Usage
**test.py** - _example_
```sh
from chessboard import display

position = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'

while True:
    display.start(position)
```

## Entry Points
```sh
from chessboard import display

validfen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2'

# Initialization
display.start()

# Position change/update
display.update(validfen)

# Checking GUI window for QUIT event. (Esc or GUI CANCEL)
display.checkForQuit()

# Close window
display.terminate()

```
## Installation
Download and install the latest release:
```sh
# install into virtualenv
pip install chess-board

or 

# install with pipenv
pipenv install chess-board

or

# install system-wide (windows), run cmd[powershell] as administrator
pip install chess-board
```

Alternatively, you could **git clone** this repo and add the directory to your package.

```sh
git clone https://github.com/ahira-justice/chess-board.git
```

## Dependencies
```sh
pygame
```
**chess-board** installation automatically installs latest **pygame** version.

## License

[GNU GENERAL PUBLIC LICENSE](LICENSE)

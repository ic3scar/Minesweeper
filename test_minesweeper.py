from board import Board
from minesweeper import Minesweeper_Game

# For testing
# b = Board(10,10,15)
# b.display_board()

while True:
    m = input('Please enter the number of rows for the play board: ')
    n = input('Please enter the number of columns for the play board: ')
    k = input('Please enter the number of mines: ')
    if m.isdigit() and n.isdigit() and k.isdigit():
        m,n,k = int(m),int(n),int(k)
        if m>0 and n>0 and k<=m*n//4:
            break
    print('The input either contains invalid characters or has too many mines! Please re-enter the parameters.')
game = Minesweeper_Game(m,n,k)

game.play()
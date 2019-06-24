from board import Board
from collections import deque

"""
For simplicity, assuming that the game is completed if every block matches with the default block
Every number should be clicked and every mine should be marked out
"""


class Minesweeper_Game:
    def __init__(self,m=10,n=10,k=10):
        self.number_of_rows = m
        self.number_of_columns = n
        self.number_of_mines = k
    
    def initialize(self):
        self.is_winner= False
        self.is_loser = False
        self.play_board = Board(self.number_of_rows, self.number_of_columns,0)
        self.mine_board = Board(self.number_of_rows,self.number_of_columns,self.number_of_mines)
        self.checked = [[0]* self.number_of_columns for i in range(self.number_of_rows)]
        self.mines_on_board = self.number_of_mines

    def play(self):
        while True:
            self.initialize()
            # For testing
            # self.mine_board.display_board()
            self.play_game()
            option = input('Do you want to continue? Yes(Y) or No(N): ')
            if option not in {'Y','y'}:
                break

    def play_game(self):
        self.play_board.display_play_board()
        while not self.is_winner and not self.is_loser:
            r,c = self.get_block_to_check()
            while True:
                option = input('Do you want to left-click(L) or right-click(R): ')
                if option=='L' or option=='R':
                    break
                print('Please enter a valid option.')
            if option == 'L':
                self.update_play_board(r,c)
            else:
                if self.is_checked(r,c):
                    print('It is not a valid move')
                    continue
                if not self.play_board.blocks[r][c].isMine:
                    self.mines_on_board -= 1
                self.checked[r][c]=1
                self.play_board.blocks[r][c].place_mine()
            if not self.is_winner and not self.is_loser:
                self.play_board.display_play_board()
                print('Number of mines unchecked: ', self.mines_on_board)
            if self.mines_on_board==0 and self.check_completeness():
                self.is_winner = True
        if self.is_winner:
            print('Congratulations!')
        else:
            print('Better luck next time!')
            self.mine_board.display_board()


    def get_block_to_check(self):
        s = input('Enter row,col (two numbers separated by a comma): ')
        stat = True
        try:
            r,c = map(int,s.split(','))
            return r,c
        except:
            stat = False
            if s=='ddd':
                self.mine_board.display_board()
            print('Please enter a valid spot.')
        if stat==False:
            return self.get_block_to_check()

    def update_play_board(self,r,c):
        self.checked[r][c]=1
        if self.play_board.blocks[r][c].isMine:
            self.play_board.blocks[r][c].isMine = False
            self.play_board.blocks[r][c].update_value(0)
            self.mines_on_board+= 1
        if self.mine_board.blocks[r][c].isMine:
            print('It is a mine!')
            self.is_loser = True
            return
        elif self.mine_board.blocks[r][c].number>0:
            self.play_board.blocks[r][c].update_value(self.mine_board.blocks[r][c].number)
            return
        else: # left-clicked on a blank spot
            # print('About to expand the blank space')
            self.checked[r][c]=1
            self.play_board.blocks[r][c].update_value('X')
            self.expand(r,c)

    def expand(self,r,c):
        queue =  deque([(r,c)])
        while queue:
            r,c = queue.popleft()
            if r+1<self.number_of_rows and not self.is_checked(r+1,c):
                self.update_block(r+1,c,queue)
            if r+1<self.number_of_rows and c+1<self.number_of_columns and not self.is_checked(r+1,c+1):
                self.update_block(r+1,c+1,queue)
            if c+1<self.number_of_columns and not self.is_checked(r,c+1):
                self.update_block(r,c+1,queue)
            if r>0 and c+1<self.number_of_columns and not self.is_checked(r-1,c+1):
                self.update_block(r-1,c+1,queue)
            if r>0 and not self.is_checked(r-1,c):
                self.update_block(r-1,c,queue)
            if r>0 and c>0 and not self.is_checked(r-1,c-1):
                self.update_block(r-1,c-1,queue)
            if c>0 and not self.is_checked(r,c-1):
                self.update_block(r,c-1,queue)
            if r+1<self.number_of_rows and c>0 and not self.is_checked(r+1,c-1):
                self.update_block(r+1,c-1,queue)
            
    
    def is_checked(self,r,c):
        return self.checked[r][c]==1
        
    def update_block(self,r,c,queue):
        self.checked[r][c]=1
        if self.mine_board.blocks[r][c].number==0:
            queue.append((r,c))
            self.play_board.blocks[r][c].number='X'
        else:
            self.play_board.blocks[r][c].update_value(self.mine_board.blocks[r][c].number)

    def display_current_board(self):
        self.play_board.display_play_board()
    
    def check_completeness(self):
        for r in range(self.number_of_rows):
            for c in range(self.number_of_columns):
                if not self.is_checked(r,c):
                    return False
        return self.mine_board.compare_with(self.play_board)
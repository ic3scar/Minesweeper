import random

class Block:
    def __init__(self,num = 0):
        self.number = num
        self.isMine = False
        self.isChecked = False
    
    def update_value(self,num):
        self.number = num

    def place_mine(self):
        self.isMine = True

    def __repr__(self):
        return self.number

class Board:
    def __init__(self,m=10,n=10,k=10):
        self.blocks = []
        for i in range(m):
            temp = [Block() for j in range(n)]
            self.blocks.append(temp)
        self.number_of_mines = k
        self.number_of_rows = m
        self.number_of_columns = n
        self.form_playboard()

    def form_playboard(self):
        valid_spots = [(i,j) for i in range(self.number_of_rows) for j in range(self.number_of_columns)]
        size = self.number_of_rows * self.number_of_columns
        for i in range(self.number_of_mines):
            ind = random.randrange(0,size-i)
            r,c = valid_spots[ind]
            self.place_mine(r,c)
            valid_spots[ind],valid_spots[size-1-i] = valid_spots[size-1-i],valid_spots[ind]

    def place_mine(self,r,c):
        self.blocks[r][c].isMine = True
        # We can also increment the number of each surrounding block by 1
        # It doesn't matter here if a surrounding block has a mine or not. 
        # This will be dealt with when displaying the playground
        if r+1<self.number_of_rows:
            self.blocks[r+1][c].number += 1
        if r+1<self.number_of_rows and c+1<self.number_of_columns:
            self.blocks[r+1][c+1].number += 1
        if c+1<self.number_of_columns:
            self.blocks[r][c+1].number += 1
        if r>0 and c+1<self.number_of_columns:
            self.blocks[r-1][c+1].number += 1
        if r>0:
            self.blocks[r-1][c].number += 1
        if r>0 and c>0:
            self.blocks[r-1][c-1].number += 1
        if c>0:
            self.blocks[r][c-1].number += 1
        if r+1<self.number_of_rows and c>0:
            self.blocks[r+1][c-1].number += 1
        
    def display_play_board(self):
        temp = ['   ']
        for c in range(self.number_of_columns):
            temp.append(str(c).center(3))
        s = '|'.join(temp)
        print(s)
        print('-'*(4*self.number_of_columns+3))
        for r in range(self.number_of_rows):
            temp = [str(r).center(3)]
            for c in range(self.number_of_columns):
                if self.blocks[r][c].isMine:
                    temp.append(' * ')
                elif self.blocks[r][c].number==0:
                    temp.append('   ')
                else:
                    temp.append(str(self.blocks[r][c].number).center(3))
            s = '|'.join(temp)
            print(s)
            print('-'*(4*self.number_of_columns+3))
        print()       
    
    def display_board(self):
        temp = ['   ']
        for c in range(self.number_of_columns):
            temp.append(str(c).center(3))
        s = '|'.join(temp)
        print(s)
        print('-'*(4*self.number_of_columns+3))
        for r in range(self.number_of_rows):
            temp = [str(r).center(3)]
            for c in range(self.number_of_columns):
                if self.blocks[r][c].isMine:
                    temp.append(' * ')
                elif self.blocks[r][c].number==0:
                    temp.append(' X ')
                else:
                    temp.append(str(self.blocks[r][c].number).center(3))
            s = '|'.join(temp)
            print(s)
            print('-'*(4*self.number_of_columns+3))
        print()
    
    def compare_with(self,board):
        for r in range(self.number_of_rows):
            for c in range(self.number_of_columns):
                # For testing
                # print(self.blocks[r][c].number, self.blocks[r][c].isMine, board.blocks[r][c].number,board.blocks[r][c].isMine)
                if self.blocks[r][c].isMine:
                    if not board.blocks[r][c].isMine:
                        return False
                elif self.blocks[r][c].number==0:
                    if board.blocks[r][c].number!=0 and board.blocks[r][c].number!='X':
                        return False
                else:
                    if board.blocks[r][c].number!=self.blocks[r][c].number:
                        return False
        return True
           
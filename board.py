from turtle import Turtle
from random import Random
FONT = ('verdana', 30, 'normal')
STARTING_X = -120
STARTING_Y = 100
SPACE = 80


class Board():

    def __init__(self, screen):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(STARTING_X, STARTING_Y)
        self.screen = screen
        self.tiles = [
            [0, 2, 0, 0],
            [2, 2, 0, 0],
            [2, 2, 2, 2],
            [2, 2, 2, 2]
        ]
        self.void_pos = (3, 3)
        self.draw_tiles()

    def draw_tiles(self):
        self.turtle.clear()
        self.turtle.goto(STARTING_X, STARTING_Y)
        for row in self.tiles:
            for col in row:
                self.turtle.write(f'{col}', align='center', font=FONT)
                self.turtle.goto(self.turtle.xcor() + SPACE, self.turtle.ycor())
            self.turtle.goto(STARTING_X, self.turtle.ycor() - SPACE)

    def go_up(self):
        # move eveything to the top
        for column in range(0,4):
            zero_pos = 0
            for row in range(0,4):
                if self.tiles[row][column]==0:
                    zero_pos += 1
                else:
                    new_val = self.tiles[row][column]
                    old_val = self.tiles[row-zero_pos][column]
                    self.tiles[row-zero_pos][column] = new_val
                    self.tiles[row][column] = old_val
            print(self.tiles[column])
        for column in range (0,4):
            row_start = 0
            check_position = [0,2]
            for position in range(0,4):
                if self.tiles[position][column] > 0:
                    if self.tiles[position][column] == self.tiles[position+1][column]:
                        sumval = self.tiles[position][column] + self.tiles[position+1][column]
                        self.tiles[position][column] = sumval
                        self.tiles[position + 1][column] = 0
        for column in range(0,4):
            zero_pos = 0
            for row in range(0,4):
                if self.tiles[row][column]==0:
                    zero_pos += 1
                else:
                    new_val = self.tiles[row][column]
                    old_val = self.tiles[row-zero_pos][column]
                    self.tiles[row-zero_pos][column] = new_val
                    self.tiles[row][column] = old_val
            print(self.tiles[column])
        self.draw_tiles()



    def go_down(self):
        up_to_void_pos = (self.void_pos[0] + 1, self.void_pos[1])
        self.swap_with_void(up_to_void_pos)

    def go_left(self):
        # move eveything to the left most
        for x in range(0,4):
            zero_pos = 0
            for y in range(0,4):
                if self.tiles[x][y]==0:
                    zero_pos += 1
                else:
                    new_val = self.tiles[x][y]
                    old_val = self.tiles[x][y - zero_pos]
                    self.tiles[x][y-zero_pos] = new_val
                    self.tiles[x][y] = old_val
            print(self.tiles[x])
        print('<<end move>>')
        # for x in range(0,4):
        #     y_start = 0
        #     for y in range(1,3):
        #         if self.tiles[x][y_start] > 0 and self.tiles[x][y]==self.tiles[x][y_start]:
        #             sum_val = self.tiles[x][y_start]+self.tiles[x][y]
        #             self.tiles[x][y_start] = sum_val
        #             self.tiles[x][y] = 0
        #         elif self.tiles[x][y] != 0 and self.tiles[x][y]==self.tiles[x][y+1]:
        #             self.tiles[x][y] = sum_val
        #             self.tiles[x][y+1] = 0
        for x in range(0,4):
            for y in range(0,4):
                if self.tiles[x][y] > 0:
                    if self.tiles[x][y] == self.tiles[x][y+1]:
                        sum_val = self.tiles[x][y] + self.tiles[x][y+1]
                        self.tiles[x][y] = sum_val
                        self.tiles[x][y+1] = 0
        # for row in range (0,4):
        #     row_start = 0
        #     check_position = [0,2]
        #     for position in check_position:
        #         if self.tiles[row][position] > 0:
        #             if self.tiles[row][position] == self.tiles[row][position+1]:
        #                 sumval = self.tiles[row][position] + self.tiles[row][position+1]
        #                 self.tiles[row][position] = sumval
        #                 self.tiles[row][position+1] = 0
        print('<<end sum>>')
        for x in range(0,4):
            zero_pos = 0
            for y in range(0,4):
                if self.tiles[x][y]==0:
                    zero_pos += 1
                else:
                    new_val = self.tiles[x][y]
                    old_val = self.tiles[x][y - zero_pos]
                    self.tiles[x][y-zero_pos] = new_val
                    self.tiles[x][y] = old_val
            print(self.tiles[x])
        print('<<end move2>>')
        self.draw_tiles()

    def go_right(self):
        # move eveything to the left most
        for x in range(0, 4):
            zero_pos = 0
            reverse_val = 3
            while(reverse_val>-1):
                if self.tiles[x][reverse_val] == 0:
                    zero_pos -= 1
                else:
                    new_val = self.tiles[x][reverse_val]
                    old_val = self.tiles[x][reverse_val + zero_pos]
                    self.tiles[x][reverse_val + zero_pos] = new_val
                    self.tiles[x][reverse_val] = old_val
                reverse_val -= 1
            print(self.tiles[x])
        print('<<end move>>')

    def swap_with_void(self, up_to_void_pos):
        x1, y1 = up_to_void_pos
        x2, y2 = self.void_pos
        self.tiles[x2][y2], self.tiles[x1][y1] = self.tiles[x1][y1], self.tiles[x2][y2]
        self.draw_tiles()
        self.void_pos = up_to_void_pos
        self.screen.update()
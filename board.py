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
            [2, 2, 0, 1],
            [2, 2, 0, 0],
            [2, 2, 0, 0],
            # [2, 2, 2, 3],
            [2, 2, 2, 4]
            # [1, 2, 3, 4]
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
        for column in range (0,4):
            for position in range(0,3):
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
        self.draw_tiles()



    def go_down(self):
        for column in range(0, 4):
            zero_pos = 0
            row = 3
            while row > -1:
                if self.tiles[row][column] == 0:
                    zero_pos += 1
                else:
                    new_val = self.tiles[row][column]
                    old_val = self.tiles[row + zero_pos][column]
                    self.tiles[row + zero_pos][column] = new_val
                    self.tiles[row][column] = old_val
                row -= 1
            row = 3
            while row > 0:
                if self.tiles[row][column] > 0:
                    if self.tiles[row][column] == self.tiles[row-1][column]:
                        sumval = self.tiles[row][column] + self.tiles[row-1][column]
                        self.tiles[row][column] = sumval
                        self.tiles[row - 1][column] = 0
                row -= 1
            zero_pos = 0
            row = 3
            while row > -1:
                if self.tiles[row][column] == 0:
                    zero_pos += 1
                else:
                    new_val = self.tiles[row][column]
                    old_val = self.tiles[row + zero_pos][column]
                    self.tiles[row + zero_pos][column] = new_val
                    self.tiles[row][column] = old_val
                row -= 1
            row = 3
        self.draw_tiles()

    def go_left(self):
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
        for x in range(0,4):
            for y in range(0,3):
                if self.tiles[x][y] > 0:
                    if self.tiles[x][y] == self.tiles[x][y+1]:
                        sum_val = self.tiles[x][y] + self.tiles[x][y+1]
                        self.tiles[x][y] = sum_val
                        self.tiles[x][y+1] = 0
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
        self.draw_tiles()

    def go_right(self):
        for x in range(0, 4):
            reverselist = self.tiles[x]
            reverselist = reverselist[::-1]
            zero_pos = 0
            for y in range(0, 4):
                if reverselist[y] == 0:
                    zero_pos += 1
                else:
                    new_val = reverselist[y]
                    old_val = reverselist[y - zero_pos]
                    reverselist[y - zero_pos] = new_val
                    reverselist[y] = old_val
            for y in range(0, 4):
                if reverselist[y] > 0:
                    if reverselist[y] == reverselist[y + 1]:
                        sum_val = reverselist[y] + reverselist[y + 1]
                        reverselist[y] = sum_val
                        reverselist[y + 1] = 0
            for y in range(0, 4):
                if reverselist[y] == 0:
                    zero_pos += 1
                else:
                    new_val = reverselist[y]
                    old_val = reverselist[y - zero_pos]
                    reverselist[y - zero_pos] = new_val
                    reverselist[y] = old_val
            reverselist = reverselist[::-1]
            self.tiles[x] = reverselist
        self.draw_tiles()

    def swap_with_void(self, up_to_void_pos):
        x1, y1 = up_to_void_pos
        x2, y2 = self.void_pos
        self.tiles[x2][y2], self.tiles[x1][y1] = self.tiles[x1][y1], self.tiles[x2][y2]
        self.draw_tiles()
        self.void_pos = up_to_void_pos
        self.screen.update()
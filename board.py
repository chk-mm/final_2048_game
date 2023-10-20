from turtle import Turtle
from random import Random
FONT = ('verdana', 30, 'normal')
STARTING_X = -120
STARTING_Y = 100
SPACE = 80
IS_MOVE_COLUMN = True


class Board():

    def __init__(self, screen):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.goto(STARTING_X, STARTING_Y)
        self.screen = screen
        self.tiles = [
            [2, 0, 2, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
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

    def compare_is_move(self):
        tmp_compare = []
        for i in range(0,4):
            tmp1 = []
            for j in range(0,4):
                tmp1.append(self.tiles[i][j])
            tmp_compare.append(tmp1)
        return tmp_compare


    def go_up(self):
        IS_MOVE = True
        tmp_compare = self.compare_is_move()
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
                        IS_MOVE = False
                        self.random_spawn()
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
        if tmp_compare != self.tiles and IS_MOVE:
            self.random_spawn()
        self.draw_tiles()



    def go_down(self):
        IS_MOVE = True
        tmp_compare = self.compare_is_move()
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
                        self.random_spawn()
                        IS_MOVE = False
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
        if tmp_compare != self.tiles and IS_MOVE:
            self.random_spawn()
        self.draw_tiles()

    def go_left(self):
        IS_MOVE = True
        tmp_compare = self.compare_is_move()
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
                        self.random_spawn()
                        IS_MOVE = False
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
        if tmp_compare != self.tiles and IS_MOVE:
            self.random_spawn()
        self.draw_tiles()

    def go_right(self):
        IS_MOVE = True
        tmp_compare = self.compare_is_move()
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
            for y in range(0, 3):
                if reverselist[y] > 0:
                    if reverselist[y] == reverselist[y + 1]:
                        sum_val = reverselist[y] + reverselist[y + 1]
                        reverselist[y] = sum_val
                        reverselist[y + 1] = 0
                        self.random_spawn()
                        IS_MOVE = False
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
        if tmp_compare != self.tiles and IS_MOVE:
            self.random_spawn()
        self.draw_tiles()

    def random_spawn(self):
        random = Random()
        while True:
            c = random.randint(0,3)
            r = random.randint(0,3)
            if self.tiles[r][c] == 0:
                self.tiles[r][c] = 2
                break
import time

from random import choice
from typing import Dict, Tuple

from square import Square

class Field:
    def __init__(self, dim_x, dim_y):
        self.squares: Dict[Tuple[int, int], Square] = {}

        self.dim_x = dim_x
        self.dim_y = dim_y

        self.__initializeSquares()

    def __initializeSquares(self):
        for x in range(self.dim_x):
            for y in range(self.dim_y):
                self.squares[x, y] = Square(
                    x,
                    y,
                    False,
                    (
                        True if x == 0 else False,
                        True if x == self.dim_x - 1 else False,
                        True if y == 0 else False,
                        True if y == self.dim_y - 1 else False,
                    )
                )

    def __neighborsAlive(self, pos_x, pos_y):
        if not (0 <= pos_x < self.dim_x and 0 <= pos_y < self.dim_y):
            print(pos_x, pos_y)
            raise Exception("invalid coordinates!")

        cells_alive = 0

        for i in self.squares[pos_x, pos_y].neighbors:
            if self.squares[pos_x + i[0], pos_y + i[1]].alive:
                cells_alive += 1

        return cells_alive

    def step(self):

        for x in range(self.dim_x):
            for y in range(self.dim_y):
                neighbors_alive = self.__neighborsAlive(x, y)
                temp_square = self.squares[x, y]
                if neighbors_alive < 2:
                    temp_square.prepareChange(False)
                elif neighbors_alive in [2, 3] and temp_square.alive:
                    temp_square.prepareChange(True)
                elif neighbors_alive > 3:
                    temp_square.prepareChange(False)
                elif neighbors_alive == 3 and not temp_square.alive:
                    temp_square.prepareChange(True)
                else:
                    temp_square.prepareChange(temp_square.alive)

        for x in range(self.dim_x):
            for y in range(self.dim_y):
                self.squares[x, y].commitChange()

#[' ', '░', '▒', '▓', '█']

    def __str__(self):
        master = []

        for x in range(self.dim_x):
            row = []
            for y in range(self.dim_y):
                row.append(str(self.squares[x, y]))
            master.append("".join(row))

        # for x in range(self.dim_x):
        #     row = []
        #     for y in range(self.dim_y):
        #         row.append(str(self.__neighborsAlive(x, y)))
        #     master.append(" ".join(row))
        master.append("\033[F" * (self.dim_y + 1))

        return "\n".join(master)

a = Field(50, 50)
asd = open("field.txt", "r").read().split("\n")

print(asd)
# quit()

for y in range(len(asd)):
    for x in range(len(asd[y])):
        # print(x, y)
        temp = asd[y][x]

        square = a.squares[x, y]
        if not temp == " ":
            square.alive = True
        else:
            square.alive = False

# a.squares[1, 1].alive = True
# a.squares[1, 2].alive = True

# print(a)
# quit()

while True:
    print(a)
    # print(a.dim_x, a.dim_y)
    a.step()
    input()
    time.sleep(.1)
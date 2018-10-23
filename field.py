from random import choice

from square import Square

class Field:
    def __init__(self, dim_x, dim_y):
        self.squares = {}

        self.dim_x = dim_x
        self.dim_y = dim_y

        self.__initializeSquares()

    def __initializeSquares(self):
        for x in range(self.dim_x):
            for y in range(self.dim_y):
                self.squares[x, y] = Square(
                    x,
                    y,
                    choice([True, False]),
                    (
                        True if x == 0 else False,
                        True if x == self.dim_x - 1 else False,
                        True if y == 0 else False,
                        True if y == self.dim_y - 1 else False,
                    )
                )


    def __str__(self):
        master = []
        for x in range(self.dim_x):
            row = []
            for y in range(self.dim_y):
                row.append(str(self.squares[x, y]))
            master.append(" ".join(row))

        return "\n".join(master)

a = Field(10, 10)
print(a)
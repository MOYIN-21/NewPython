class Board:
    def __init__(self, name: str):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.__name = name

    def display(self):
        print(" %s | %s | %s |" % (self.cells[0], self.cells[1], self.cells[2]))
        print("_______________")
        print(" %s | %s | %s |" % (self.cells[3], self.cells[4], self.cells[5]))
        print("_______________")
        print(" %s | %s | %s |" "" % (self.cells[6], self.cells[7], self.cells[8]))

    def check_winner(self, x, y, player):
        if self.cells[0][x] == player and self.cells[1][x] == player and self.cells[2][x] == player:
            return True
        elif self.cells[y][0] == player and self.cells[y][1] == player and self.cells[y][2] == player:
            return True
        elif self.cells[0][2] == player and self.cells[1][1] == player and self.cells[2][0] == player:
            return True
        elif self.cells[0][0] == player and self.cells[1][1] == player and self.cells[2][2] == player:
            return True
        else:
            return False

    def check_if_board_is_full(self):
        for row in self.cells:
            for col in row:
                if col is None:
                    return False
            return True


board = Board("name")
board.display()

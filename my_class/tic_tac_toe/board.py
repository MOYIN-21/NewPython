class Board:
    def __init__(self, name: str):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.__name = name

    def display(self):
        print(" %s | %s | %s |" % (self.cells[0], self.cells[1], self.cells[2]))
        print("_______________")
        print(" %s | %s | %s |" % (self.cells[3], self.cells[4], self.cells[5]))
        print("_______________")
        print(" %s | %s | %s |" ""% (self.cells[6], self.cells[7], self.cells[8]))

    def register_player(self, name):
        if name!= 3:
        return name + 1


board = Board("name")
board.display()

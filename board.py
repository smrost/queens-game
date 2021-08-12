#creating a blueprint/object representing a chess board
class Board:
    #creating two physical attributes: size and array of pieces types
    def __init__(self, size): #passing a SIZE here
        self.n = size
        self.pieces = set() #pieces attribute equal to "set" to store different types of pieces
        # Sets are used to store multiple items in a single variable.
        #(i=0, i<pieces.length, i++) loop until i becomes as large as array length (which means through the whole array)
        #for other in pieces
        # pieces = [Queen, Queen, Queen, Queen, Queen, Queen, Queen, Queen]
        #Queen != 

    def size(self):
        return self.n #return the size number passed to board

    # create a check if the piece attacks another piece
    def admissiblePlacementFor(self, piece): #passing a PIECE here
        for other in self.pieces: #loop for every piece in pieces and calls the current one "other"
            if ((other != piece) #if other piece is different to current piece
                and other.attacks(piece) #and other piece attacks current piece
                or piece.attacks(other)): #or current piece attacks other piece
                    return False
        return True

    def add(self, piece): #function allowing us to add pieces to the set (set is empty at start)
        self.pieces.add(piece)

    def remove(self, piece): #function allowing us to remove pieces from the set
        self.pieces.remove(piece)



#Create a board
    # 1. allow us to set the size of the board
    # 2. create a set/array of the chess figures that would be added
    # 3. make a way to check if chess figures can cross/kill other chess figures
    # 4. make a way to add a chess figure to the board
    # 5. make a way to remove a chess figure to the board
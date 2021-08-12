class Piece:
    def __init__(self):
        self.board = None
        self.i = None #row
        self.j = None #column

    def isOnBoard(self): #checks if piece is on the board
        return self.board != None 

    def placeOn(self, board, i, j): #this places the piece on the board
        if (not self.isOnBoard()
            and (0 <= i)
            and (i < board.size())
            and (0 <= j)
            and (j < board.size()) ):
                self.board = board;
                self.i = i;
                self.j = j;
                board.add( self );

    def removeFromBoard(self): #this removes piece from the board
        if (self.isOnBoard()):
            self.board.remove(self)
            self.board = None

    def attacks(self, piece): #?????
        raise Exception("An abstract method has been invoked")

    def isMindfulOf(self, piece):
        return ((piece!=None)
                and self.isOnBoard()
                and piece.isOnBoard()
                and self.board == piece.board #board of same and board of piece should be the same
                and self != piece) #self and piece should be different
    
    def rowIndex(self): #create its rox index (of the piece)
        if (self.isOnBoard()):
            return self.i
        else:
            return self.UNKNOWN
    
    def colIndex(self): #create column index of the piece
        if (self.isOnBoard()):
            return self.j;
        else:
            return self.UNKNOWN

    UNKNOWN = -1


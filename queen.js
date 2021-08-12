// from piece import Piece

// class Queen(Piece):
//     def __init__(self):
//         Piece.__init__(self)

//     def attacks(self, piece): 
//         i = self.rowIndex()
//         j = self.colIndex()

//         u = piece.rowIndex()
//         v = piece.colIndex()

//         return (
//             self.isMindfulOf(piece)
//             and ((i == u)
//                 or (j == v) 
//                 or (i-j == u-v)
//                 or (i+j == u+v)) )




import Piece from piece;

class Queen extends Piece{
    constructor(self){
        Piece.self; //not sure about this
    }

    attacks(self,piece){
        i = self.rowIndex()
        j = self.colIndex()

        u = piece.rowIndex()
        v = piece.colIndex()

    return (
        self.isMindfulOf(piece)
        && (i==u) 
        || (j==v)
        || (i-j == u-v)
        || (i+j == u+v)
    )
    }


}
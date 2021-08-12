class board {
    constructor(this) {
        this.n = size;
        this.pieces = new Set();
    function size(this) {
        return this.n;
    }
  }
}

function admissiblePlacementFor(piece) {
    for (let other in this.pieces) {
        if (other != piece
           && other.attacks(piece) 
           || piece.attacks(other)) {
               return false;
           }

    }
    return true;
}

function add(piece) {
    this.pieces.add(piece);
}

function remove(piece) {
    this.pieces.remove(piece);
}


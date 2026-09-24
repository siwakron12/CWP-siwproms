def checkmate(board):

    rows = board.splitlines()

    if not rows:
        return

    size = len(rows)
    for row in rows:
        if len(row) != size:
            print("error")
            return

  
    king_row = -1
    king_col = -1
    king_count = 0

    for r in range(size):
        for c in range(size):
            if rows[r][c] == "K":
                king_row = r
                king_col = c
                king_count += 1

    if king_count != 1:
        return

    pawn_row = king_row + 1
    if pawn_row < size:
        if king_col - 1 >= 0:
            if rows[pawn_row][king_col - 1] == "P":
                print("Success")
                return

        if king_col + 1 < size:
            if rows[pawn_row][king_col + 1] == "P":
                print("Success")
                return

   
 #  ตรวจ Rook / Queen
   
    straight_directions = [
        (-1, 0),  # บน
        (1, 0),   # ล่าง
        (0, -1),  # ซ้าย
        (0, 1)    # ขวา
    ]

    for dr, dc in straight_directions:
        r = king_row + dr
        c = king_col + dc

        while 0 <= r < size and 0 <= c < size:

            piece = rows[r][c]

            if piece in "PBRQK":

                if piece == "R" or piece == "Q":
                    print("Success")
                    return

         
                break

            r += dr
            c += dc


#  ตรวจ Bishop / Queen

    diagonal_directions = [
        (-1, -1),  # บนซ้าย
        (-1, 1),   # บนขวา
        (1, -1),   # ล่างซ้าย
        (1, 1)     # ล่างขวา
    ]

    for dr, dc in diagonal_directions:
        r = king_row + dr
        c = king_col + dc

        while 0 <= r < size and 0 <= c < size:

            piece = rows[r][c]

            if piece in "PBRQK":

                if piece == "B" or piece == "Q":
                    print("Success")
                    return

                break

            r += dr
            c += dc

    print("Fail")
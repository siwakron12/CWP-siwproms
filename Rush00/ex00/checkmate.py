def checkmate(board: str):
    # 1. แปลง string เป็น list ของแต่ละบรรทัด
    lines = [line for line in board.strip().split('\n') if line]
    if not lines:
        return

    n = len(lines)
    
    # 2. หาตำแหน่ง King (K)
    king_pos = None
    for r in range(n):
        for c in range(len(lines[r])):
            if lines[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break

    # ถ้าไม่มี King อยู่บนกระดาน
    if not king_pos:
        return

    kr, kc = king_pos

    # 3. ฟังก์ชันช่วยเช็กว่าพิกัดอยู่ในกระดานหรือไม่
    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < len(lines[r])

    # 4. เช็กทิศทางต่างๆ
    # ตัวอย่าง: เช็กทิศทางตรง (สำหรับ Rook 'R' และ Queen 'Q')
    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_directions:
        r, c = kr + dr, kc + dc
        while is_valid(r, c):
            piece = lines[r][c]
            if piece in ('.', ' '): # ถ้าเป็นช่องว่าง ให้เดินต่อ
                r += dr
                c += dc
                continue
            if piece in ('R', 'Q'): # เจอตัวรุก
                print("Success")
                return
            else: # เจอตัวหมากอื่นบังทาง
                break

    # TODO: เพิ่มการเช็กทิศทางเฉียงสำหรับ Bishop ('B') และ Queen ('Q')
    # diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # TODO: เพิ่มการเช็ก Pawn ('P') ในระยะประชิดแนวเฉียง

    # ถ้าเช็กครบทุกทิศแล้วไม่เจอตัวรุก
    print("Fail")
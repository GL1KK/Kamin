import logging

COMB_WIN = ((0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 4, 8),
            (2, 4, 6),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8))

logging.basicConfig(filename="log.txt", level=logging.DEBUG, encoding="utf8")


def draw_desk():
    print(f"{desk[0]} | {desk[1]} | {desk[2]}")
    print("---------")
    print(f"{desk[3]} | {desk[4]} | {desk[5]}")
    print("---------")
    print(f"{desk[6]} | {desk[7]} | {desk[8]}")


def input_data():
    def check_correct_data(data):
        try:
            if 1 <= int(data) <= 9:
                if desk[int(data)-1] not in ("x", "o"):
                    logging.debug(f"Ход {data} принят!")
                    return True
            logging.debug(f"Ход {data} не принят!")
            return False
        except:
            logging.debug("Нас пытались сломать!")
            return False

    if c_s % 2 == 0:
        data = input("Ваш ход: ")
        while not check_correct_data(data):
            print("Некорректный ход, попробуйте еще раз")
            data = input("Ваш ход: ")
        desk[int(data)-1] = "x"
    else:
        for x, y, z in COMB_WIN:
            line = [desk[x], desk[y], desk[z]]
            if line.count("o") == 2 and line.count("x") == 0:
                for pos in (x, y, z):
                    if desk[pos] not in ("x", "o"):
                        desk[pos] = "o"
                        print(f"Бот выигрывает, ход на {pos + 1}!")
                        logging.debug(f"Бот выигрывает, ход на {pos + 1}!")
                        return
        
        for x, y, z in COMB_WIN:
            line = [desk[x], desk[y], desk[z]]
            if line.count("x") == 2 and line.count("o") == 0:
                for pos in (x, y, z):
                    if desk[pos] not in ("x", "o"):
                        desk[pos] = "o"
                        print(f"Бот блокирует игрока, ход на {pos + 1}!")
                        logging.debug(f"Бот блокирует игрока, ход на {pos + 1}!")
                        return
        
        if desk[4] not in ("x", "o"):
            desk[4] = "o"
            print(f"Бот ходит в центр, ход на 5!")
            return
        
        for i, cell in enumerate(desk):
            if cell not in ("x", "o"):
                desk[i] = "o"
                print(f"Бот сходил на {i+1}")
                return


def check_win():
    for x, y, z in COMB_WIN:
        if desk[x] == desk[y] == desk[z]:
            winner = "Игрок" if desk[x] == "x" else "Бот"
            print(f"Победа {winner.lower()}а!")
            return desk[x]


def main():
    global desk, c_m_x, c_m_o, c_s
    c_m_x = c_m_o = 0
    c_s = 0
    desk = [i for i in range(1, 10)]
    for i in range(9):
        draw_desk()
        input_data()
        if c_s >= 3:
            if c_m_o >= 3 or c_m_x >= 3:
                print(f"Максимальное количество ошибок у {'o' if c_s % 2 == 1 else 'x'}")
            if check_win():
                draw_desk()
                break
        c_s += 1
    else:
        print("НИЧЬЯ")
        draw_desk()


main()
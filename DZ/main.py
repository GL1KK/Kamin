import logging

# Настройка логгеров
logger_info = logging.getLogger("info_logger")
logger_info.setLevel(logging.INFO)
info_handler = logging.FileHandler("info_log.txt")
logger_info.addHandler(info_handler)

logger_debug = logging.getLogger("debug_logger")
logger_debug.setLevel(logging.DEBUG)
debug_handler = logging.FileHandler("debug_log.txt")
logger_debug.addHandler(debug_handler)

def draw_desk():
    print(f"{desk[0]} | {desk[1]} | {desk[2]}")
    print("---------")
    print(desk[3], "|", desk[4], "|", desk[5])
    print("---------")
    print(f"{desk[6]} | {desk[7]} | {desk[8]}")
    logger_info.info("Игровое поле отображено")

def input_data():
    def check_correct_data():
        try:
            if 1 <= int(data) <= 9:
                if int(data) in desk:
                    logger_debug.debug(f"Ход {data} принят!")
                    logger_info.info(f"Совершен ход: {data}")
                    return True
            logger_debug.debug(f"Ход {data} не принят!")
            return False
        except:
            logger_debug.debug("Нас пытались сломать!")
    data = input("Ваш ход: ")
    if check_correct_data():
        global desk
        desk[int(data) - 1] = "o" if c_s % 2 else "x"

def main():
    global desk, c_m_x, c_m_o, c_s
    c_m_x = c_m_o = 0
    c_s = 0
    desk = [i for i in range(1, 10)]
    logger_info.info("Игра начата") 
    for i in range(9):
        draw_desk()
        input_data()
        c_s += 1
    logger_info.info("Игра завершена") 

main()
import platformm
import pygame

FILE = "/home/daniil/Projects/Python/KAMIN/mario_gift/levels/1.txt"
BG_FILE = "/home/daniil/Projects/Python/KAMIN/mario_gift/images/bg.gif"


class Level:
    path_level: str

    def __init__(self, path=FILE, bg=BG_FILE):
        self.path_level = path
        self.bg = pygame.image.load(bg)

        self.__get_platform(self.__load())

    def __load(self):
        # TODO: реализовать метод загрузки из файла
        return [i for i in open(self.path_level)]

    def __get_platform(self, info_map):
        # TODO: реализовать метод который будет отдавать объекты платформы
        self.r_w = len(max(info_map))*platformm.PLATFORM_WIDTH
        self.r_h = len(info_map)*platformm.PLATFORM_HEIGHT
        self.plts = []
        y = 0
        for row in info_map:
            x = 0
            for symbol in row:
                if symbol == "-":
                    self.plts.append(platformm.Platform(x, y))
                x += platformm.PLATFORM_WIDTH
            y += platformm.PLATFORM_HEIGHT

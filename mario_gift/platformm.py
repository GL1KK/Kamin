import pygame

PLATFORM_WIDTH = 32  # Ширина прямоугольника
PLATFORM_HEIGHT = 32  # Высота
PLATFORM_COLOR = "#006262"  # Цвет прямоугольника


class Platform(pygame.sprite.Sprite):
    # TODO: реализовать класс для платформ

    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH,
                                     PLATFORM_HEIGHT))
        #self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.image = pygame.image.load("images/platform.png")
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

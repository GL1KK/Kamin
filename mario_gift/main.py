import pygame
import player
import level
import camera

# Объявляем переменные
# TODO: продумать необходимые константы


def main():
    # TODO: реализовать работу приложения
    pygame.init()
    pygame.mixer.music.load("music/super-mario-saundtrek.mp3")
    pygame.mixer.music.play(-1)
    window = pygame.display.set_mode(camera.DISPLAY)
    pygame.display.set_caption("☺А-ЛЯ ИГРА МАРИО☻")
    lvl = level.Level()
    obj_for_draw = pygame.sprite.Group()
    for obj in lvl.plts:
        obj_for_draw.add(obj)
    hero = player.Player(155, 55)
    obj_for_draw.add(hero)
    timer = pygame.time.Clock()
    while True:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit(123)
            hero.move(event)
        window.blit(lvl.bg, (0, 0))
        hero.update(lvl.plts)
        obj_for_draw.draw(window)
        pygame.display.update()


if __name__ == "__main__":
    main()

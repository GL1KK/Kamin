import pygame
import pyganim

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#000000"
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
DELAY = 1
ANIM_RIGHT = [("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/r1.png", DELAY),
              ("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/r2.png", DELAY),
              ("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/r3.png", DELAY),
              ("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/r4.png", DELAY),
              ("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/r5.png", DELAY)]

ANIM_LEFT = [("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/l1.png", DELAY),
             ("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/l2.png", DELAY),
             ("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/l3.png", DELAY),
             ("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/l4.png", DELAY),
             ("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/l5.png", DELAY)]

ANIM_STAY = [("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/0.png", DELAY)]
ANIM_JUMP_RIGHT = [("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/jr.png", DELAY)]
ANIM_JUMP_LEFT = [("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/jl.png", DELAY)]
ANIM_JUMP = [("/home/daniil/Projects/Python/KAMIN/mario_gift/images/hero/j.png", DELAY)]


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.left = False
        self.right = False
        self.up = False
        self.onGround = False
        self.image.set_colorkey(pygame.Color(COLOR))
        
        self.anim_stay = pyganim.PygAnimation(ANIM_STAY)
        self.anim_stay.play()
        
        self.anim_left = pyganim.PygAnimation(ANIM_LEFT)
        self.anim_left.play()
        
        self.anim_right = pyganim.PygAnimation(ANIM_RIGHT)
        self.anim_right.play()
        
        self.anim_jump_right = pyganim.PygAnimation(ANIM_JUMP_RIGHT)
        self.anim_jump_right.play()
        
        self.anim_jump_left = pyganim.PygAnimation(ANIM_JUMP_LEFT)
        self.anim_jump_left.play()
        
        self.anim_jump = pyganim.PygAnimation(ANIM_JUMP)
        self.anim_jump.play()
        
        self.anim_stay.blit(self.image, (0, 0))

    def update(self, platforms):
        if self.left:
            self.xvel = -MOVE_SPEED
            self.image.fill(pygame.Color(COLOR))
            if not self.onGround:
                self.anim_jump_left.blit(self.image, (0, 0))
            else:
                self.anim_left.blit(self.image, (0, 0))
        elif self.right:
            self.xvel = MOVE_SPEED
            self.image.fill(pygame.Color(COLOR))
            if not self.onGround:
                self.anim_jump_right.blit(self.image, (0, 0))
            else:
                self.anim_right.blit(self.image, (0, 0))
        else:
            self.xvel = 0
            self.image.fill(pygame.Color(COLOR))
            if not self.onGround:
                self.anim_jump.blit(self.image, (0, 0))
            else:
                self.anim_stay.blit(self.image, (0, 0))

        if self.up:
            if self.onGround:
                self.yvel = -JUMP_POWER
                self.onGround = False
                self.image.fill(pygame.Color(COLOR))
                if self.right:
                    self.anim_jump_right.blit(self.image, (0, 0))
                elif self.left:
                    self.anim_jump_left.blit(self.image, (0, 0))
                else:
                    self.anim_jump.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0

    def move(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            self.right = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_d:
            self.right = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            self.left = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_a:
            self.left = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.up = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            self.up = False


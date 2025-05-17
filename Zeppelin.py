import pygame
import os
import sys
from random import randint

# Inisialisasi pygame
pygame.init()

# Ukuran layar
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zeppelin Game")

# Load image dari folder images/
def load_image(name):
    return pygame.image.load(os.path.join("images", name + ".png")).convert_alpha()

# Definisi Actor manual
class Actor:
    def __init__(self, image_name):
        self.pos = (0, 0)
        self.set_image(image_name)

    def set_image(self, name):
        self.image_name = name
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.x, self.y = self.pos

    def draw(self):
        self.rect.center = self.pos
        screen.blit(self.image, self.rect)

    @property
    def x(self):
        return self.pos[0]

    @x.setter
    def x(self, value):
        self.pos = (value, self.pos[1])

    @property
    def y(self):
        return self.pos[1]

    @y.setter
    def y(self, value):
        self.pos = (self.pos[0], value)

    @property
    def top(self):
        self.rect.center = self.pos
        return self.rect.top

    @property
    def bottom(self):
        self.rect.center = self.pos
        return self.rect.bottom

    @property
    def right(self):
        self.rect.center = self.pos
        return self.rect.right

    def collidepoint(self, x, y):
        self.rect.center = self.pos
        return self.rect.collidepoint(x, y)

# Aktor dan game state
zeppelin = Actor("zeppelin")
zeppelin.pos = 400, 300

enemy = Actor("enemy-up")
enemy.pos = randint(800, 1600), randint(10, 200)

cave = Actor("cave")
cave.pos = randint(800, 1600), 460

tree = Actor("tree")
tree.pos = randint(800, 1600), 450

enemy_up = True
up = False
game_over = False
score = 0
number_of_updates = 0

# Fungsi-fungsi
def draw():
    screen.blit(load_image("background"), (0, 0))
    if not game_over:
        zeppelin.draw()
        enemy.draw()
        cave.draw()
        tree.draw()
        font = pygame.font.SysFont(None, 40)
        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(score_text, (700, 5))
    else:
        font = pygame.font.SysFont(None, 50)
        lose_text = font.render("You lose: Score: " + str(score), True, (0, 0, 0))
        screen.blit(lose_text, (300, 250))

def on_mouse_down():
    global up
    up = True
    zeppelin.y -= 50

def on_mouse_up():
    global up
    up = False

def flap():
    global enemy_up
    if enemy_up:
        enemy.set_image("enemy-down")
        enemy_up = False
    else:
        enemy.set_image("enemy-up")
        enemy_up = True

def update():
    global game_over, score, number_of_updates
    if not game_over:
        if not up:
            zeppelin.y += 3

        if enemy.x > 0:
            enemy.x -= 4
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            enemy.x = randint(800, 1600)
            enemy.y = randint(10, 200)
            score += 1
            number_of_updates = 0

        if cave.right > 0:
            cave.x -= 2
        else:
            cave.x = randint(800, 1600)
            score += 1

        if tree.right > 0:
            tree.x -= 2
        else:
            tree.x = randint(800, 1600)
            score += 1

        if zeppelin.top < 0 or zeppelin.bottom > 560:
            game_over = True

        if (zeppelin.collidepoint(enemy.x, enemy.y) or
            zeppelin.collidepoint(cave.x, cave.y) or
            zeppelin.collidepoint(tree.x, tree.y)):
            game_over = True

# Loop utama
clock = pygame.time.Clock()
running = True

while running:
    update()
    draw()
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_down()
        elif event.type == pygame.MOUSEBUTTONUP:
            on_mouse_up()

pygame.quit()
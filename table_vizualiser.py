import math
import time

import pygame


def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Table Vizualiser")

    return screen


def draw(screen, modulo, table=2):
    points = {}

    font = pygame.font.SysFont("Fira Code", 15)

    text_modulo = font.render("Modulo : " + str(modulo), True, (249, 180, 64))
    text_table = font.render("Table : " + str(round(table, 2)), True, (249, 180, 64))

    screen.blit(text_modulo, (10, 10))
    screen.blit(text_table, (10, 30))

    for number in range(modulo):
        x = int(400 + 300 * math.cos(2 * math.pi * number / modulo))
        y = int(400 + 300 * math.sin(2 * math.pi * number / modulo))

        x_text = int(390 + 325 * math.cos(2 * math.pi * number / modulo))
        y_text = int(390 + 325 * math.sin(2 * math.pi * number / modulo))

        if number % (modulo / 20) == 0:
            text = font.render(str(number), True, (249, 180, 64))
            screen.blit(text, (x_text, y_text))

        points[number] = (x, y)

    for number in range(modulo):
        color = (21, 96, 98)
        start = points[number]
        end = (
            int(400 + 300 * math.cos(2 * math.pi * table * number / modulo)),
            int(400 + 300 * math.sin(2 * math.pi * table * number / modulo)),
        )
        pygame.draw.aaline(screen, color, start, end, 1)

    pygame.draw.circle(screen, (249, 180, 64), (400, 400), 301, 2)
    pygame.display.flip()


def animate(screen, modulo):
    table = 0

    while True:
        draw(screen, modulo, table)
        time.sleep(1 / modulo)
        table += 0.01

        screen.fill((2, 35, 35))


def main():
    modulo = 1000

    screen = init_pygame()

    animate(screen, modulo)

    while True or table < 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


if __name__ == "__main__":
    main()

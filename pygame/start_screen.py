#start_screen.py
import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
grey =(128,128,128)
FPS = 45


def draw_button(screen, rect, color, text):
    pygame.draw.rect(screen, color, rect)
    button_font = pygame.font.Font(None, 30)
    button_text = button_font.render(text, True, BLACK)
    text_rect = button_text.get_rect(center=rect.center)
    screen.blit(button_text, text_rect)


def show_start_screen(screen, clock, width, height):
    background_image = pygame.image.load("b2.jpeg").convert()
    background_image = pygame.transform.scale(background_image, (width, height))

    waiting = True
    while waiting:
        screen.blit(background_image, (0, 0))
        title_font = pygame.font.Font(None, 74)
        title_text = title_font.render("Balloon Pop", True, grey)
        screen.blit(title_text,
                    (width // 2 - title_text.get_width() // 2, height // 2 - title_text.get_height() // 2 - 100))

        start_button_rect = pygame.Rect(width // 2 - 150, height // 2 + 50, 300, 100)
        quit_button_rect = pygame.Rect(width // 2 - 150, height // 2 + 200, 300, 100)

        draw_button(screen, start_button_rect, RED, "Start Game")
        draw_button(screen, quit_button_rect, RED, "Quit")

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(pos):
                    waiting = False
                elif quit_button_rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
        clock.tick(FPS)

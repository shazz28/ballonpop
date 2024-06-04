#difficulty.py
import pygame
import sys
import cv2
import numpy as np

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
FPS = 45

def draw_button(screen, rect, color, text):
    pygame.draw.rect(screen, color, rect)
    button_font = pygame.font.Font(None, 48)
    button_text = button_font.render(text, True, BLACK)
    text_rect = button_text.get_rect(center=rect.center)
    screen.blit(button_text, text_rect)

def show_difficulty_screen(screen, clock, width, height):
    # Load the video
    cap = cv2.VideoCapture('v2.mp4')

    button_width, button_height = 200, 100
    button_top = height // 2 - 20

    easy_button_rect = pygame.Rect(width // 2 - button_width // 2, button_top - 125, button_width, button_height)
    normal_button_rect = pygame.Rect(width // 2 - button_width // 2, button_top + 10, button_width, button_height)
    hard_button_rect = pygame.Rect(width // 2 - button_width // 2, button_top + 150, button_width, button_height)
    quit_button_rect = pygame.Rect(width - 140, 20, 120, 50)  # Top right corner

    waiting = True
    while waiting:
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        frame = cv2.resize(frame, (width, height))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0, 0))

        title_font = pygame.font.Font(None, 74)
        title_text = title_font.render("Select Difficulty", True, GREY)
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 2 - title_text.get_height() // 2 - 210))

        draw_button(screen, easy_button_rect, RED, "Easy")
        draw_button(screen, normal_button_rect, RED, "Normal")
        draw_button(screen, hard_button_rect, RED, "Hard")
        draw_button(screen, quit_button_rect, GREY, "Quit")

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if easy_button_rect.collidepoint(pos):
                    cap.release()
                    return "easy"
                elif normal_button_rect.collidepoint(pos):
                    cap.release()
                    return "normal"
                elif hard_button_rect.collidepoint(pos):
                    cap.release()
                    return "hard"
                elif quit_button_rect.collidepoint(pos):
                    cap.release()
                    pygame.quit()
                    sys.exit()
        clock.tick(FPS)

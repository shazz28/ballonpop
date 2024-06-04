import pygame
import random
import sys
from start_screen import show_start_screen
from difficulty_screen import show_difficulty_screen

# Constants
WIDTH = 1080
HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 45

SPEEDS = {
    "easy": 4,
    "normal": 7,
    "hard": 15
}

class Balloon:
    def __init__(self, speed):
        self.images = [
            pygame.image.load("1.png"),
            pygame.image.load("2.png"),
            pygame.image.load("3.png")
        ]
        self.image = random.choice(self.images)
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), HEIGHT + self.rect.height // 2)
        self.speed = speed

    def move(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def draw_button(screen, rect, color, text):
    pygame.draw.rect(screen, color, rect)
    button_font = pygame.font.Font(None, 48)
    button_text = button_font.render(text, True, BLACK)
    text_rect = button_text.get_rect(center=rect.center)
    screen.blit(button_text, text_rect)

def show_menu(screen, clock):
    menu_font = pygame.font.Font(None, 74)
    menu_text = menu_font.render("Paused", True, BLACK)
    screen.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 2 - menu_text.get_height() // 2 - 150))

    resume_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)
    quit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 60, 200, 100)
    change_diff_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 170, 300, 100)

    draw_button(screen, resume_button_rect, RED, "Resume")
    draw_button(screen, quit_button_rect, RED, "Quit")
    draw_button(screen, change_diff_button_rect, RED, "Change Difficulty")

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if resume_button_rect.collidepoint(pos):
                    return "resume"
                elif quit_button_rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
                elif change_diff_button_rect.collidepoint(pos):
                    return "change_difficulty"

        clock.tick(FPS)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Balloon Pop")
    clock = pygame.time.Clock()

    while True:
        show_start_screen(screen, clock, WIDTH, HEIGHT)

        difficulty = show_difficulty_screen(screen, clock, WIDTH, HEIGHT)
        if difficulty == "back":
            continue

        balloon_speed = SPEEDS[difficulty]

        balloons = []
        score = 0
        font = pygame.font.Font(None, 36)

        menu_button_rect = pygame.Rect(WIDTH - 140, 20, 120, 50)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if menu_button_rect.collidepoint(pos):
                        action = show_menu(screen, clock)
                        if action == "resume":
                            continue
                        elif action == "change_difficulty":
                            difficulty = show_difficulty_screen(screen, clock, WIDTH, HEIGHT)
                            if difficulty == "back":
                                break  # Exit the inner loop and go to the start screen
                            balloon_speed = SPEEDS[difficulty]
                            balloons.clear()
                            score = 0
                            continue  # Resume the game with the new difficulty

                    balloon_clicked = False
                    for balloon in balloons:
                        if balloon.rect.collidepoint(pos):
                            balloons.remove(balloon)
                            score += 1
                            balloon_clicked = True
                            break
                    if not balloon_clicked:
                        score -= 1
            else:
                screen.fill(WHITE)

                if random.randint(0, 100) < 2:
                    balloons.append(Balloon(balloon_speed))

                for balloon in balloons:
                    balloon.move()
                    balloon.draw(screen)

                score_text = font.render("Score: {}".format(score), True, BLACK)
                screen.blit(score_text, (10, 10))

                draw_button(screen, menu_button_rect, RED, "Menu")

                pygame.display.flip()
                clock.tick(FPS)
                continue

            break  # Break the inner while loop if "change_difficulty" is clicked

if __name__ == "__main__":
    main()

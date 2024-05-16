import pygame
import random
import sys

# Constants
WIDTH = 1080
HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BALLOON_SPEED = 3
FPS = 45

class Balloon:
    def __init__(self):
        self.images = [
            pygame.image.load("1.png"),
            pygame.image.load("2.png"),
            pygame.image.load("3.png")
        ]
        self.image = random.choice(self.images)
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), HEIGHT + self.rect.height // 2)
        self.speed = BALLOON_SPEED

    def move(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Balloon pop")
    clock = pygame.time.Clock()

    balloons = []
    score = 0
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                balloon_clicked = False
                for balloon in balloons:
                    if balloon.rect.collidepoint(pos):
                        balloons.remove(balloon)
                        score += 1
                        balloon_clicked = True
                        break
                if not balloon_clicked:
                    score -= 1

        screen.fill(WHITE)

        if random.randint(0, 100) < 2:
            balloons.append(Balloon())

        for balloon in balloons:
            balloon.move()
            balloon.draw(screen)

        score_text = font.render("Score: {}".format(score), True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

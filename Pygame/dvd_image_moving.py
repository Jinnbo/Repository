# dvd_image_moving.py
# Create a rectangle that moves around the screen

# GOALS:
#   * Create a rectangle class
#       * size and position
#       * colour
#       * velocity x- and y- direction
#   * Draw a rectangle on the screen
#   * Move rectangle in x and y


import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WIDTH = 800
HEIGHT = 600
TITLE = "<DVD Screensaver>"


class Rectangle:
    def __init__(self, colour=WHITE):
        self.width, self.height = (150,80)
        self.x, self.y = (WIDTH/2, HEIGHT / 2)

        self.colour = colour

        self.vel_x = 3
        self.vel_y = 3

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.colour,
            [
                self.x,
                self.y,
                self.width,
                self.height
            ]
        )

    def update(self):
        """Updates the location of the block in space.

        Returns:
            None
        """
        self.x += self.vel_x
        self.y += self.vel_y

        # Keep it in the screen
        if self.x + self.width > WIDTH or self.x < 0:
            self.vel_x *= -1
        if self.y + self.height > HEIGHT or self.y < 0:
            self.vel_y *= -1

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    block_one = Rectangle((0,255,0))
    block_two = Rectangle()
    block_two.x, block_two.y = (
        random.randrange(0, WIDTH-block_two.width),
        random.randrange(0, HEIGHT-block_two.height)
    )

    block_one.vel_x, block_two.vel_y = (
        random.choice([-4,-3,3,4]),
        random.choice([-4, -3, 3, 4])

    )


    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        # Update the position of the block
        block_one.update()
        block_two.update()

        # ----- DRAW
        screen.fill(BLACK)

        block_one.draw(screen)
        block_two.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        block_one.colour = random.choice([RED,GREEN,BLUE])
        clock.tick(60)


    pygame.quit()


if __name__ == "__main__":
    main()
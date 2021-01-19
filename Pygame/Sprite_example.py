# sprite_example.py
# INtroduction to Sprite class

# Goals:
#   * introduce the Sprite class
#   * subclass the Sprite class (inheritance)
import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1920
HEIGHT = 1080
TITLE = "<Sprite Example>"
NUM_JEWELS = 75
NUM_ENEMY = 10


class Jewel(pygame.sprite.Sprite):
    def __init__(self):
        # Call the superclass constructor
        super().__init__()

        # Image
        self.image = pygame.Surface((35, 20))
        self.image.fill((100, 255, 100))

        # Rect is Rectangle (x,y, width, height)
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/link.png")

        self.rect = self.image.get_rect()

    def update(self):
        """ Changes the position of the player
        based on the mouse's position"""

        self.rect.center = pygame.mouse.get_pos()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x, self.y = (WIDTH / 2, HEIGHT / 2)



        self.image = pygame.image.load("./images/ganon2.png")
        self.image = pygame.transform.scale(self.image, (67, 86))

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Keep enemy in the screen

        if self.rect.x + self.rect.width > WIDTH or self.rect.x < 0:
            self.vel_x *= -1
        if self.rect.y + self.rect.height > HEIGHT or self.rect.y < 0:
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
    score = 0
    Enemy.vel_x = 10
    Enemy.vel_y = 10


    # Sprite group and sprite creation
    all_sprite_group = pygame.sprite.Group()
    jewels_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()

    # Jewel creation
    for i in range(NUM_JEWELS):
        jewel = Jewel()
        jewel.rect.x = random.randrange(WIDTH - jewel.rect.width)
        jewel.rect.y = random.randrange(HEIGHT - jewel.rect.height)
        all_sprite_group.add(jewel)
        jewels_group.add(jewel)

    enemy_list = []
    for i in range(NUM_ENEMY):
        enemy = Enemy()
        enemy_list.append(enemy)



    # Player creation
    player = Player()
    all_sprite_group.add(player)




    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprite_group.update()

        for enemy in enemy_list:
            enemy.update()


        # Player collides with a jewel
        jewels_collected = pygame.sprite.spritecollide(player, jewels_group, True)
        for jewel in jewels_collected:
            score += 1
            print(score)







        # ----- DRAW
        screen.fill(BLACK)
        all_sprite_group.draw(screen)


        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)



    pygame.quit()


if __name__ == "__main__":
    main()
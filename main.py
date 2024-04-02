import pygame
import constants
from character import Character
from weapon import Weapon

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")

# =========== Create clock for maintaining frame rate
clock = pygame.time.Clock()

# =========== Define player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# Helped function to scale image
def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

# Load weapon
bow_image = scale_img(pygame.image.load("assets/images/weapons/bow.png").convert_alpha(), constants.WEAPON_SCALE)
arrow_image = scale_img(pygame.image.load("assets/images/weapons/arrow.png").convert_alpha(), constants.WEAPON_SCALE)
# Load character images
mob_animations = []
mob_types = ["elf", "imp", "skeleton", "goblin", "muddy", "tiny_zombie", "big_demon"]


animation_types = ["idle","run"]
for mob in mob_types:
    animation_list = []
    for animation in animation_types:
        # Reset temporary list of images
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f"assets/images/characters/{mob}/{animation}/{i}.png").convert_alpha()
            img = scale_img(img, constants.SCALE)
            temp_list.append(img)
        animation_list.append(temp_list)
    mob_animations.append(animation_list)


# =========== Create Player
player = Character(100, 100, mob_animations, 0)
# Create player's weapon
bow = Weapon(bow_image, arrow_image)

# Create Sprite Groups

arrow_group = pygame.sprite.Group()


# =========== Main game loop
run = True
while run:
    # =========== Control frame rate
    clock.tick(constants.FPS)
    screen.fill(constants.BG)

    # =========== Calculate player movement
    dx = 0
    dy = 0
    if moving_right == True:
        dx = constants.SPEED
    if moving_left == True:
        dx = -constants.SPEED
    if moving_up == True:
        dy = -constants.SPEED
    if moving_down == True:
        dy = constants.SPEED

    # =========== Move Player
    player.move(dx, dy)

    # =========== Update Player
    player.update()
    arrow = bow.update(player)
    if arrow:
        arrow_group.add(arrow)
    for arrow in arrow_group:
        arrow.update()


    # =========== Draw player on screen
    player.draw(screen)
    bow.draw(screen)
    for arrow in arrow_group:
        arrow.draw(screen)
    # =========== Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # =========== Take keyboard presses        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_right = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moving_up = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                moving_down = True
    # =========== Keyup events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False
    pygame.display.update()

pygame.quit()            
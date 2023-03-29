import pygame

pygame.init()

screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My Game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

player_size = 20
player_x = screen_width // 2
player_y = screen_height - player_size
player_speed = 5
player_jump_height = 10
player_is_jumping = False
player_y_velocity = 0
player_jumps_remaining = 2

ground_y = screen_height - player_size
ground_height = screen_height // 2
ground_color = GREEN

sky_color = BLUE

clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
        if player_x < 0:
            player_x = 0

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
        if player_x > screen_width - player_size:
            player_x = screen_width - player_size

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if not player_is_jumping and player_jumps_remaining > 0:
            player_is_jumping = True
            player_jumps_remaining -= 1
            player_y_velocity = -player_jump_height

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        pass  # put any code here to handle the 's' key press

    player_y_velocity += 1
    player_y += player_y_velocity

    if player_y + player_size >= ground_y:
        player_y = ground_y - player_size
        player_y_velocity = 0
        player_is_jumping = False
        player_jumps_remaining = 2

    screen.fill(sky_color)

    pygame.draw.rect(screen, ground_color, (0, ground_y, screen_width, ground_height))

    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))

    pygame.display.update()

    clock.tick(60)

pygame.quit()

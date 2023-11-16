import pygame
import random

pygame.init()

# Screen dimensions
dis_width = 600
dis_height = 400

# Define the path to your font and image files
font_path = 'C:\\Users\\sunmo\\Downloads\\Roboto\\Roboto-Regular.ttf'
background_path = 'C:\\Users\\sunmo\\Downloads\\stars-1654074_1280.jpg'

# Load the custom font and background image
custom_font = pygame.font.Font(font_path, 35)  # Adjusted font size for fitting text
background_image = pygame.image.load(background_path)
background_image = pygame.transform.scale(background_image, (dis_width, dis_height))

# Set up display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by [OLUWADAMILARE SUNMOLA]')

snake_block = 10
snake_speed = 19

# Colors
# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
orange = (255, 165, 0)  # Updated RGB values for orange
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Rest of your code remains the same...


def score(score):
    value = custom_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, orange, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = custom_font.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0       
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.blit(background_image, [0, 0])
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()

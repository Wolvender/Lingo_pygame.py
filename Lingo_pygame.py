import pygame
import pygame_gui

# Settting the Game screen

pygame.init()

width, height = 765, 550


screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((width, height))

Other_font = pygame.font.SysFont("appel" ,170, italic=True,bold=True)
base_font = pygame.font.SysFont("inkfree",32,italic=True,bold=True)
user_text = ""


# text input player


# Background

bg = pygame.image.load("D:\img lingo\img lingo1.png")


base_color = (255, 255, 255)



# Rect and txt cords

input_rect1 = pygame.Rect(90, 1, 80, 98)


displayText = pygame.display.set_caption("Lingooo")

text = base_font.render("Guess the Word", True, (15, 15, 15))

textrect = text.get_rect()
textrect.center = ((750//2, 1050//2))



# Color for rectangle
color_active = pygame.Color("#66a5ca")
color_passive = pygame.Color("#76a5cc")

color = color_passive

active = False


# Game loop




run = True
while run:
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    screen.blit(text, textrect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect1.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode.upper()

   
                


    
    if active:
        color = color_active
    else:
        color = color_passive

    pygame.draw.rect(screen, color, input_rect1)

    
    text_surface = Other_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect1.x + 0, input_rect1.y + 0))
    input_rect1.w = max(100, text_surface.get_width() + 0)


    
    pygame.display.update()
    clock.tick(60)



# Running Game


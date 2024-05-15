import pygame
import sys

# Settting the Game screen


class Game:
    def __init__(self):
        pygame.init()
        self.width = 850
        self.height = 650

        self.rect_height = 750
        self.rect_width = 1050



        self.rect = pygame.Rect(106, 1, 1, 97)
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.fps = pygame.time.Clock()

        self.Other_font = pygame.font.SysFont("" ,150)
        self.base_font = pygame.font.SysFont("inkfree",32,italic=True,bold=True)

        self.user_text = ""
        self.tab_count = 0
        self.tab_max = 5


        # Background
        self.bg = pygame.image.load("D:\img lingo\img lingo2.jpg")

        # Rect and txt cords
        self.displayText = pygame.display.set_caption("Lingooo")

        self.text = self.base_font.render("Guess the Word", True, (15, 15, 15))
        self.textrect = self.text.get_rect(center=(self.rect_height // 2, self.rect_width // 2))

        # Color for rectangle
        self.color_active = pygame.Color("#66a5ca")
        self.color_passive = pygame.Color("#76a5cc")

        self.color = 255, 255, 255, 127

        self.active = False

                

# Game input    
    def Game_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_TAB and self.tab_count < self.tab_max:
                self.user_text += "\n"
                self.tab_count += 1
                print(self.tab_count)
                
            elif event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            elif event.type == pygame.K_UP:
                self.user_text - "\n"
            else:
                self.user_text += event.unicode.upper()
                        
        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 1)
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.text, self.textrect)

        self.text_surface = self.Other_font.render(self.user_text,  True, pygame.Color(255, 255, 255, 255))
        self.screen.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))
        self.rect.w = max(100, self.text_surface.get_width() + 10)

        pygame.display.update()
        self.fps.tick(60)



    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.Game_input(event)

            self.draw()
            self.fps.tick(60)

        pygame.quit()


if __name__ == '__main__':
    try:
        g = Game()
        g.run()
    except Exception as e:
        print("error occurd", e)
        pygame.quit()

# Running Game


from color import color
import pygame

class Screen:
    def __init__(self, width=800, height=600, back_color=color.back_color, font_type= "monospace", font_size=35, clock_tick=30):
        self.width = width
        self.height = height
        self.back_color = back_color
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont(font_type, font_size)
        self.clock = pygame.time.Clock()
        self.clock_tick = clock_tick

    def refresh_background(self):
        self.screen.fill(self.back_color)

    def draw_enemies(self, enemy_list):
        for enemy in enemy_list:
            enemy.draw(self.screen)

    def draw_player(self, player):
        player.draw(self.screen)

    def draw_score_label(self, score, color=color.yellow):
        text = "Score: " + str(score)
        label= self.font.render(text, 1, color)
        self.screen.blit(label, (self.width-200, self.height-40))
        
    def update_screen(self, enemy_list, player, score):
        self.refresh_background()
        self.draw_enemies(enemy_list)
        self.draw_player(player)
        self.draw_score_label(score)

        self.clock.tick(self.clock_tick)
        pygame.display.update()

from color import color
import pygame


class player:
    def __init__(self, x, y, size, color=color.Maroon):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def detect_collision(self, other):
        if (other.x >= self.x and other.x < (self.x + self.size)) or (self.x >= other.x and self.x < (other.x + other.size)): #Condition in terms of x where enemy/player can overlap or collide#Use parentheses just to ensure it's evaluated properly
            if (other.y >= self.y and other.y < (self.y + self.size)) or (self.y >= other.y and self.y < (other.y + self.size)): #Checks if there is x overlap then y overlap
                return True
        return False

class Enemy(player):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, color=color.Blue)

class zaytoven(player):
    def __init__(self, x, y):
        super().__init__(x, y, size=75, color=color.Blue)

class LargeEnemy(player):
    def __init__(self, x, y):
        super().__init__(x, y, size=100, color=color.Blue)

class HumanPlayer(player):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, color=color.Maroon)

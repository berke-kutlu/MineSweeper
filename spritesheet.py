import pygame

# Sprite Sheet Class
class SpriteSheet(object):
    def __init__(self, spritesheet):
        self.sheet = spritesheet

    # Get Sprite From Sprite Sheet
    def get_sprite(self, frame, width, height, scale=1):
        sprite = pygame.Surface((width, height)) # Create Sub Surface
        sprite.blit(self.sheet, (0, 0), ((frame * width), 0, width, height)) # Add a Sprite From Sprite Sheet
        sprite = pygame.transform.scale(sprite, (width * scale, height * scale)) # Scale The Sprite
        return sprite
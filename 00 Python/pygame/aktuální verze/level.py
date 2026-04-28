import pygame
import json
import game_object


class Level:
    def __init__(self, screen, background, level_data, sprite_groups):
        self.screen = screen
        self.background = background
        self.level_data = level_data
        self.sprite_groups = sprite_groups

        for object_type, group in self.sprite_groups.items():
            self.create_object(object_type, group)
    
   
    def create_object(self, object_type, group):
        with open(self.level_data, mode="r") as f:
            data = json.load(f)
        
        for entity in data["entities"][object_type]:
            x = entity["x"]
            y = entity["y"]
            w = entity["width"]
            h = entity["height"]
            class_name = getattr(game_object, object_type)
            object = class_name(x, y, w, h)
            group.add(object)

    def draw_objects(self):
        self.screen.blit(self.background, (0,0))

        for group in self.sprite_groups.values():
            group.draw(self.screen)

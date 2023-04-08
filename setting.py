import os
import pygame as pg

setting = {
    'w': 800,
    'h': 800,
    'title': 'Very good, super, superduper, megasuper game(Наверно😑)',
    'fps': 60,
}

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, 'media')

player_img = pg.image.load(os.path.join(media_folder, 'player.png'))
Obstacle_img = pg.image.load(os.path.join(media_folder, 'Obstacle_Gosha.png'))
background_img = pg.image.load(os.path.join(media_folder, 'Background.png'))
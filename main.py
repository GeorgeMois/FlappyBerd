from Obstacle import Obstacle
from Player import Player
from setting import *

pg.init()

screen = pg.display.set_mode((setting['w'], setting['h']))
pg.display.set_caption(setting['title'])

clock = pg.time.Clock()

obstacle_group = pg.sprite.Group()
all_sprite = pg.sprite.Group()

player = Player()
all_sprite.add(player)

font = pg.font.SysFont("Arial", 90)
score_surface = font.render ("0", True, (255, 255, 255))

def new_mobs():
    obstacle_bottom = Obstacle(setting["w"], 700)
    obstacle_top = Obstacle(setting["w"], 100)
    obstacle_group.add(obstacle_top, obstacle_bottom)
    all_sprite.add(obstacle_group)

SPAWN_SPRITE = pg.USEREVENT + 1
pg.time.set_timer(SPAWN_SPRITE, 1000  )

pg.time.set_timer(pg.USEREVENT, 1000 )

run = True
score = 0
while run:
    clock.tick(setting['fps'])
    pg.display.flip()
    screen.blit(background_img, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == SPAWN_SPRITE:
            new_mobs()
        if event.type == pg.USEREVENT:
            score_surface = font.render(f"{score}", True, "black ")
            score += 1


    if pg.sprite.spritecollide(player, obstacle_group, False, pg.sprite.collide_circle):
              run = False

    screen.blit(score_surface, (270, 20 ))

    all_sprite.update()

    all_sprite.draw(screen)
    pg.display.flip()

pg.quit()

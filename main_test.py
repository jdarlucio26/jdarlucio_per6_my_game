# File created by: Joshua Darlucio

# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/


'''
My goal is:
- create a fire and water Mob. If hit by a Mob will loose 50 points
- Every plat hit, earns 100 points
- Add more platforms
- Add a score to screen.Each jump to new platform equals 100 points

How to reach the goal:
- Get scoreboard. Associate the plats with a score
- Create a new Mob 

Reach Goal:
Have the player have only 3 lives and if the player falls onto a disappearing block and falls to the bottom
they loose a life. 

'''
# import libs
import pygame as pg
import os
# import settings 
from settings_test import *
from sprites_test import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file
class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)

        self.platforms.add(self.plat1)
        
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,6):
            m = Mob(20,20,(0, 117, 119))
            # f = MobF(15,20,(178, 34, 34))
            self.all_sprites.add(m)
            # self.all_sprites.add(f)
            self.enemies.add(m)
            # self.enemies.add(f)

        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()
        plathits = pg.sprite.spritecollide(self.player, self.enemies, False)
        if plathits:
            plathits[0].attached_now = True
            self.score += 10
            print(self.score)
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            self.player.standing = True
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0

    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        if self.player.standing:
            self.draw_text(self.score, 24, WHITE, WIDTH/2, HEIGHT/2)
        # is this a method or a function?
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)


# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()
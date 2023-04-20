# File created by: Joshua Darlucio

# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/


'''
My goal is:
- create a fire mob. Fire mob will make player lose points, if hit
- add scoreboard
How to reach the goal:
- Get scoreboard. Associate the Mobs with a score
- Create a new Mob 

Reach Goal:
Have the player have only 3 lives and if the player falls onto a disappearing block and falls to the bottom
they loose a life. 

'''
# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
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
        # starting a new game. Adding platforms, mobs, and players
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.fire = pg.sprite.Group()
        self.water = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (39,64,96), "normal")
        self.plat2 = Platform(WIDTH, 500, 0, HEIGHT-50, (39,64,96), "normal")
        # Creating the bottom platform
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        self.all_sprites.add(self.plat2)
        self.platforms.add(self.plat2)
        # Creating player/block
        self.all_sprites.add(self.player)
        # Creates the platforms listed in settins
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # Creates the different types of Mobs on screen
        for i in range(0,15):
            m = Mob(20,20,(0,200,255))
            self.all_sprites.add(m)
            self.water.add(m)
        for i in range(0,15):
            f = FireMob(24,24,(255,0,0))
            self.all_sprites.add(f)
            self.fire.add(f)
    # This allows the code to draw, updat, and use the keyboard to make the block move and draw text on screen
        self.run()
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    # This will allow the block to jump when the spacebar gets clicked on
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    # This will update the player by adding score when it touches the mob.
    def update(self):
        self.all_sprites.update()
        fhits = pg.sprite.spritecollide(self.player, self.fire, False)
        whits = pg.sprite.spritecollide(self.player, self.water, False)
        if fhits:
            self.score -= 0.5
        elif whits:
            self.score += 0.5
        # This determines what type of platform the block hits and what the platform will do
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
# This will draw the background and any other text (including score)
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_text("Red = Fire (Loose point); Blue = Water (Earn point)", 24, (251,252,255), 400, 560)
        self.draw_text(str(self.score), 24, WHITE, 400, 5)
        # is this a method or a function?
        pg.display.flip()
# This is to draw text on the screen.
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
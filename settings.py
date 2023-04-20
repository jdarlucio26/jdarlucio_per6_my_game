# Pygame box that shows screen.
WIDTH = 800
HEIGHT = 600
# Player acceleration, jump, gravity, and friction
PLAYER_ACC = 2
PLAYER_JUMP = 20
PLAYER_FRICTION = -0.5
PLAYER_GRAV = 0.8
# Mob acceleration, jump, gravity, and friction
MOB_ACC = 2
MOB_FRICTION = -0.5
# Colors for different things
BLACK = (0,0,0)
BLUE = (50,50,255)
RED = (255,50,50)
WHITE = (255, 255, 0)
GREEN = (0,255,0)
FPS = 60
RUNNING = True 
SCORE = 1
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (39,64,96), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (200,200,200), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (200,200,200), "disappearing "),
                 (350, 200, 100, 20, (200,200,200), "normal"),
                 (50, 100, 50, 20, (200,200,200), "normal"),
                 (400, 70, 60, 5, (200,200,200), "normal"),
                 (600, 70, 100, 20, (200,200,200), "normal"),
                 (550, 500, 50, 20, (200,200,200), "normal"),
                 (659, 375, 70, 17, (200,200,200), "normal"),
                 (575, 300, 60, 15, (200,200,200), "bouncey"),
                 (5, 370, 120, 10, (200,200,200), "bouncey"),
                 (WIDTH / 2 - 250, HEIGHT * 1/2 + 200, 75, 20, (200,200,200), "normal")]


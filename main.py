from ursina import *
from entities import *
from settings import *

class Core:
    def __init__(self):
        self.app = Ursina()
        self.load_assets()
        self.sky = Sky()
        self.hand = Hand()

    def load_assets(self):
        self.grass_texture = load_texture(grass_texture)
        self.stone_texture = load_texture(stone_texture)
        self.brick_texture = load_texture(brick_texture)
        self.dirt_texture  = load_texture(dirt_texture)
        self.sky_texture   = load_texture(sky_texture)
        self.arm_texture   = load_texture(arm_texture)
        self.punch_sound   = Audio(punch_sound, loop = False, autoplay = False)

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = Core()
    app.run()



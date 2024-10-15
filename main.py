from ursina import *
from entities import *

class Core:
    def __init__(self):
        self.app = Ursina()
        self.load_assets()
        self.sky = Sky(self.sky_texture)
        self.hand = Hand(self.arm_texture)

    def load_assets(self):
        self.grass_texture = load_texture('assets/grass_block.png')
        self.stone_texture = load_texture('assets/stone_block.png')
        self.brick_texture = load_texture('assets/brick_block.png')
        self.dirt_texture  = load_texture('assets/dirt_block.png')
        self.sky_texture   = load_texture('assets/skybox.png')
        self.arm_texture   = load_texture('assets/arm_texture.png')
        self.bedrock_texture = load_texture("assets/bedrock.png")
        self.punch_sound   = Audio('audio/punch_sound',loop = False, autoplay = False)


    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = Core()
    app.run()



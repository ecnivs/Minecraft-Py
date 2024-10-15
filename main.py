from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from settings import *

app = Ursina()

# load assets
grass_texture = load_texture(grass_texture)
stone_texture = load_texture(stone_texture)
brick_texture = load_texture(brick_texture)
dirt_texture = load_texture(dirt_texture)
sky_texture = load_texture(sky_texture)
arm_texture = load_texture(arm_texture)
punch_sound = Audio(punch_sound, loop = False, autoplay = False)

def update():
	global block_pick
	global tab

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

    # invisible wall
	if player.x < 0: player.x = 0
	if player.x > render_distance-1: player.x = render_distance-1
	if player.z < 0: player.z = 0
	if player.z > render_distance-1: player.z = render_distance-1

    # toggle blocks
	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4

	# respawn location
	if player.y < -10:
		voxel = Voxel(position = (x,-1,z))
		player.y = +3
		player.x = 0

    # lock and unlock mouse
	if held_keys['tab'] == 1 and tab == 1:
		tab = 0
		try:
			if mouse.locked == True:
				mouse.locked = False
				mouse.visible = True
			else:
				mouse.locked = True
				mouse.visible = False
		except:
			pass
	if held_keys['tab'] == 0 and tab == 0:
		tab = 1

class Bedrock(Button):
	# making and indestructible block
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = dirt_texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)

    # placing blocks on the bedrock
	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				punch_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)

class Voxel(Button):
	# blocks
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)

	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				punch_sound.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = dirt_texture)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)

			if key == 'left mouse down':
				# destroy blocks
				punch_sound.play()
				destroy(self)

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Hand(Entity):
	# hand
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)
	
# render ground
for z in range(render_distance):
	for x in range(render_distance):
		voxel = Voxel(position = (x,0,z))
		voxel = Voxel(position = (x,-1,z), texture=dirt_texture)
		bedrock = Bedrock(position = (x,-2,z))

if __name__ == "__main__":
    player = FirstPersonController()
    sky = Sky()
    hand = Hand()
    app.run()


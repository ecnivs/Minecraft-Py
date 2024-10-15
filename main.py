from ursina import Ursina

class Core:
    def __init__(self):
        self.app = Ursina()

    def run(self):
        self.app.run()


if __name__ == "__main__":
    app = Core()
    app.run()



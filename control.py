class ControlPlayer:

    def __init__(self, obj, mode):
        self.mode = mode
        self.object = obj

    def moveDown(self):
        self.object = self.object.move(self.object.speed)

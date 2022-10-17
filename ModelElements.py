def point3d():
    pass


def angle3d():
    pass


def color():
    pass


def power():
    pass


def scene_id():
    pass


class Camera:
    def __init__(self):
        self.Location = point3d()
        self.Angle = angle3d()
    
    def rotate(self, angle3d):
        pass
    
    def move(self, point3d):
        pass


class Flash:
    def __init__(self):
        self.location = point3d()
        self.angle = angle3d()
        self.color = color()
        self.power = power()

    def rotate(self, angle3d):
        pass
    
    def move(self, point3d):
        pass


class PoligonalModel:
    def __init__(self):
        self.poligons = []
        self.textures = []


class Scene:
    def __init__(self):
        self.id = scene_id()
        self.models = []
        self.flashes = []

    def method1(self, var1: some_type):
        return var1

    def method2(self, var1: some_type, var2: some_type):
        return var1


class ModelElement:
    def create_element(self, name, location, angle):
        if name == 'Flash':
            return Flash(location, angle)
        if name == 'Camera':
            return Camera(location, angle)

from ModelElements import ModelElement, PoligonalModel, Scene, Flash, Camera


class ModelStore:
    def __init__(self):
        self.models = []
        self.scenes = []
        self.flashes = []
        self.cameras = []
        self.__observer = []
        self.__notify = None
        self.__i_model_changer = None

    def add_camera(self, location, angle):
        self.cameras.append(ModelElement('Camera', location, angle))

    def add_flash(self, location, angle):
        self.flashes.append(ModelElement('Flash', location, angle))

    def register_observer(self, observer):
        self.__observer.append(observer)

    def change_observers(self):
        for observer in self.__observer:
            observer.apply_update_model()

    def get_scene(self, scene_id):
        return self.get_scene(scene_id)

    @property
    def notify_change(self):
        pass

    @notify_change.setter
    def notify_change(self, notify):
        self.__notify = notify
        if self.__i_model_changer is not None:
            self.__i_model_changer.model_changer()


class IModelChanger:
    def model_changer(self):
        pass


class IModelChangedObserver(ModelStore):
    def apply_update_model(self):
        pass

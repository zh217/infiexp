import abc


class Experiment(abc.ABC):
    resources = {'CPU': 1, 'GPU': 4}

    def __init__(self):
        pass

    def setup_model(self):
        pass

    def prepare_model(self):
        pass

    def save_model(self):
        pass

    def restore_model(self):
        pass

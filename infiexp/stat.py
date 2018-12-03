class StatAggregator:
    def __init__(self, auto_flush_steps, init_step=0):
        pass

    def flush(self):
        pass

    def log_text(self, data_dict, concat=True, concat_separator='\n'):
        pass

    def log_image(self, data_dict):
        pass

    def log_audio(self, data_dict, concat=True, concat_frames=1600):
        pass

    def log_num(self, data_dict):
        pass

    def log_ma(self, data_dict):
        pass

    def log_acc(self, data_dict):
        pass

    def step(self, n=1):
        pass

    def register(self, callback):
        pass

    def deregister(self, handle):
        pass

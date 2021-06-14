class SingleTon:
    instance = None

    @staticmethod
    def get_instance():
        if SingleTon.instance is None:
            SingleTon()
        return SingleTon.instance

    # @classmethod
    # def get_instance(cls):
    #     if cls.instance is None:
    #         SingleTon()
    #     return cls.instance

    def __init__(self):
        if SingleTon.instance is not None:
            raise Exception('only one instance can exist')
        else:
            self.instance_id = id(self)
            SingleTon.instance = self

    def get_id(self):
        return self.instance_id

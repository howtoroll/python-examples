class SingleTon:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.instance_id = id(self)

    def get_id(self):
        return self.instance_id
